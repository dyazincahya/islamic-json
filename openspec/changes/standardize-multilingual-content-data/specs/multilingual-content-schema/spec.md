## Purpose

Defines a stable, versioned, bilingual data contract through which downstream applications can discover and consume non-Quran and non-hadith Islamic content consistently.

## ADDED Requirements

### Requirement: Versioned dataset discovery

The dataset SHALL publish a v2 manifest that declares the schema version, dataset version, default locale, supported locales, collection identifiers, and version-relative collection paths.

#### Scenario: Consumer discovers v2 collections

- **WHEN** a consumer loads the v2 manifest
- **THEN** it receives enough versioned metadata and relative paths to discover every published v2 collection without inferring the repository directory structure

#### Scenario: Dataset version changes

- **WHEN** published v2 content changes in a release
- **THEN** the manifest identifies the release with a dataset version suitable for a version-pinned CDN URL

### Requirement: Stable content identity

Every v2 stage, content item, block, list item, source, and registry entry that can be referenced SHALL have a stable, unique, lowercase ASCII semantic identifier independent of localized display text and array position.

#### Scenario: Localized title changes

- **WHEN** an Indonesian or English title is corrected
- **THEN** the entity identifier and references to that entity remain unchanged

#### Scenario: Duplicate identifier is introduced

- **WHEN** validation encounters the same identifier more than once in a namespace that requires uniqueness
- **THEN** validation fails and identifies every conflicting location

### Requirement: Required bilingual localization

Localized user-facing fields SHALL use BCP 47 locale keys and SHALL contain non-empty Indonesian (`id`) and English (`en`) values.

#### Scenario: Content is bilingual

- **WHEN** a content item is validated
- **THEN** every required localized field contains Indonesian under `id` and English under `en`

#### Scenario: Required translation is missing

- **WHEN** an item omits or empties a required `id` or `en` localized value
- **THEN** validation fails with the item identifier, field path, and missing locale

### Requirement: Typed content documents

The v2 contract SHALL distinguish at least lesson, practice, supplication, sequence, glossary entry, stage, collection index, and manifest document types while sharing common version, identity, localization, relationship, and source conventions.

#### Scenario: Consumer reads a typed item

- **WHEN** a consumer loads a valid content document
- **THEN** its declared type determines which fields and content structures are valid without relying on its file name

### Requirement: Structured presentation-neutral content

Educational prose and instructional content SHALL be represented by validated structured blocks rather than presentation-library classes or embedded HTML. The initial block vocabulary SHALL support headings, paragraphs, ordered lists, unordered lists, quotations, callouts, recitations, steps, checklists, images, audio references, and source references.

#### Scenario: Application renders a lesson

- **WHEN** an application loads a valid lesson
- **THEN** it can select a locale and render each block without parsing embedded HTML

#### Scenario: Unsupported block type is added

- **WHEN** a document declares a block type not recognized by its schema version
- **THEN** validation fails with the document identifier and block location

### Requirement: Standardized recitation data

Arabic recitations SHALL use the `arabic` field name and SHALL represent translation and locale-sensitive transliteration separately. Empty recitation values SHALL be omitted or explicitly null rather than represented as empty strings.

#### Scenario: Supplication has an Arabic recitation

- **WHEN** a supplication includes recited Arabic text
- **THEN** it exposes the Arabic script, Indonesian and English translations, and any provided transliterations through their standardized fields

#### Scenario: Sequence step has no prescribed recitation

- **WHEN** a practice step has no recitation
- **THEN** the item remains valid without inventing or supplying an empty Arabic string

### Requirement: Discoverable collections and relationships

Every published content collection SHALL provide an index containing item identifiers, types, slugs, and relative document paths. All declared cross-document relationships SHALL resolve to known identifiers of compatible types.

#### Scenario: Consumer lists a collection

- **WHEN** a consumer loads a collection index
- **THEN** it can discover available items and their relative paths without downloading all content documents

#### Scenario: Relationship target is missing

- **WHEN** validation encounters a prerequisite, next, related, stage, recitation, or other reference to an unknown identifier
- **THEN** validation fails and identifies the source item and unresolved target

### Requirement: Machine-readable validation

The repository SHALL provide machine-readable schemas and a repeatable validation command that verifies JSON syntax, schema conformance, locale completeness, identifier uniqueness, path resolution, relationship integrity, and registry references for v2 data.

#### Scenario: Valid dataset is checked

- **WHEN** the validation command runs against a conforming v2 dataset
- **THEN** it exits successfully and reports no errors

#### Scenario: Invalid JSON is checked

- **WHEN** the validation command encounters malformed or empty JSON in the validated v2 paths
- **THEN** it exits unsuccessfully and identifies the invalid file

### Requirement: Legacy compatibility and excluded datasets

Existing non-Quran/non-hadith paths SHALL remain available during v2 migration, and v2 work SHALL NOT alter files or public data shapes in `holy-quran` or any hadith-library dataset.

#### Scenario: Existing consumer continues using legacy URL

- **WHEN** v2 is introduced
- **THEN** a previously published legacy non-Quran/non-hadith URL remains available with its existing shape

#### Scenario: Quran or hadith is referenced by learning content

- **WHEN** v2 educational content cites a Quran verse or hadith
- **THEN** it stores only a structured bibliographic reference and does not modify or duplicate the excluded source dataset
