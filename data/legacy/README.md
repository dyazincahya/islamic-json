# Legacy datasets

This directory preserves older public JSON collections in their original, inconsistent formats:

- `asmaul-husna/`
- `dhikr/`
- `dua/`
- `pillars-of-islam/`

These files are retained for compatibility and are not normalized in place. New integrations should use [`../v2/`](../v2/) when an equivalent standardized bilingual resource is available.

Known issue: `dhikr/data/morning-dhikr.json` is an existing malformed/empty legacy resource and is intentionally preserved unchanged.

See [`../../MIGRATION.md`](../../MIGRATION.md) for old-to-new paths and the compatibility-tag strategy.
