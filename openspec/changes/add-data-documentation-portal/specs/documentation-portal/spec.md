## Purpose

Defines an accessible bilingual documentation portal that combines developer reference material with interactive Vue-based dataset experiences.

## ADDED Requirements

### Requirement: Documentation information architecture

The portal SHALL provide discoverable overview, guide, reference, Demo UI, explorer, API, migration, and contributing sections covering manifests, collections, content types, localization, blocks, relationships, sources, semantic icons, validation, CDN usage, and dataset boundaries.

#### Scenario: New developer enters portal

- **WHEN** a user opens the portal home page
- **THEN** the user can navigate to getting started, the click-through Demo UI, data exploration, API access, schema reference, and contribution guidance

### Requirement: Obsidian Emerald design system

The portal SHALL use semantic design tokens with black, gray, and white foundations, restrained emerald accents, minimal borders/shadows, readable code styling, appropriate Arabic typography, and accessible semantic presentation colors.

#### Scenario: Portal presents semantic interface tokens

- **WHEN** a user opens the portal in light or dark mode
- **THEN** the canvas, surfaces, text, links, focus indicator, and component states use the corresponding semantic tokens

### Requirement: Theme and locale controls

The portal SHALL support light, dark, and system themes plus Indonesian and English presentation, preserve user preferences locally, and provide default-locale fallback when a selected translation is unavailable.

#### Scenario: User selects dark English mode

- **WHEN** the user selects dark theme and English
- **THEN** subsequent navigation retains both preferences and rendered localized fields use English with documented fallback behavior

### Requirement: Responsive accessible navigation

The portal SHALL provide keyboard-accessible header, search, left navigation, on-page navigation, mobile drawer behavior, skip-to-content, focus indicators, and reduced-motion support meeting WCAG AA contrast expectations.

#### Scenario: Keyboard user opens mobile navigation

- **WHEN** the user operates the navigation without a pointer
- **THEN** focus is managed within the drawer and returns to the trigger after closure

### Requirement: Documentation search

The portal SHALL allow users to search documentation pages and discover relevant explorer/reference destinations without requiring a server-side search service.

#### Scenario: User searches for localization

- **WHEN** the user submits a localization-related query
- **THEN** matching guide and reference pages are presented with navigable results

### Requirement: Demo UI dataset navigation

The portal SHALL distinguish API documentation from a click-through Demo UI and SHALL provide separate navigable entry points for current v2 learning content, legacy compatibility data, and the independent Holy Quran dataset.

#### Scenario: User chooses a dataset demo

- **WHEN** a user opens the Demo UI section
- **THEN** the user can select v2 Learning, Legacy Browser, or Holy Quran Browser and can see the selected dataset's status and scope
