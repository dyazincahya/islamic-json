from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "validate_v2.py"
SCHEMAS = ("manifest", "stages", "index", "content", "sources", "icons", "features")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def create_schemas(root: Path, *, fixture_contract: bool = True) -> None:
    schema: dict[str, object] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
    }
    if fixture_contract:
        schema.update(
            {
                "properties": {"valid": {"const": True}},
                "required": ["valid"],
            }
        )
    for name in SCHEMAS:
        write_json(root / "data" / "v2" / "schemas" / f"{name}.schema.json", schema)


def create_live_dataset(root: Path) -> None:
    create_schemas(root, fixture_contract=False)
    write_json(
        root / "data" / "v2" / "manifest.json",
        {
            "collections": [
                {"id": "collection.lessons", "path": "indexes/lessons.json"}
            ],
            "assetBaseUrl": "https://cdn.jsdelivr.net/gh/example/data@v2.0.0/data/v2/assets/",
        },
    )
    write_json(
        root / "data" / "v2" / "stages.json",
        {
            "stages": [
                {
                    "id": f"stage.stage-{order}",
                    "order": order,
                    "entryContentId": "lesson.alpha",
                }
                for order in range(1, 8)
            ]
        },
    )
    write_json(
        root / "data" / "v2" / "indexes" / "lessons.json",
        {
            "items": [
                {
                    "id": "lesson.alpha",
                    "type": "lesson",
                    "slug": "alpha",
                    "status": "reviewed",
                    "path": "content/lessons/alpha.json",
                }
            ]
        },
    )
    write_json(
        root / "data" / "v2" / "content" / "lessons" / "alpha.json",
        {
            "id": "lesson.alpha",
            "type": "lesson",
            "slug": "alpha",
            "status": "reviewed",
            "title": {"id": "Alfa", "en": "Alpha"},
            "stageId": "stage.stage-1",
            "nextIds": ["lesson.alpha"],
            "sourceIds": ["source.one"],
            "featureIds": ["feature.reading"],
            "iconId": "general.default",
            "review": {
                "contentReview": {"status": "approved"},
                "localeReviews": {
                    "id": {"status": "approved"},
                    "en": {"status": "approved"},
                },
                "reviewedBy": "reviewer.one",
                "reviewedAt": "2026-08-25",
            },
        },
    )
    write_json(
        root / "data" / "v2" / "registries" / "sources.json", {"sources": [{"id": "source.one"}]}
    )
    write_json(
        root / "data" / "v2" / "registries" / "features.json",
        {"features": [{"id": "feature.reading"}]},
    )
    write_json(
        root / "data" / "v2" / "registries" / "icons.json",
        {
            "icons": [
                {
                    "id": "general.default",
                    "providers": {
                        "materialSymbols": {
                            "name": "circle",
                            "style": "outlined",
                            "provenance": {
                                "provider": "Google",
                                "sourceName": "Material Symbols",
                                "license": "Apache-2.0",
                            },
                        }
                    },
                    "license": {"name": "Apache-2.0"},
                }
            ]
        },
    )


def run_validator(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )


