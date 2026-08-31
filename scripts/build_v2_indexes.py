#!/usr/bin/env python3
"""Generate v2 collection and stage indexes from typed content documents."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "data" / "v2"
TITLES = {
    "lesson": {"id": "Pelajaran", "en": "Lessons"},
    "practice": {"id": "Praktik", "en": "Practices"},
    "supplication": {"id": "Doa dan zikir", "en": "Supplications and remembrance"},
    "sequence": {"id": "Rangkaian ibadah", "en": "Worship sequences"},
    "glossary-entry": {"id": "Glosarium", "en": "Glossary"},
}
PLURALS = {
    "lesson": "lessons",
    "practice": "practices",
    "supplication": "supplications",
    "sequence": "sequences",
    "glossary-entry": "glossary",
}


def write(path, value):
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main():
    items = defaultdict(list)
    stage_items = defaultdict(list)
    for path in sorted((V2 / "content").rglob("*.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        kind = value["type"]
        relative = path.relative_to(V2).as_posix()
        entry = {key: value[key] for key in ("id", "type", "slug")}
        entry["path"] = relative
        for key in ("stageId", "stageOrder", "group", "seasonalTags"):
            if key in value:
                entry[key] = value[key]
        items[kind].append(entry)
        if "stageId" in value:
            stage_items[value["stageId"]].append(entry)
    for kind, entries in items.items():
        entries.sort(
            key=lambda entry: (
                entry.get("stageId", ""),
                entry.get("stageOrder", 0),
                entry["id"],
            )
        )
        write(
            V2 / "indexes" / f"{PLURALS[kind]}.json",
            {
                "schemaVersion": "2.0",
                "type": "collection-index",
                "id": f"collection.{PLURALS[kind]}",
                "itemType": kind,
                "title": TITLES[kind],
                "items": entries,
            },
        )
    stages_path = V2 / "stages.json"
    stages = json.loads(stages_path.read_text(encoding="utf-8"))
    for stage in stages["stages"]:
        stage["contentIds"] = [
            entry["id"]
            for entry in sorted(
                stage_items[stage["id"]],
                key=lambda entry: (entry.get("stageOrder", 0), entry["id"]),
            )
        ]
        write(
            V2 / stage["indexPath"],
            {
                "schemaVersion": "2.0",
                "type": "collection-index",
                "id": f"collection.{stage['id'].removeprefix('stage.')}",
                "itemType": "lesson",
                "title": stage["title"],
                "items": [
                    entry
                    for entry in sorted(
                        stage_items[stage["id"]],
                        key=lambda entry: (entry.get("stageOrder", 0), entry["id"]),
                    )
                    if entry["type"] == "lesson"
                ],
            },
        )
    write(stages_path, stages)
    print(
        f"Generated {len(items)} collection indexes and {len(stages['stages'])} stage indexes."
    )


if __name__ == "__main__":
    main()
