## Purpose

Defines structured provenance and editorial states so consumers and contributors can distinguish valid JSON from translated, sourced, and scholarly reviewed Islamic content.

## ADDED Requirements

### Requirement: Structured source references
Content SHALL represent sources as structured entries with a stable source identifier, source type, localized citation label, and type-appropriate locator fields. Supported source types SHALL include Quran reference, hadith reference, book, article, and web resource.

#### Scenario: Content cites a Quran verse
- **WHEN** an item cites a Quran verse
- **THEN** the source records surah and ayah locators plus bilingual citation labels without copying the verse into the source record

#### Scenario: Content cites a hadith
- **WHEN** an item cites a hadith
- **THEN** the source identifies the collection and available hadith number or locator without modifying a hadith-library dataset

### Requirement: Explicit publication state
Every content item SHALL declare one of the controlled publication states `draft`, `translated`, `under-review`, `reviewed`, or `deprecated`.

#### Scenario: New content is incomplete
- **WHEN** a contributor adds content that has not completed translation and review
- **THEN** the item is represented with a non-reviewed publication state and remains distinguishable from reviewed content

#### Scenario: Consumer requests reviewed material
- **WHEN** a consumer filters a collection index to reviewed status
- **THEN** only items declared reviewed are returned by that filtering operation

### Requirement: Separate review dimensions
Review metadata SHALL separately represent content review, Indonesian translation review, English translation review, reviewer attribution, review date, and optional review notes.

#### Scenario: English translation remains unreviewed
- **WHEN** subject matter has been reviewed but the English translation has not
- **THEN** the metadata records those outcomes independently and the item cannot satisfy reviewed publication readiness

### Requirement: Reviewed publication readiness
An item SHALL NOT validate as `reviewed` unless all required Indonesian and English content is present, required source references are structurally valid, content review is complete, both locale reviews are complete, and required reviewer metadata is supplied.

#### Scenario: Reviewed item lacks reviewer attribution
- **WHEN** an item declares reviewed status without the required reviewer information
- **THEN** validation fails with the item identifier and missing review field

#### Scenario: Draft item has incomplete review metadata
- **WHEN** a draft item omits completed review outcomes
- **THEN** it may remain valid as draft provided the omission is permitted by the draft schema

### Requirement: Source claims remain auditable
Free-form source descriptions SHALL NOT substitute for structured references in reviewed v2 content. Human-readable notes MAY supplement, but SHALL NOT replace, machine-readable locators.

#### Scenario: Reviewed item uses only a free-form citation
- **WHEN** validation finds a reviewed item whose required evidence is represented only by an unstructured string
- **THEN** validation fails and identifies the unsupported citation field

### Requirement: Deprecation preserves traceability
Deprecated items SHALL retain their stable identifier and SHALL declare a bilingual reason plus an optional replacement identifier when replacement content exists.

#### Scenario: Incorrect item is superseded
- **WHEN** an item is deprecated in favor of corrected content
- **THEN** consumers can identify the deprecation reason and navigate to the replacement without references silently changing target
