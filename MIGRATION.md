# Data layout migration guide

The repository has moved public datasets below `data/`. This is a breaking path change for unpinned root-level URLs.

## Compatibility policy

Before release, a maintainer must create and push the immutable compatibility tag described in [`data/v2/migration/compatibility-release.md`](data/v2/migration/compatibility-release.md). No tag is created by this repository change.

- Existing users: replace `<compatibility-tag>` with the announced pre-move tag to keep the old layout.
- New users: pin the current/new release tag and use the `data/` paths below.
- Do not use `main` as a production compatibility guarantee.

## Path map

| Previous path | Compatibility-tag URL path | New path | Recommended alternative |
| --- | --- | --- | --- |
| `asmaul-husna/asmaul-husna.json` | `asmaul-husna/asmaul-husna.json` | `data/legacy/asmaul-husna/asmaul-husna.json` | `data/v2/indexes/glossary.json` |
| `dhikr/` | `dhikr/` | `data/legacy/dhikr/` | `data/v2/indexes/supplications.json` |
| `dua/` | `dua/` | `data/legacy/dua/` | `data/v2/indexes/supplications.json` |
| `pillars-of-islam/` | `pillars-of-islam/` | `data/legacy/pillars-of-islam/` | `data/v2/stages.json` |
| `v2/` | `v2/` | `data/v2/` | `data/v2/manifest.json` |
| `holy-quran/` | `holy-quran/` | `data/holy-quran/` | Independent Quran dataset |

## Version-pinned CDN patterns

Use an immutable release tag in place of `<tag>`.

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@<tag>/data/v2/manifest.json
https://cdn.statically.io/gh/dyazincahya/islamic-json/<tag>/data/v2/manifest.json
https://raw.githubusercontent.com/dyazincahya/islamic-json/<tag>/data/v2/manifest.json
```

The GitHub Pages portal is commit-matched documentation, not a replacement for a version-pinned API release:

```text
https://dyazincahya.github.io/islamic-json/
```
