## Purpose

Defines structured source references and deprecation traceability for consumers of Islamic JSON content.

## ADDED Requirements

### Requirement: Structured source references

Content SHALL represent sources as structured entries with a stable source identifier, source type, localized citation label, and type-appropriate locator fields. Supported source types SHALL include Quran reference, hadith reference, book, article, and web resource.

#### Scenario: Content cites a Quran verse

- **WHEN** an item cites a Quran verse
- **THEN** the source records surah and ayah locators plus bilingual citation labels without copying the verse into the source record

#### Scenario: Content cites a hadith

- **WHEN** an item cites a hadith
- **THEN** the source identifies the collection and available hadith number or locator without modifying a hadith-library dataset

### Requirement: Source claims remain structured

When a content item declares a source reference, it SHALL use the structured source registry identifier and machine-readable locator where the source type requires one. Human-readable notes MAY supplement but SHALL NOT replace machine-readable locators.

#### Scenario: Content cites a registered source

- **WHEN** a content item declares a source reference
- **THEN** the reference resolves to a structured source record and uses its supported locator fields

### Requirement: Deprecation preserves traceability

Deprecated items SHALL retain their stable identifier and SHALL declare a bilingual reason plus an optional replacement identifier when replacement content exists.

#### Scenario: Incorrect item is superseded

- **WHEN** an item is deprecated in favor of corrected content
- **THEN** consumers can identify the deprecation reason and navigate to the replacement without references silently changing target
