## Purpose

Defines interactive views that turn current v2, legacy compatibility, and independent Quran JSON into understandable click-through experiences.

## ADDED Requirements

### Requirement: Dataset dashboard

The portal SHALL derive and display dataset version, locales, collection counts, content totals, stage totals, and publication-state summaries from the bundled manifest and indexes rather than hardcoded metrics.

#### Scenario: Dataset content count changes

- **WHEN** a document is added and indexes are rebuilt
- **THEN** the next portal build displays the updated count without editing a page component

### Requirement: Seven-stage journey visualization

The portal SHALL display all seven ordered stages, goals, entry content, content membership, adaptive Quran paths, and navigable progression in a responsive timeline suitable for desktop and mobile.

#### Scenario: User selects a journey stage

- **WHEN** the user activates a stage
- **THEN** the portal displays its localized goal and ordered content with links to item details

### Requirement: Collection explorer

The portal SHALL let users search and filter indexed items by collection type, stage, publication status, group, season, and locale-aware text, with usable empty, loading, and error states.

#### Scenario: User filters reviewed practices

- **WHEN** collection type is practice and status is reviewed
- **THEN** only matching indexed items are displayed and the active filters remain visible

### Requirement: Typed content rendering

The portal SHALL render every supported v2 content type and structured block, including Arabic recitation with RTL direction, transliteration, translations, steps, checklists, source references, audio references, feature links, relationships, and completion prompts.

#### Scenario: User views a recitation block

- **WHEN** a valid recitation block is loaded
- **THEN** Arabic, locale-appropriate transliteration and translation, optional audio, and sources are presented accessibly

### Requirement: Raw JSON and metadata views

Every collection, registry, stage catalog, and content item SHALL provide syntax-highlighted raw JSON with copy, download, and source-path context alongside its visual preview.

#### Scenario: Developer inspects raw lesson

- **WHEN** the developer opens the Raw JSON tab
- **THEN** the exact loaded document is shown and can be copied or downloaded

### Requirement: Legacy compatibility browser

The portal SHALL provide a Legacy Browser for Asmaul Husna, dhikr, dua, and pillars-of-Islam collections without normalizing or mutating their original file formats. It SHALL identify each collection as legacy, display known issues, and expose its exact JSON/API path.

#### Scenario: User opens malformed legacy resource

- **WHEN** a user selects a malformed or empty legacy JSON resource
- **THEN** the browser presents an explicit compatibility warning, the raw endpoint actions, and an actionable parse-error state rather than concealing or altering the source

### Requirement: Independent Holy Quran browser

The portal SHALL provide a Holy Quran Browser that lets users navigate available juz, all available surah, and the selected surah's ayah data while clearly identifying the dataset as independent rather than legacy.

#### Scenario: User reads a selected surah

- **WHEN** a user selects a surah from the Quran Browser
- **THEN** the browser loads and presents its metadata and ayah data with Arabic rendered RTL and exposes the exact JSON/API path

### Requirement: Demo UI inspection bridge

Every Demo UI dataset view SHALL expose an action that opens its source JSON in the portal API inspector or a raw endpoint action, preserving the selected dataset path.

#### Scenario: User inspects rendered Quran data

- **WHEN** a user activates the data inspection action on a Quran view
- **THEN** the API inspector receives the exact selected Quran resource path and displays its provider-aware actions

### Requirement: Semantic icon rendering

The portal SHALL resolve an item's semantic icon through local mapping, optional bundled SVG, provider mapping, or fallback chain, and SHALL preserve accessible labels if no visual icon can be rendered.

#### Scenario: Preferred icon asset is unavailable

- **WHEN** an SVG fails to load
- **THEN** the portal uses a valid fallback or text-only accessible presentation without hiding the content
