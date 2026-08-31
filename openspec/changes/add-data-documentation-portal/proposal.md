## Why

The repository now contains a structured multilingual v2 dataset, but users still need to understand file paths manually, inspect raw JSON, and construct CDN URLs themselves. A public documentation portal and clearer repository layout will make the data discoverable, visually understandable, directly consumable through free CDN endpoints, and automatically published from the same validated commit.

## What Changes

- **BREAKING** Reorganize public data under `data/`: inconsistent superseded collections under `data/legacy/`, the standardized dataset under `data/v2/`, and the independent Quran dataset under `data/holy-quran/`. Quran content remains unchanged and is not labeled legacy.
- **BREAKING** Replace unversioned root data paths as the primary contract with a root manifest and documented version-pinned release URLs; preserve the previous layout through a tagged compatibility snapshot and publish an old-to-new URL migration guide.
- Add a `docs/` portal built with VitePress, Vue 3, TypeScript, and Tailwind CSS, combining prose documentation with interactive data components.
- Apply an accessible GitHub Primer-inspired “Obsidian Emerald” design system using black, gray, and white foundations, restrained emerald accents, light/dark/system themes, semantic color tokens, responsive navigation, and appropriate Arabic typography.
- Visualize dataset statistics, the seven-stage learning journey, collection contents, publication states, relationships, recitations, sources, semantic icons, and raw JSON.
- Add a distinct click-through Demo UI alongside API documentation: a v2 learning experience, a compatibility-aware legacy browser, and an independent Holy Quran browser for juz, surah, and ayah data.
- Document manifests, indexes, content types, localization, blocks, review states, sources, icons, validation, legacy compatibility, Quran dataset boundaries, contribution workflow, and CDN usage.
- Add API/CDN shortcuts to collections and content items, including provider/version selection, URL copy, raw response in a new tab, in-portal JSON preview, download, and copyable JavaScript, TypeScript, cURL, and PowerShell snippets.
- Support jsDelivr as the recommended provider, Statically as an alternative, GitHub Raw for debugging, and GitHub Pages for commit-matched portal data; distinguish stable release tags from mutable `main` URLs.
- Bundle the validated `data/v2/` subset into the static documentation build so the deployed portal visualizes data from the same commit without requiring a CDN release.
- Add GitHub Actions checks for dataset validation, tests, TypeScript, and VitePress build on pull requests and pushes, with automatic GitHub Pages deployment only from `main`.

## Capabilities

### New Capabilities

- `repository-data-layout`: User-friendly public data organization, root discovery manifest, compatibility snapshot expectations, and old-to-new path migration behavior.
- `documentation-portal`: Responsive bilingual documentation experience, Obsidian Emerald design system, navigation, search, theme handling, and technical/reference/contribution documentation.
- `dataset-visualization`: Dashboard, seven-stage journey, collection explorer, typed content renderer, relationships, source/icon presentation, filters, and raw JSON views.
- `cdn-api-explorer`: Provider-aware stable/latest endpoint generation, API shortcuts, response preview, raw opening, URL/download actions, and copyable usage snippets.
- `pages-deployment`: Reproducible data preparation, quality gates, static portal build, artifact publication, and secure automatic GitHub Pages deployment.

### Modified Capabilities

None.

## Impact

- Moves current root data directories and `v2/` into a new public `data/` hierarchy, requiring manifest paths, validators, index builders, checksum baselines, README examples, and consumer URLs to be updated.
- Requires a compatibility release/tag and migration documentation before old unpinned URLs are removed; creating or pushing Git commits/tags remains an explicit release action rather than an implicit implementation step.
- Adds a Node-based documentation toolchain and lockfile alongside the existing Python validation toolchain.
- Adds Vue/VitePress source, Tailwind styling, generated static data preparation, client-side loading/search/rendering, and a GitHub Pages workflow.
- Public GitHub Pages output will expose documentation, schemas, registries, indexes, content JSON, and selected SVG assets. It will exclude fixtures and migration checksums while including the legacy and Quran files required by their lazy-loaded Demo UI browsers.
- The portal treats draft and under-review content visibly and does not imply scholarly approval from successful technical validation.
- Depends on the standardized v2 artifacts produced by `standardize-multilingual-content-data`; unresolved release-tag verification in that change can be completed as part of the explicit release process.
