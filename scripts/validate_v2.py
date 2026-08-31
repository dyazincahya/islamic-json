#!/usr/bin/env python3
"""Validate v2 schemas, fixtures, data integrity, assets, and legacy checksums."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from collections.abc import Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse

from jsonschema import exceptions, validators
from referencing import Registry
from referencing.exceptions import Unresolvable
from referencing.jsonschema import DRAFT202012

SCHEMA_FILES = {
    "manifest": "manifest.schema.json",
    "stages": "stages.schema.json",
    "index": "index.schema.json",
    "content": "content.schema.json",
    "sources": "sources.schema.json",
    "icons": "icons.schema.json",
    "features": "features.schema.json",
}
CONTENT_TYPES = {"lesson", "practice", "supplication", "sequence", "glossary-entry"}
SEMANTIC_ID = re.compile(r"^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*$")

PROTECTED_NAMES = ("holy-quran", "hadith", "hadist")
LEGACY_EXCLUDED_PARTS = {".git", ".agent", ".agents", "openspec", "docs"}
REFERENCE_FIELDS = {
    "prerequisite": "entity",
    "prerequisites": "entity",
    "prerequisiteId": "entity",
    "prerequisiteIds": "entity",
    "next": "entity",
    "nextId": "entity",
    "nextIds": "entity",
    "nextContent": "entity",
    "nextContentIds": "entity",
    "related": "entity",
    "relatedId": "entity",
    "relatedIds": "entity",
    "relatedContent": "entity",
    "relatedContentIds": "entity",
    "recitationId": "entity",
    "recitationIds": "entity",
    "replacementId": "entity",
    "replacementIds": "entity",
    "entryContentId": "content",
    "entryContentIds": "content",
    "stageId": "stage",
    "stageIds": "stage",
    "sourceId": "source",
    "sourceIds": "source",
    "featureId": "feature",
    "featureIds": "feature",
    "iconId": "icon",
    "iconIds": "icon",
    "fallbackId": "icon",
}


@dataclass(frozen=True)
class Document:
    path: Path
    relative: str
    value: Any
    role: str | None
    fixture_expectation: str | None = None


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notices: list[str] = []

    def error(self, path: str | Path, message: str) -> None:
        self.errors.append(f"{str(path).replace(chr(92), '/')}: {message}")

    def notice(self, message: str) -> None:
        self.notices.append(message)


def json_pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def walk(
    value: Any, path: tuple[Any, ...] = ()
) -> Iterator[tuple[tuple[Any, ...], Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path + (index,))


def read_json(path: Path, display: str, reporter: Reporter) -> Any | None:
    try:
        raw = path.read_bytes()
    except OSError as error:
        reporter.error(display, f"cannot read file: {error}")
        return None
    if not raw or not raw.strip():
        reporter.error(display, "empty JSON file")
        return None
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        reporter.error(display, f"invalid UTF-8 at byte {error.start}: {error.reason}")
        return None
    try:
        value = json.loads(text)
    except json.JSONDecodeError as error:
        reporter.error(
            display,
            f"malformed JSON at line {error.lineno}, column {error.colno}: {error.msg}",
        )
        return None
    if value is None:
        reporter.error(display, "empty JSON value (null is not a document)")
        return None
    return value


def fixture_details(
    relative: PurePosixPath, value: Any
) -> tuple[str | None, str | None]:
    parts = list(relative.parts)
    if "fixtures" not in parts:
        return None, None
    index = parts.index("fixtures")
    tail = [part.lower() for part in parts[index + 1 :]]
    expectation = next((part for part in tail if part in {"valid", "invalid"}), None)
    if expectation is None:
        return None, None

    schema_hint = None
    if isinstance(value, dict) and isinstance(value.get("$schema"), str):
        schema_name = PurePosixPath(value["$schema"].split("#", 1)[0]).name
        schema_hint = next(
            (
                role
                for role, filename in SCHEMA_FILES.items()
                if filename == schema_name
            ),
            None,
        )
    if schema_hint:
        return expectation, schema_hint

    searchable = "/".join(tail)
    for role in (
        "manifest",
        "stages",
        "sources",
        "icons",
        "features",
        "index",
        "content",
    ):
        if re.search(rf"(^|[/_.-]){re.escape(role)}(?:es)?([/_.-]|$)", searchable):
            return expectation, role
    if isinstance(value, dict):
        document_type = value.get("type") or value.get("documentType")
        if document_type in CONTENT_TYPES:
            return expectation, "content"
    return expectation, None


def live_role(relative: PurePosixPath) -> str | None:
    value = relative.as_posix()
    if value == "manifest.json":
        return "manifest"
    if value == "stages.json":
        return "stages"
    if len(relative.parts) >= 2 and relative.parts[0] == "indexes":
        return "index"
    if len(relative.parts) >= 2 and relative.parts[0] == "content":
        return "content"
    registry_roles = {
        "registries/sources.json": "sources",
        "registries/icons.json": "icons",
        "registries/features.json": "features",
    }
    return registry_roles.get(value)


def parse_v2(v2_dir: Path, root: Path, reporter: Reporter) -> list[Document]:
    documents: list[Document] = []
    if not v2_dir.is_dir():
        reporter.error("v2", "directory does not exist")
        return documents
    for path in sorted(v2_dir.rglob("*.json")):
        relative_root = path.relative_to(root).as_posix()
        relative_v2 = PurePosixPath(path.relative_to(v2_dir).as_posix())
        value = read_json(path, relative_root, reporter)
        if value is None:
            continue
        expectation, fixture_role = fixture_details(relative_v2, value)
        role = fixture_role if expectation else live_role(relative_v2)
        documents.append(Document(path, relative_root, value, role, expectation))
        if (
            expectation is None
            and role is None
            and relative_v2.parts[0] not in {"schemas", "migration"}
        ):
            reporter.error(
                relative_root, "no expected v2 schema can be selected for this path"
            )
    return documents


def load_schemas(
    v2_dir: Path, root: Path, documents: Sequence[Document], reporter: Reporter
) -> dict[str, Any]:
    schema_dir = v2_dir / "schemas"
    parsed = {document.path: document.value for document in documents}
    schemas: dict[str, Any] = {}
    for role, filename in SCHEMA_FILES.items():
        path = schema_dir / filename
        display = path.relative_to(root).as_posix()
        if not path.is_file():
            reporter.error(display, f"required {role} schema is missing")
            continue
        schema = parsed.get(path)
        if schema is None:
            schema = read_json(path, display, reporter)
        if schema is not None:
            schemas[role] = schema

    for path in sorted(schema_dir.glob("*.schema.json")) if schema_dir.is_dir() else []:
        schema = parsed.get(path)
        if schema is None:
            continue
        try:
            validator_class = validators.validator_for(schema)
            validator_class.check_schema(schema)
        except exceptions.SchemaError as error:
            reporter.error(
                path.relative_to(root).as_posix(),
                f"invalid JSON Schema at {json_pointer(error.schema_path)}: {error.message}",
            )
    return schemas


def build_schema_registry(schema_dir: Path) -> Registry:
    registry = Registry()
    for path in sorted(schema_dir.glob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8-sig"))
        resource = DRAFT202012.create_resource(schema)
        registry = registry.with_resource(path.resolve().as_uri(), resource)
        schema_id = schema.get("$id") if isinstance(schema, dict) else None
        if isinstance(schema_id, str):
            registry = registry.with_resource(schema_id, resource)
    return registry


def schema_errors(
    document: Document, schema: Any, registry: Registry, schema_uri: str
) -> list[str]:
    validator_class = validators.validator_for(schema)
    validator_class.check_schema(schema)
    effective_schema = schema
    if isinstance(schema, dict) and "$id" not in schema:
        effective_schema = {"$id": schema_uri, **schema}
    validator = validator_class(effective_schema, registry=registry)
    return [
        f"schema violation at {json_pointer(error.absolute_path)}: {error.message}"
        for error in sorted(
            validator.iter_errors(document.value),
            key=lambda item: list(item.absolute_path),
        )
    ]


def validate_instances(
    documents: Sequence[Document],
    schemas: Mapping[str, Any],
    root: Path,
    reporter: Reporter,
) -> None:
    try:
        v2_dir = root / "data" / "v2"
        registry = build_schema_registry(v2_dir / "schemas")
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        reporter.error(
            "data/v2/schemas", f"cannot build schema reference registry: {error}"
        )
        return
    for document in documents:
        if document.role is None:
            if document.fixture_expectation:
                reporter.error(
                    document.relative,
                    "fixture schema cannot be inferred from its path, name, $schema, or type",
                )
            continue
        schema = schemas.get(document.role)
        if schema is None:
            continue
        try:
            schema_path = v2_dir / "schemas" / SCHEMA_FILES[document.role]
            errors = schema_errors(
                document, schema, registry, schema_path.resolve().as_uri()
            )
        except (exceptions.SchemaError, Unresolvable, OSError) as error:
            reporter.error(
                document.relative, f"cannot apply {document.role} schema: {error}"
            )
            continue
        if document.fixture_expectation == "invalid":
            if not errors:
                reporter.error(
                    document.relative,
                    f"invalid fixture unexpectedly passes {document.role} schema",
                )
            continue
        for error in errors:
            prefix = (
                "valid fixture failed: "
                if document.fixture_expectation == "valid"
                else ""
            )
            reporter.error(document.relative, prefix + error)


def registry_entries(document: Document, preferred_key: str) -> list[dict[str, Any]]:
    value = document.value
    if isinstance(value, list):
        return [entry for entry in value if isinstance(entry, dict)]
    if not isinstance(value, dict):
        return []
    for key in (preferred_key, "items", "entries"):
        candidate = value.get(key)
        if isinstance(candidate, list):
            return [entry for entry in candidate if isinstance(entry, dict)]
    return []


def root_id(document: Document) -> str | None:
    return (
        document.value.get("id")
        if isinstance(document.value, dict)
        and isinstance(document.value.get("id"), str)
        else None
    )


def collect_identifiers(
    live: Sequence[Document], reporter: Reporter
) -> tuple[dict[str, set[str]], dict[str, list[tuple[str, str]]]]:
    namespaces: dict[str, set[str]] = defaultdict(set)
    locations: dict[str, list[tuple[str, str]]] = defaultdict(list)

    def add(
        identifier: Any, namespace: str, location: str, pointer: tuple[Any, ...]
    ) -> None:
        if not isinstance(identifier, str) or not SEMANTIC_ID.fullmatch(identifier):
            return
        namespaces[namespace].add(identifier)
        locations[identifier].append((location, json_pointer(pointer)))

    for document in live:
        if document.role == "index":
            continue
        if document.role in {"sources", "icons", "features", "stages"}:
            key = document.role if document.role != "stages" else "stages"
            namespace = (
                document.role[:-1] if document.role.endswith("s") else document.role
            )
            for index, entry in enumerate(registry_entries(document, key)):
                add(entry.get("id"), namespace, document.relative, (key, index, "id"))
            continue
        if document.role != "content":
            continue
        for pointer, value in walk(document.value):
            if not isinstance(value, dict) or "id" not in value:
                continue
            if "en" in value and set(value).issubset({"id", "en"}):
                continue
            add(value.get("id"), "content", document.relative, pointer + ("id",))

    for identifier, found in sorted(locations.items()):
        unique_locations = set(found)
        if len(unique_locations) > 1:
            rendered = ", ".join(
                f"{path}{pointer}" for path, pointer in sorted(unique_locations)
            )
            reporter.error(
                "v2", f"duplicate globally unique ID {identifier!r}: {rendered}"
            )
    namespaces["entity"] = set().union(*namespaces.values()) if namespaces else set()
    return namespaces, locations


def valid_relative_path(value: Any) -> bool:
    if (
        not isinstance(value, str)
        or not value
        or "\\" in value
        or "?" in value
        or "#" in value
    ):
        return False
    parsed = urlparse(value)
    path = PurePosixPath(value)
    return (
        not parsed.scheme
        and not parsed.netloc
        and not path.is_absolute()
        and ".." not in path.parts
        and "." not in path.parts
    )


def index_entries(document: Document) -> list[dict[str, Any]]:
    return registry_entries(document, "items")


def validate_indexes(
    live: Sequence[Document],
    v2_dir: Path,
    namespaces: Mapping[str, set[str]],
    reporter: Reporter,
) -> None:
    content_by_path = {
        document.path.relative_to(v2_dir).as_posix(): document
        for document in live
        if document.role == "content"
    }
    indexed_content: set[str] = set()
    indexed_ids: dict[str, str] = {}
    expected_by_directory = {
        "lessons": "lesson",
        "practices": "practice",
        "supplications": "supplication",
        "sequences": "sequence",
        "glossary": "glossary-entry",
    }

    for path, document in content_by_path.items():
        parts = PurePosixPath(path).parts
        if len(parts) >= 2 and isinstance(document.value, dict):
            expected = expected_by_directory.get(parts[1])
            actual = document.value.get("type") or document.value.get("documentType")
            if expected and actual != expected:
                reporter.error(
                    document.relative,
                    f"document type {actual!r} disagrees with content directory {parts[1]!r} (expected {expected!r})",
                )

    for index_document in (document for document in live if document.role == "index"):
        for position, entry in enumerate(index_entries(index_document)):
            pointer = f"/items/{position}"
            item_path = entry.get("path") or entry.get("documentPath")
            if not valid_relative_path(item_path):
                reporter.error(
                    index_document.relative,
                    f"{pointer}/path is not a safe v2-relative path: {item_path!r}",
                )
                continue
            normalized = PurePosixPath(str(item_path)).as_posix()
            target = content_by_path.get(normalized)
            if target is None:
                reporter.error(
                    index_document.relative,
                    f"{pointer}/path does not resolve to v2 content: {normalized!r}",
                )
                continue
            indexed_content.add(normalized)
            target_value = target.value if isinstance(target.value, dict) else {}
            comparisons = {
                "id": target_value.get("id"),
                "type": target_value.get("type") or target_value.get("documentType"),
                "slug": target_value.get("slug"),
            }
            for field, actual in comparisons.items():
                if field in entry and entry[field] != actual:
                    reporter.error(
                        index_document.relative,
                        f"{pointer}/{field} is {entry[field]!r}, but {normalized!r} declares {actual!r}",
                    )
            identifier = entry.get("id")
            if isinstance(identifier, str):
                previous = indexed_ids.get(identifier)
                if previous and previous != normalized:
                    reporter.error(
                        index_document.relative,
                        f"index ID {identifier!r} points to both {previous!r} and {normalized!r}",
                    )
                indexed_ids[identifier] = normalized
                if identifier not in namespaces.get("content", set()):
                    reporter.error(
                        index_document.relative,
                        f"{pointer}/id references unknown content ID {identifier!r}",
                    )

    for path, document in sorted(content_by_path.items()):
        if path not in indexed_content:
            reporter.error(
                document.relative,
                "content document is not present in any collection index",
            )


def extract_reference_ids(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from extract_reference_ids(item)
    elif isinstance(value, dict):
        for key in (
            "targetId",
            "id",
            "contentId",
            "sourceId",
            "featureId",
            "iconId",
            "stageId",
        ):
            if isinstance(value.get(key), str):
                yield value[key]
                return


def validate_references(
    live: Sequence[Document], namespaces: Mapping[str, set[str]], reporter: Reporter
) -> None:
    for document in live:
        if document.role not in {"content", "stages"}:
            continue
        owner = root_id(document) or document.relative
        for pointer, value in walk(document.value):
            if not pointer or not isinstance(pointer[-1], str):
                continue
            field = pointer[-1]
            namespace = REFERENCE_FIELDS.get(field)
            if namespace is None and field == "targetId":
                namespace = "entity"
            if namespace is None:
                continue
            for target in extract_reference_ids(value):
                if target not in namespaces.get(namespace, set()):
                    reporter.error(
                        document.relative,
                        f"{json_pointer(pointer)} on {owner!r} references unknown {namespace} ID {target!r}",
                    )


def validate_manifest(
    live: Sequence[Document], v2_dir: Path, reporter: Reporter
) -> None:
    for document in (item for item in live if item.role == "manifest"):
        if not isinstance(document.value, dict):
            continue
        collections = document.value.get("collections", [])
        if isinstance(collections, dict):
            collections = list(collections.values())
        if isinstance(collections, list):
            for index, collection in enumerate(collections):
                if not isinstance(collection, dict):
                    continue
                path = collection.get("path") or collection.get("indexPath")
                if not valid_relative_path(path):
                    reporter.error(
                        document.relative,
                        f"/collections/{index}/path is not a safe v2-relative path: {path!r}",
                    )
                elif not (v2_dir / PurePosixPath(str(path))).is_file():
                    reporter.error(
                        document.relative,
                        f"/collections/{index}/path does not exist: {path!r}",
                    )


def localized_complete(value: Any) -> bool:
    return isinstance(value, dict) and all(
        isinstance(value.get(locale), str) and value[locale].strip()
        for locale in ("id", "en")
    )


def validate_deprecations(
    live: Sequence[Document], namespaces: Mapping[str, set[str]], reporter: Reporter
) -> None:
    for document in (item for item in live if item.role == "content"):
        if not isinstance(document.value, dict) or "deprecation" not in document.value:
            continue
        item = document.value
        identifier = item.get("id", document.relative)
        if not isinstance(item.get("id"), str) or not item["id"].strip():
            reporter.error(
                document.relative, "deprecated item does not retain a stable ID"
            )
        deprecation_value = item.get("deprecation")
        deprecation: dict[str, Any] = (
            deprecation_value if isinstance(deprecation_value, dict) else {}
        )
        reason = deprecation.get("reason")
        if not localized_complete(reason):
            reporter.error(
                document.relative,
                f"deprecated item {identifier!r} lacks a non-empty bilingual reason",
            )
        replacement = deprecation.get("replacementId")
        if replacement is not None:
            if replacement == item.get("id"):
                reporter.error(
                    document.relative,
                    f"deprecated item {identifier!r} cannot replace itself",
                )
            elif replacement not in namespaces.get("entity", set()):
                reporter.error(
                    document.relative,
                    f"deprecated item {identifier!r} has unknown replacement ID {replacement!r}",
                )


def stage_entries(document: Document) -> list[dict[str, Any]]:
    return registry_entries(document, "stages")


def validate_stages(
    live: Sequence[Document], namespaces: Mapping[str, set[str]], reporter: Reporter
) -> None:
    stage_documents = [item for item in live if item.role == "stages"]
    for document in stage_documents:
        stages = stage_entries(document)
        if len(stages) != 7:
            reporter.error(
                document.relative,
                f"stage catalog must contain exactly seven stages, found {len(stages)}",
            )
        orders = [stage.get("order") for stage in stages]
        if sorted(order for order in orders if isinstance(order, int)) != list(
            range(1, 8)
        ):
            reporter.error(
                document.relative,
                "stage orders must be the unique integers 1 through 7",
            )
        for index, stage in enumerate(stages):
            entry = stage.get("entryContentId") or stage.get("entryId")
            if isinstance(entry, str) and entry not in namespaces.get("content", set()):
                reporter.error(
                    document.relative,
                    f"/stages/{index}/entryContentId references unknown content ID {entry!r}",
                )


def icon_entries(
    live: Sequence[Document],
) -> list[tuple[Document, int, dict[str, Any]]]:
    result = []
    for document in (item for item in live if item.role == "icons"):
        result.extend(
            (document, index, entry)
            for index, entry in enumerate(registry_entries(document, "icons"))
        )
    return result


def validate_icon_registry(
    live: Sequence[Document], root: Path, v2_dir: Path, reporter: Reporter
) -> None:
    entries = icon_entries(live)
    by_id: dict[str, tuple[Document, int, dict[str, Any]]] = {}
    for document, index, entry in entries:
        identifier = entry.get("id")
        if isinstance(identifier, str):
            by_id[identifier] = (document, index, entry)
    for identifier in sorted(by_id):
        chain: list[str] = []
        current: str | None = identifier
        while current is not None:
            if current in chain:
                cycle = chain[chain.index(current) :] + [current]
                document, _, _ = by_id[identifier]
                reporter.error(
                    document.relative, f"icon fallback cycle: {' -> '.join(cycle)}"
                )
                break
            chain.append(current)
            record = by_id.get(current)
            if record is None:
                document, _, _ = by_id[identifier]
                reporter.error(
                    document.relative,
                    f"icon {identifier!r} has unknown fallback {current!r}",
                )
                break
            fallback = record[2].get("fallbackId")
            current = fallback if isinstance(fallback, str) else None

    view_boxes: dict[str, list[str]] = defaultdict(list)
    styles: dict[str, list[str]] = defaultdict(list)
    for document, index, entry in entries:
        pointer = f"/icons/{index}"
        mappings = entry.get("providers") or entry.get("providerMappings")
        if isinstance(mappings, dict):
            for provider, mapping in mappings.items():
                if provider not in {"fontAwesome", "materialSymbols"}:
                    reporter.error(
                        document.relative,
                        f"{pointer}/providers has unsupported provider {provider!r}",
                    )
                if isinstance(mapping, str):
                    if not mapping.strip():
                        reporter.error(
                            document.relative,
                            f"{pointer}/providers/{provider} is empty",
                        )
                elif isinstance(mapping, dict):
                    provenance = mapping.get("provenance")
                    if not isinstance(provenance, dict) or not provenance.get(
                        "license"
                    ):
                        reporter.error(
                            document.relative,
                            f"{pointer}/providers/{provider} lacks provenance license metadata",
                        )
                    name = mapping.get("name") or mapping.get("iconName")
                    if not isinstance(name, str) or not name.strip():
                        reporter.error(
                            document.relative,
                            f"{pointer}/providers/{provider} lacks a non-empty icon name",
                        )
                    style = mapping.get("style")
                    allowed_styles = {
                        "fontAwesome": {
                            "solid",
                            "regular",
                            "brands",
                            "light",
                            "thin",
                            "duotone",
                            "sharp",
                        },
                        "materialSymbols": {"outlined", "rounded", "sharp"},
                    }
                    if style is not None and style not in allowed_styles.get(
                        provider, set()
                    ):
                        reporter.error(
                            document.relative,
                            f"{pointer}/providers/{provider}/style is invalid: {style!r}",
                        )
                else:
                    reporter.error(
                        document.relative,
                        f"{pointer}/providers/{provider} must be a string or object",
                    )

        asset = entry.get("svg") or entry.get("asset")
        if not isinstance(asset, dict):
            continue
        asset_path = asset.get("path")
        if not valid_relative_path(asset_path) or not str(asset_path).lower().endswith(
            ".svg"
        ):
            reporter.error(
                document.relative,
                f"{pointer}/svg/path is not a safe relative SVG path: {asset_path!r}",
            )
            continue
        provenance = asset.get("provenance")
        if not isinstance(provenance, dict) or not (
            provenance.get("provider") or provenance.get("sourceName")
        ):
            reporter.error(
                document.relative, f"{pointer}/svg lacks provider or origin metadata"
            )
        license_data = (
            (provenance or {}).get("license")
            or asset.get("license")
            or entry.get("license")
            or entry.get("licensing")
        )
        if not license_data:
            reporter.error(document.relative, f"{pointer}/svg lacks license metadata")
        attribution_required = (
            isinstance(license_data, dict)
            and license_data.get("attributionRequired") is True
        )
        if attribution_required and not (
            asset.get("attribution") or entry.get("attribution")
        ):
            reporter.error(
                document.relative, f"{pointer}/svg lacks required attribution"
            )
        svg_path = v2_dir / PurePosixPath(str(asset_path))
        if not svg_path.is_file():
            reporter.error(
                document.relative, f"{pointer}/svg/path does not exist: {asset_path!r}"
            )
            continue
        view_box, style = validate_svg(svg_path, root, reporter)
        if view_box:
            view_boxes[view_box].append(svg_path.relative_to(root).as_posix())
        if style:
            styles[style].append(svg_path.relative_to(root).as_posix())
    if len(view_boxes) > 1:
        reporter.error(
            "data/v2/assets/icons",
            f"SVG assets use inconsistent viewBox values: {', '.join(sorted(view_boxes))}",
        )
    if len(styles) > 1:
        reporter.error(
            "data/v2/assets/icons",
            f"SVG assets use inconsistent declared styles: {', '.join(sorted(styles))}",
        )


def local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1].lower()


def validate_svg(
    path: Path, root: Path, reporter: Reporter
) -> tuple[str | None, str | None]:
    display = path.relative_to(root).as_posix()
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        reporter.error(display, f"cannot read UTF-8 SVG: {error}")
        return None, None
    if re.search(r"<!DOCTYPE|<!ENTITY", text, re.IGNORECASE):
        reporter.error(
            display, "SVG contains a prohibited DOCTYPE or entity declaration"
        )
    try:
        svg = ET.fromstring(text)
    except ET.ParseError as error:
        reporter.error(display, f"malformed SVG XML: {error}")
        return None, None
    if local_name(svg.tag) != "svg":
        reporter.error(display, "root element is not <svg>")
    view_box = svg.attrib.get("viewBox") or svg.attrib.get("viewbox")
    if not view_box or not re.fullmatch(
        r"-?(?:\d+(?:\.\d+)?|\.\d+)\s+-?(?:\d+(?:\.\d+)?|\.\d+)\s+(?:\d+(?:\.\d+)?|\.\d+)\s+(?:\d+(?:\.\d+)?|\.\d+)",
        view_box.strip(),
    ):
        reporter.error(display, "SVG lacks a valid four-number viewBox")
        view_box = None
    declared_style = None
    for element in svg.iter():
        tag = local_name(element.tag)
        if tag == "script":
            reporter.error(display, "SVG contains prohibited <script>")
        if tag == "text":
            reporter.error(display, "SVG contains font-dependent <text>")
        if "class" in element.attrib:
            reporter.error(
                display, "SVG contains presentation-library class attributes"
            )
        if tag == "style":
            reporter.error(display, "SVG contains an embedded <style> block")
        for attribute, value in element.attrib.items():
            attribute_name = local_name(attribute)
            lowered = value.strip().lower()
            if attribute_name.startswith("on"):
                reporter.error(
                    display, f"SVG contains event handler attribute {attribute_name!r}"
                )
            if (
                attribute_name in {"href", "src"}
                and lowered
                and not lowered.startswith("#")
            ):
                reporter.error(
                    display, f"SVG contains external resource reference {value!r}"
                )
            if re.search(r"url\(\s*['\"]?(?!#)", value, re.IGNORECASE):
                reporter.error(
                    display, f"SVG contains external CSS resource reference {value!r}"
                )
            if attribute_name == "data-style" and value.strip():
                declared_style = value.strip()
    return view_box.strip() if view_box else None, declared_style


def validate_asset_base_url(live: Sequence[Document], reporter: Reporter) -> None:
    has_assets = bool(
        icon_entries(live)
        and any(
            (entry.get("svg") or entry.get("asset"))
            for _, _, entry in icon_entries(live)
        )
    )
    if not has_assets:
        return
    manifests = [
        item
        for item in live
        if item.role == "manifest" and isinstance(item.value, dict)
    ]
    for document in manifests:
        url = document.value.get("assetBaseUrl") or document.value.get("assetsBaseUrl")
        if not isinstance(url, str) or not url.strip():
            reporter.error(
                document.relative,
                "SVG assets exist but the manifest has no assetBaseUrl",
            )
            continue
        lowered = url.lower()
        if any(
            token in lowered
            for token in (
                "@main",
                "@master",
                "@latest",
                "/main/",
                "/master/",
                "/latest/",
            )
        ):
            reporter.error(
                document.relative,
                f"assetBaseUrl is mutable rather than version-pinned: {url!r}",
            )
        if ("cdn.jsdelivr.net" in lowered or "unpkg.com" in lowered) and not re.search(
            r"@[^/]+/", url
        ):
            reporter.error(
                document.relative,
                f"assetBaseUrl does not contain a pinned package/repository version: {url!r}",
            )


def protected_path(path: str) -> bool:
    return any(
        any(name in part.lower() for name in PROTECTED_NAMES)
        for part in PurePosixPath(path).parts
    )


def is_legacy_json(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return (
        relative.parts[:2] in {("data", "legacy"), ("data", "holy-quran")}
        and relative.name != "manifest.json"
        and not any(part in LEGACY_EXCLUDED_PARTS for part in relative.parts)
    )


def validate_compatibility(root: Path, v2_dir: Path, reporter: Reporter) -> None:
    baseline_path = v2_dir / "migration" / "legacy-checksums.json"
    display = baseline_path.relative_to(root).as_posix()
    if not baseline_path.is_file():
        reporter.error(display, "legacy checksum baseline is missing")
        return
    baseline = read_json(baseline_path, display, reporter)
    if not isinstance(baseline, dict) or not isinstance(baseline.get("items"), list):
        reporter.error(display, "baseline must contain an items array")
        return
    expected_paths: set[str] = set()
    for index, item in enumerate(baseline["items"]):
        if not isinstance(item, dict):
            reporter.error(display, f"/items/{index} must be an object")
            continue
        path_value = item.get("path")
        checksum = item.get("sha256")
        if not valid_relative_path(path_value):
            reporter.error(display, f"/items/{index}/path is unsafe: {path_value!r}")
            continue
        normalized_path = str(path_value)
        if normalized_path in expected_paths:
            reporter.error(display, f"duplicate checksum path {path_value!r}")
            continue
        expected_paths.add(normalized_path)
        if protected_path(normalized_path) and item.get("protected") is not True:
            reporter.error(
                display,
                f"protected Quran/hadith path is not marked protected: {path_value!r}",
            )
        target = root / PurePosixPath(normalized_path)
        if not target.is_file():
            reporter.error(normalized_path, "legacy compatibility file is missing")
            continue
        try:
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
        except OSError as error:
            reporter.error(normalized_path, f"cannot checksum legacy file: {error}")
            continue
        if not isinstance(checksum, str) or not re.fullmatch(r"[0-9a-f]{64}", checksum):
            reporter.error(
                display, f"/items/{index}/sha256 is not a lowercase SHA-256 digest"
            )
        elif actual != checksum:
            label = "protected dataset" if item.get("protected") else "legacy dataset"
            reporter.error(
                normalized_path,
                f"{label} checksum changed (expected {checksum}, got {actual})",
            )

    current_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*.json")
        if is_legacy_json(path, root)
    }
    for path in sorted(current_paths - expected_paths):
        reporter.error(
            path,
            "legacy JSON is not recorded in data/v2/migration/legacy-checksums.json",
        )


def validate_integrity(
    live: Sequence[Document], root: Path, v2_dir: Path, reporter: Reporter
) -> None:
    namespaces, _ = collect_identifiers(live, reporter)
    validate_manifest(live, v2_dir, reporter)
    validate_indexes(live, v2_dir, namespaces, reporter)
    validate_references(live, namespaces, reporter)
    validate_deprecations(live, namespaces, reporter)
    validate_stages(live, namespaces, reporter)
    validate_icon_registry(live, root, v2_dir, reporter)
    validate_asset_base_url(live, reporter)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate OpenSpec v2 JSON schemas, fixtures, graph integrity, SVG safety, and legacy checksums.",
        epilog="Documented repository command: python scripts/validate_v2.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--skip-compatibility",
        action="store_true",
        help="skip legacy checksum verification (intended only for isolated tooling tests)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    v2_dir = root / "data" / "v2"
    reporter = Reporter()
    documents = parse_v2(v2_dir, root, reporter)
    schemas = load_schemas(v2_dir, root, documents, reporter)
    validate_instances(documents, schemas, root, reporter)
    live = [
        document
        for document in documents
        if document.fixture_expectation is None and document.role is not None
    ]
    validate_integrity(live, root, v2_dir, reporter)
    if not args.skip_compatibility:
        validate_compatibility(root, v2_dir, reporter)

    for notice in reporter.notices:
        print(f"NOTICE: {notice}")
    if reporter.errors:
        print(
            f"Validation failed with {len(reporter.errors)} error(s):", file=sys.stderr
        )
        for error in reporter.errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    fixture_count = sum(
        document.fixture_expectation is not None for document in documents
    )
    live_count = len(live)
    print(
        f"Validation passed: {len(schemas)} schemas, {live_count} live JSON documents, {fixture_count} fixtures."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
