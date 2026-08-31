# V2 migration summary

## Scope

V2 standardizes non-Quran and non-hadith data only. Legacy and Quran files are preserved byte-for-byte and are protected by `legacy-checksums.json`. The independent `data/holy-quran` dataset and any hadith-library dataset are excluded from v2 migration; content can reference them only through bibliographic locators.

## Migrated datasets

- 99 Asmaul Husna entries as glossary entries.
- 55 daily dua entries as supplications.
- One draft placeholder for the empty legacy morning-dhikr input.
- Shahada, obligatory prayer, fasting, zakat-fitrah, and Hajj legacy content as typed lessons, practices, supplications, and sequences.

## Learning catalog

The v2 stage catalog contains seven ordered stages. New curriculum content is bilingual (`id` and `en`) and intentionally published as `draft` or `under-review` until source, subject-matter, and locale review are complete.

## Validation record

Run before every release:

```sh
python scripts/build_v2_indexes.py
python scripts/validate_v2.py
python -m unittest discover -s scripts/tests -v
```

The validator verifies schemas, content indexes, IDs, relationships, localization gates, provenance/review metadata, semantic icons, SVG safety, and legacy checksums. A release tag is required before using the documented `@v2.0.0`-style CDN URLs for `data/v2/` in production.
