## Purpose

Defines the ordered seven-stage learning catalog and the relationships that turn standalone Islamic content into adaptable, discoverable learning journeys.

## ADDED Requirements

### Requirement: Seven ordered learning stages
The catalog SHALL expose exactly seven top-level stages in this order: introduction to Islam; Shahada and foundations of faith; purification and prayer; fasting, zakat, and Hajj; Quran learning; hadith, Sunnah, and character; and daily Muslim life. Every stage SHALL have a stable identifier, numeric order, bilingual title, bilingual goal, and entry-content reference.

#### Scenario: Consumer displays the complete journey
- **WHEN** a consumer loads the stage catalog
- **THEN** it can display all seven bilingual stages in the prescribed order and navigate to each stage's entry content

### Requirement: Stage content membership
Every journey lesson, practice, or sequence SHALL identify its owning stage, order or grouping within that stage, and publication status.

#### Scenario: Consumer lists a stage
- **WHEN** a consumer requests content belonging to a stage
- **THEN** it can order and group the stage's published content without inferring membership from file paths

### Requirement: Guided content relationships
Journey items SHALL support explicit prerequisite, next, and related-content relationships through stable identifiers, and all relationship targets SHALL resolve to cataloged items.

#### Scenario: User completes an introductory lesson
- **WHEN** an application processes the lesson's next-content relationships
- **THEN** it can offer the intended next lesson without hardcoded navigation rules

#### Scenario: Item declares a missing prerequisite
- **WHEN** catalog validation finds an unresolved prerequisite
- **THEN** validation fails with both the source identifier and unresolved identifier

### Requirement: Adaptive Quran learning paths
The Quran-learning stage SHALL expose separate entry paths for users who cannot yet read, can read and want tajwid practice, want to understand meaning, or want reading consistency. It SHALL reference Quran-related application features without changing or embedding the `holy-quran` dataset.

#### Scenario: Beginner selects reading ability
- **WHEN** an application selects the cannot-yet-read entry path
- **THEN** the catalog points to introductory Iqra, Arabic-letter, vowel, and letter-joining learning content rather than forcing the standard Quran reader flow

#### Scenario: Experienced reader enters Quran stage
- **WHEN** an application selects a reading, understanding, or consistency path
- **THEN** the catalog does not require that user to start with Iqra

### Requirement: Thematic hadith guidance without library modification
The hadith, Sunnah, and character stage SHALL support thematic guidance items that contain explanation, life examples, and actionable practice while referring bibliographically to hadith sources without modifying or duplicating a hadith-library dataset.

#### Scenario: Consumer presents a thematic hadith lesson
- **WHEN** a thematic guidance item is loaded
- **THEN** the consumer can present its theme, source reference, explanation, life example, and suggested action independently of hadith-book browsing

### Requirement: Application feature links
Journey content SHALL support provider-neutral feature links for relevant application functions such as prayer schedules, location, audio, reminders, calculators, reading pages, bookmarks, and continuation history.

#### Scenario: Prayer lesson links to a schedule
- **WHEN** a prayer lesson declares a prayer-schedule feature link
- **THEN** an application can map that semantic feature identifier to its own route or capability

#### Scenario: Consumer does not implement a feature
- **WHEN** an application does not recognize an optional feature identifier
- **THEN** the educational content remains usable without that integration

### Requirement: Completion prompts without user state
Journey items SHALL support bilingual acknowledgement or practice-checklist completion prompts, but the dataset SHALL NOT store individual user progress, reminder preferences, location, or history.

#### Scenario: Practice has completion criteria
- **WHEN** an application loads a practice item
- **THEN** it can render the supplied completion prompt and persist the result in application-owned storage

### Requirement: Seasonal discovery metadata
Relevant fasting, zakat, Hajj, and daily-life journeys SHALL support semantic seasonal tags so applications can promote them at an appropriate time without changing the canonical learning order.

#### Scenario: Ramadan approaches
- **WHEN** an application filters the catalog by the Ramadan season tag
- **THEN** it can discover applicable fasting, Ramadan, and zakat-fitrah content
