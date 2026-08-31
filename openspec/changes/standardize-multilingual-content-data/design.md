## Context

The repository is a static JSON dataset consumed directly through public CDN URLs. Its non-Quran/non-hadith content currently has several incompatible shapes: raw arrays and standalone objects; `arab`, `arabic`, and misspelled `arrabic`; `indo` and `id` used inconsistently as locales or identifiers; HTML embedded in `extras`; free-form citations; UI-library icon classes; and one malformed empty JSON file. There is no package manifest, schema set, or validation command.

Existing URLs may already be consumed externally and cannot be assumed safe to change. The dataset contains religious guidance where syntactic validity and structured source traceability are distinct concerns. See `proposal.md` for motivation and scope.

## Goals / Non-Goals

**Goals:**

- Establish one authoring and consumption contract for new non-Quran/non-hadith content.
- Preserve stable legacy CDN URLs while allowing a clean v2 model.
- Support Indonesian and English without tying identity or structure to either language.
- Make learning order, cross-content links, sources, and icons machine-readable.
- Keep output usable as static files through GitHub-backed CDNs and native application caches.
- Make invalid syntax, schema drift, unresolved references, and unsafe assets detectable before publication.

**Non-Goals:**

- Changing, normalizing, or repackaging files under `holy-quran` or any hadith-library dataset.
- Storing user progress, location, reminder preferences, bookmarks, or reading history.
- Defining application routing, UI components, calculation algorithms, or a backend API.

- Bundling every Font Awesome or Material Symbols asset.

## Decisions

### 1. Add a parallel versioned v2 tree instead of changing legacy documents

New standardized data will live beneath `v2/`, with a root manifest, schemas, collection indexes, content documents, and optional assets. Existing paths remain untouched during migration. Releases are intended to be consumed through Git tags such as `@v2.0.0`, not mutable `main` URLs.

This avoids an unannounced breaking change for CDN consumers. In-place conversion was rejected because the repository has no way to discover or coordinate all downstream users. A query-parameter API was rejected because the repository is static.

Proposed layout:

```text
v2/
├── manifest.json
├── stages.json
├── indexes/
├── content/
│   ├── lessons/
│   ├── practices/
│   ├── supplications/
│   ├── sequences/
│   └── glossary/
├── registries/
│   ├── sources.json
│   └── icons.json
├── schemas/
└── assets/
    └── icons/
```

### 2. Use localized field maps in canonical source documents

Localized fields use objects such as `{ "id": "...", "en": "..." }`. Indonesian and English remain adjacent to shared facts, identifiers, Arabic text, relationships, and references. This minimizes cross-locale drift and makes completeness validation straightforward for the initial two locales.

Fully separate locale trees were considered but rejected for canonical authoring because structural changes and stable references could drift independently. If payload size later matters, locale-specific bundles can be generated from the canonical documents without changing the source contract.

### 3. Use stable semantic identifiers and relative paths

Identifiers are lowercase ASCII namespace tokens such as `lesson.what-is-islam`, `stage.introduction`, and `worship.prayer`. They are distinct from URL slugs, titles, and sequence positions. Documents and indexes use relative repository paths; the manifest supplies discovery roots and an optional asset base URL.

Numeric-only IDs and localized text IDs were rejected because reordering or translation corrections would break references. Absolute URLs in every document were rejected because they prevent consumers from selecting a CDN, release tag, mirror, or local bundle.

### 4. Use typed documents with a constrained block vocabulary

Common metadata is shared, while JSON Schema branches validate lesson, practice, supplication, sequence, glossary, stage, index, and manifest-specific fields. Rich educational content uses a deliberately small block vocabulary. Blocks and nested list items receive IDs when they can be linked or independently reviewed.

Embedded HTML was rejected because it couples data to web rendering, complicates native consumption and localization, and introduces sanitization concerns. A completely free-form universal block model was rejected as unnecessary complexity; new block types require an explicit schema-version change.

### 5. Separate recitation, translation, transliteration, and audio

Arabic script uses the single `arabic` field. Meaning translations are localized. Transliteration is localized because Indonesian and English conventions can differ. Audio is represented as optional metadata and a URL or relative asset reference, never embedded binary data. Absence is expressed by omission or null according to schema, not an empty string.

This corrects current naming drift without implying that all educational content or ritual steps have a prescribed recitation.

### 6. Represent learning as a graph over an ordered stage catalog

The seven stages provide top-level order and entry points. Content remains in typed documents and refers to a stage plus explicit prerequisite, next, and related IDs. Quran ability paths and thematic hadith guidance are catalog metadata and educational content; they do not alter excluded datasets.

A deeply nested stage JSON tree was rejected because shared items would be duplicated and moving an item would rewrite large documents. A graph permits reusable content while indexes preserve efficient discovery.

