## Why

The repository's non-Quran and non-hadith datasets currently use inconsistent root shapes, field names, locale conventions, rich-text representations, identifiers, and source metadata. A versioned standard is needed so applications can consume bilingual Islamic learning content reliably, connect it into a guided seven-stage journey, and verify its technical and editorial readiness without breaking existing CDN consumers.

## What Changes

- Introduce a versioned v2 data contract for non-Quran and non-hadith content with stable semantic identifiers, consistent document envelopes, typed content, BCP 47 locale keys, and required Indonesian and English localized fields.
- Define structured content blocks and typed models for lessons, practices, supplications, sequences, glossary entries, stages, and indexes instead of embedding presentation-specific HTML.
- Publish a manifest and indexes that let CDN consumers discover the dataset version, supported locales, collections, content paths, and optional asset base URL.
- Model the seven learning stages and cross-content relationships through stable IDs, including prerequisites, next content, related content, feature links, and completion prompts; user progress remains application-owned.
- Add structured bibliographic references so applications can present and trace declared source locators without adding an editorial-review workflow.
- Introduce a provider-neutral semantic icon registry. Content references `iconId`; the registry may expose versioned SVG asset URLs and provider mappings while allowing applications to supply local icons and fallbacks.
- Add machine-readable schemas and automated validation for JSON syntax, identifiers, locales, references, registry entries, and required fields.
- Migrate existing Asmaul Husna, dua, dhikr, and pillars-of-Islam data into v2 while retaining legacy files and URLs during the compatibility period.
- Add the missing non-Quran/non-hadith learning content incrementally across the seven stages, with Indonesian and English required by the v2 contract.
- Explicitly exclude modifications to the `holy-quran` dataset and any hadith-library dataset. Other content may contain structured bibliographic references to Quran verses or hadith records without copying or changing those datasets.

## Capabilities

### New Capabilities

- `multilingual-content-schema`: Versioned, typed, bilingual JSON documents, manifests, indexes, structured blocks, stable identifiers, relationships, and validation rules for non-Quran/non-hadith content.
- `learning-journey-catalog`: Seven ordered learning stages and discoverable lesson/practice journeys with prerequisites, transitions, feature links, and completion prompts.
- `content-provenance-review`: Structured source references and deprecation traceability.
- `semantic-icon-registry`: Provider-neutral semantic icon identifiers, optional versioned SVG assets, application provider mappings, fallbacks, licensing metadata, and CDN resolution.

### Modified Capabilities

None.

## Impact

- Adds versioned dataset paths, schemas, indexes, manifests, optional icon assets, validation tooling, and documentation.
- Existing non-Quran/non-hadith files become migration inputs but remain available at their current paths; v2 consumers use the new contract and versioned CDN URLs.
- Consumer applications gain a stable discovery and relationship model but must implement locale selection, content block rendering, icon resolution, and fallback behavior to adopt v2.
- Content contributors must supply stable IDs, Indonesian and English text, and structured references that pass validation.
- SVG assets, when included, require explicit provenance and license metadata and must be suitable for remote CDN delivery.
- No data or API shape under `holy-quran` or a hadith-library dataset is changed.
