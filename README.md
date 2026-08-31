# Islamic JSON

Open Islamic JSON datasets for applications, learning tools, and references.

## Start here

Load [`manifest.json`](manifest.json) to discover the current dataset, retained legacy data, Quran dataset, documentation portal, and migration guide.

```text
data/
├── v2/          Current multilingual structured learning data
├── legacy/      Original collections retained for compatibility
└── holy-quran/  Independent Quran dataset (not legacy)
```

> **Breaking path change:** the historical root-level data directories now live under `data/`. See [`MIGRATION.md`](MIGRATION.md) before updating an existing integration. A pre-move compatibility tag must be explicitly created by a maintainer before release; this change does not create or push one.

## Current v2 dataset

`data/v2/` is the versioned contract for new non-Quran and non-hadith content. It supports Indonesian (`id`) and English (`en`). Start with [`data/v2/manifest.json`](data/v2/manifest.json), which declares collection indexes, stages, registries, and the asset base URL.

```text
data/v2/
├── manifest.json
├── stages.json
├── indexes/
├── content/
├── registries/
├── schemas/
└── assets/icons/
```

### Content conventions

- Each item has an immutable semantic `id`, URL `slug`, `type`, and publication `status`.
- Localized user-facing fields use `{ "id": "…", "en": "…" }`; IDs never contain translated text.
- Rich content uses typed `blocks`, not HTML.
- Arabic recitation uses `arabic`; transliteration and meaning translations are separate localized fields.
- `sourceIds` point to the structured source registry. Technical validation is not scholarly approval.
- Content uses semantic `iconId` values. Consumers can map them to Font Awesome, Material Symbols, local assets, or optional repository SVGs.
- User progress, location, reminders, and bookmarks belong to consuming applications.

## CDN access

Use a published immutable Git tag in place of `<tag>` for production. `main` is mutable and should only be used for development.

### jsDelivr (recommended)

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@<tag>/<path>
```

Example:

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@<tag>/data/v2/manifest.json
```

### Statically (alternative)

```text
https://cdn.statically.io/gh/dyazincahya/islamic-json/<tag>/<path>
```

### GitHub Raw (debugging fallback)

```text
https://raw.githubusercontent.com/dyazincahya/islamic-json/<tag>/<path>
```

The documentation portal will provide copyable URLs, JSON previews, and integration snippets after deployment:

```text
https://dyazincahya.github.io/islamic-json/
```

## Consumer example

```js
const baseUrl =
  "https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@<tag>/data/v2/";
const manifest = await fetch(`${baseUrl}manifest.json`).then((response) =>
  response.json(),
);
const lessons = await fetch(
  `${baseUrl}${manifest.collections[0].indexPath}`,
).then((response) => response.json());
const locale = "id";

const firstLesson = lessons.items[0];
const lesson = await fetch(`${baseUrl}${firstLesson.path}`).then((response) =>
  response.json(),
);
console.log(lesson.title[locale] ?? lesson.title[manifest.defaultLocale]);
```

## Validation and contribution

```sh
python scripts/build_v2_indexes.py
python scripts/validate_v2.py
python -m unittest discover -s scripts/tests -v
```

Contributors must preserve both supported locales, use schema-defined blocks and semantic registry IDs, and keep unverified material as `draft`, `translated`, or `under-review`. See [`data/v2/migration/README.md`](data/v2/migration/README.md) for v2 scope and validation notes.

## Dataset boundaries

- [`data/v2/`](data/v2/) standardizes non-Quran and non-hadith learning data.
- [`data/legacy/`](data/legacy/) preserves older file shapes and known issues unchanged.
- [`data/holy-quran/`](data/holy-quran/) is an independent Quran dataset and is neither legacy nor deprecated.
