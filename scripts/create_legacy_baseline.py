#!/usr/bin/env python3
"""Create deterministic inventory and checksum fixtures for legacy JSON data."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
V2_DIR = DATA_DIR / "v2"
INVENTORY_PATH = V2_DIR / "migration" / "legacy-inventory.json"
CHECKSUM_PATH = V2_DIR / "migration" / "legacy-checksums.json"
EXCLUDED_PARTS = {".git", ".agent", ".agents", "openspec", "docs"}
PROTECTED_DATASETS = {"holy-quran", "hadith", "hadist"}


def is_legacy_json(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return (
        relative.parts[:2] in {("data", "legacy"), ("data", "holy-quran")}
        and relative.name != "manifest.json"
        and not any(part in EXCLUDED_PARTS for part in relative.parts)
    )


def inspect_json(path: Path) -> dict[str, Any]:
    relative = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    result: dict[str, Any] = {
        "path": relative,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }

    try:
        value = json.loads(raw.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        result.update({"validJson": False, "parseError": str(error)})
        return result

    root_type = (
        "array"
        if isinstance(value, list)
        else "object"
        if isinstance(value, dict)
        else type(value).__name__
    )
    sample = value[0] if isinstance(value, list) and value else value
    result.update(
        {
            "validJson": True,
            "rootType": root_type,
            "itemCount": len(value) if isinstance(value, list) else 1,
            "sampleFields": sorted(sample.keys()) if isinstance(sample, dict) else [],
        }
    )
    return result


def main() -> int:
    entries = [
        inspect_json(path)
        for path in sorted(ROOT.rglob("*.json"))
        if is_legacy_json(path)
    ]
    public_content = [
        entry
        for entry in entries
        if not any(part in PROTECTED_DATASETS for part in Path(entry["path"]).parts)
    ]
    protected = [entry for entry in entries if entry not in public_content]

    inventory = {
        "schemaVersion": "1.0.0",
        "description": "Migration inventory of legacy non-Quran and non-hadith JSON data.",
        "generatedBy": "scripts/create_legacy_baseline.py",
        "items": [
            {key: value for key, value in entry.items() if key != "sha256"}
            for entry in public_content
        ],
    }
    checksums = {
        "schemaVersion": "1.0.0",
        "description": "Byte-level compatibility baseline for all legacy and protected JSON datasets.",
        "generatedBy": "scripts/create_legacy_baseline.py",
        "items": [
            {
                "path": entry["path"],
                "sha256": entry["sha256"],
                "protected": entry in protected,
            }
            for entry in entries
        ],
    }

    INVENTORY_PATH.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    CHECKSUM_PATH.write_text(
        json.dumps(checksums, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {len(public_content)} inventory entries to {INVENTORY_PATH.relative_to(ROOT)}"
    )
    print(
        f"Wrote {len(entries)} checksums ({len(protected)} protected) to {CHECKSUM_PATH.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