class ValidatorCliTests(unittest.TestCase):
    def test_valid_and_invalid_schema_fixtures_have_expected_outcomes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_schemas(root)
            write_json(
                root / "data" / "v2" / "fixtures" / "valid" / "content" / "lesson.json",
                {"valid": True},
            )
            write_json(
                root / "data" / "v2" / "fixtures" / "invalid" / "content" / "lesson.json",
                {"valid": False},
            )

            result = run_validator(root, "--skip-compatibility")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("2 fixtures", result.stdout)

    def test_invalid_fixture_that_passes_schema_fails_the_suite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_schemas(root)
            write_json(
                root / "data" / "v2" / "fixtures" / "invalid" / "content" / "lesson.json",
                {"valid": True},
            )

            result = run_validator(root, "--skip-compatibility")

            self.assertEqual(result.returncode, 1)
            self.assertIn("invalid fixture unexpectedly passes", result.stderr)

    def test_empty_v2_json_reports_the_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_schemas(root)
            path = root / "data" / "v2" / "fixtures" / "valid" / "content" / "empty.json"
            path.parent.mkdir(parents=True)
            path.write_text("  \n", encoding="utf-8")

            result = run_validator(root, "--skip-compatibility")

            self.assertEqual(result.returncode, 1)
            self.assertIn(
                "data/v2/fixtures/valid/content/empty.json: empty JSON file", result.stderr
            )

    def test_protected_json_is_hashed_without_json_parsing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_schemas(root)
            protected = root / "data" / "holy-quran" / "data.json"
            protected.parent.mkdir(parents=True)
            protected.write_bytes(b"not JSON and intentionally not inspected")
            checksum = hashlib.sha256(protected.read_bytes()).hexdigest()
            write_json(
                root / "data" / "v2" / "migration" / "legacy-checksums.json",
                {
                    "items": [
                        {
                            "path": "data/holy-quran/data.json",
                            "sha256": checksum,
                            "protected": True,
                        }
                    ]
                },
            )

            result = run_validator(root)

            self.assertEqual(result.returncode, 0, result.stderr)

    def test_live_dataset_integrity_and_reviewed_gates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_live_dataset(root)

            valid = run_validator(root, "--skip-compatibility")
            self.assertEqual(valid.returncode, 0, valid.stderr)

            content_path = root / "data" / "v2" / "content" / "lessons" / "alpha.json"
            content = json.loads(content_path.read_text(encoding="utf-8"))
            content["sourceIds"] = ["source.missing"]
            content["review"].pop("reviewedBy")
            content["sources"] = ["free-form citation"]
            write_json(content_path, content)

            invalid = run_validator(root, "--skip-compatibility")
            self.assertEqual(invalid.returncode, 1)
            self.assertIn("unknown source ID 'source.missing'", invalid.stderr)
            self.assertIn("lacks reviewer attribution", invalid.stderr)
            self.assertIn("uses free-form source text", invalid.stderr)

    def test_deprecation_icon_cycle_and_provider_metadata_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_live_dataset(root)
            content_path = root / "data" / "v2" / "content" / "lessons" / "alpha.json"
            content = json.loads(content_path.read_text(encoding="utf-8"))
            content["status"] = "deprecated"
            content["deprecation"] = {
                "reason": {"id": "", "en": "Superseded"},
                "replacementId": "lesson.missing",
            }
            write_json(content_path, content)
            index_path = root / "data" / "v2" / "indexes" / "lessons.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["items"][0]["status"] = "deprecated"
            write_json(index_path, index)
            write_json(
                root / "data" / "v2" / "registries" / "icons.json",
                {
                    "icons": [
                        {
                            "id": "general.default",
                            "fallbackId": "general.other",
                            "providers": {
                                "fontAwesome": {"name": "circle", "style": "invalid"}
                            },
                            "license": "CC-BY-4.0",
                        },
                        {"id": "general.other", "fallbackId": "general.default"},
                    ]
                },
            )

            result = run_validator(root, "--skip-compatibility")

            self.assertEqual(result.returncode, 1)
            self.assertIn("lacks a non-empty bilingual reason", result.stderr)
            self.assertIn("unknown replacement ID 'lesson.missing'", result.stderr)
            self.assertIn("icon fallback cycle", result.stderr)
            self.assertIn("style is invalid", result.stderr)

    def test_unsafe_svg_and_changed_checksum_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_live_dataset(root)
            asset_path = root / "data" / "v2" / "assets" / "icons" / "unsafe.svg"
            asset_path.parent.mkdir(parents=True)
            asset_path.write_text(
                '<svg viewBox="0 0 24 24"><script>alert(1)</script><text>unsafe</text><image href="https://example.com/x"/></svg>',
                encoding="utf-8",
            )
            icons_path = root / "data" / "v2" / "registries" / "icons.json"
            icons = json.loads(icons_path.read_text(encoding="utf-8"))
            icons["icons"][0]["svg"] = {
                "path": "assets/icons/unsafe.svg",
                "origin": "custom",
                "license": {"name": "CC-BY-4.0", "attributionRequired": True},
                "attribution": "Example",
            }
            write_json(icons_path, icons)
            legacy = root / "legacy" / "data.json"
            write_json(legacy, {"unchanged": True})
            write_json(
                root / "data" / "v2" / "migration" / "legacy-checksums.json",
                {
                    "items": [
                        {
                            "path": "legacy/data.json",
                            "sha256": "0" * 64,
                            "protected": False,
                        }
                    ]
                },
            )

            result = run_validator(root)

            self.assertEqual(result.returncode, 1)
            self.assertIn("SVG contains prohibited <script>", result.stderr)
            self.assertIn("font-dependent <text>", result.stderr)
            self.assertIn("external resource reference", result.stderr)
            self.assertIn("legacy dataset checksum changed", result.stderr)

    def test_relative_schema_references_are_resolved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_schemas(root, fixture_contract=False)
            write_json(
                root / "data" / "v2" / "schemas" / "shared.schema.json",
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "type": "object",
                    "required": ["type"],
                },
            )
            write_json(
                root / "data" / "v2" / "schemas" / "content.schema.json",
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "$ref": "shared.schema.json",
                },
            )
            write_json(
                root / "data" / "v2" / "fixtures" / "valid" / "content" / "lesson.json",
                {"type": "lesson"},
            )

            result = run_validator(root, "--skip-compatibility")

            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