Feature links use semantic tokens, for example `feature.prayer-schedule` or `feature.audio`, with optional parameters. Applications map supported tokens to routes or capabilities and ignore unsupported optional links.

### 8. Store bibliographic locators, not copies of excluded datasets

Sources use typed records for Quran references, hadith references, books, articles, and web resources. Quran and hadith references contain locators and bilingual display labels, but do not copy or mutate the source datasets. Reusable references may be centralized in a registry; item-local references remain acceptable where they are not shared.

Free-form citation strings may be retained as supplementary notes during migration but do not replace declared structured locators.

### 9. Make semantic icon IDs the contract and SVG an optional default

Content stores only a controlled `iconId`. The icon registry can contain accessible labels, semantic fallback, Font Awesome or Material Symbols mappings, and an optional relative SVG path. Applications can choose a provider mapping, a local component, the remote default SVG, or no icon.

Storing Font Awesome classes was rejected because it is web- and vendor-specific. Requiring SVG for every entry was rejected because applications may already bundle icon systems. Copying entire icon libraries was rejected due to repository size, unused assets, update cost, and licensing complexity.

When SVG is included, a version-pinned manifest base URL plus relative path resolves the CDN URL. Assets use a consistent view box/style and are checked for scripts, external references, and licensing metadata. Consumers displaying remote SVG should prefer image-safe rendering; inline rendering requires application-side sanitization.

### 10. Validate schema and cross-file integrity in two layers

JSON Schema validates document-local syntax, required fields, enums, patterns, and type-specific structures. A repository validation script handles dataset-wide properties JSON Schema cannot reliably enforce: unique IDs, file/index agreement, relationship resolution, stage membership, source/icon references, fallback cycles, excluded-path protection, and SVG safety/provenance.

The validator will target v2 plus explicit migration checks. Legacy data is inventoried but is not required to conform to v2 in place.

## Risks / Trade-offs

- [The v2 format temporarily duplicates legacy data] → Keep v2 as the canonical future format, document migration mapping, and defer legacy removal to a separately announced breaking release.
- [Inline bilingual fields increase payload size] → Use collection indexes and individual content files; add generated locale bundles later only if measured payload costs justify them.
- [Cross-file IDs can become difficult to manage manually] → Enforce namespace conventions, uniqueness, index agreement, and reference resolution in one validation command.
- [Religious content may be technically valid but incorrect] → Keep draft and reviewed states distinct, require provenance and reviewer attribution, and document that automated validation is not scholarly review.
- [English and Indonesian content may drift semantically] → Keep translations adjacent, record locale review independently, and block reviewed state until both are approved.
- [Remote icons can fail or change appearance] → Pin release URLs, provide fallback chains and provider mappings, and recommend local caching or mappings for critical navigation.
- [Third-party icon licensing can be violated] → Include only a curated subset with explicit provider, source name, version, license, and attribution; reject untracked assets.
- [Structured blocks require renderer work in consumers] → Keep the initial vocabulary constrained and versioned, publish examples, and avoid silent introduction of unknown block types.
- [The complete seven-stage curriculum is large] → Deliver schema and representative reviewed content first, then fill stages in tracked batches without weakening completeness rules for reviewed items.

## Migration Plan

1. Inventory and freeze the existing non-Quran/non-hadith public paths as legacy compatibility fixtures.
2. Add the v2 directory skeleton, manifest contract, JSON Schemas, identifier conventions, and validator.
3. Add stage, source, feature, and icon registries plus collection indexes and representative fixture documents for every supported type.
4. Migrate existing Asmaul Husna, dua, dhikr, Shahada, prayer, fasting, zakat, and Hajj data into v2, assigning stable IDs and retaining uncertain material as draft or under-review.
5. Replace embedded HTML with structured blocks and convert free-form citations into structured references where adequate locators can be verified.
6. Add and review missing bilingual learning content in stage order, with adaptive Quran journey metadata and thematic hadith references kept separate from excluded datasets.
7. Add a curated SVG subset only where semantic IDs cannot be served adequately by consumer mappings; record licenses and verify CDN-safe assets.
8. Validate the complete v2 graph, publish documentation and version-pinned CDN examples, then create a tagged v2 release.

Rollback consists of removing or reverting the new v2 release before consumers adopt it; legacy URLs remain unaffected. After a tag is published, corrections use a new version rather than mutating the tagged release.

## Open Questions

- The specific people or governance process authorized to set scholarly content review to complete can be established before items are promoted from `under-review`; it does not alter the data contract.
- The first curated SVG visual style and provider mix can be selected during asset curation because SVG remains optional and semantic icon IDs are already the stable contract.
