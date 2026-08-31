## Purpose

Defines a discoverable public repository layout and compatibility contract for current, legacy, and independent Islamic JSON datasets.

## ADDED Requirements

### Requirement: User-friendly data hierarchy
The repository SHALL organize public datasets under `data/legacy/`, `data/v2/`, and `data/holy-quran/`, where legacy contains superseded inconsistent formats, v2 contains the current standardized contract, and the Quran remains an independent dataset that is not labeled deprecated.

#### Scenario: User browses repository data
- **WHEN** a user opens the `data/` directory
- **THEN** the directory names and accompanying documentation clearly distinguish legacy, current v2, and Quran datasets

### Requirement: Root dataset discovery
The repository SHALL publish a root manifest that identifies the latest standardized dataset manifest, documentation portal, dataset statuses, and public paths without requiring users to infer them from folders.

#### Scenario: Consumer starts at root manifest
- **WHEN** a consumer loads the root manifest
- **THEN** it can discover the current v2 entry point, legacy metadata, Quran dataset, and documentation location

### Requirement: Internal references follow relocated paths
All manifests, index paths, asset references, validators, generators, checksum baselines, documentation examples, and build tooling SHALL resolve successfully after the data hierarchy is relocated.

#### Scenario: Relocated v2 dataset is validated
- **WHEN** the repository validator runs after relocation
- **THEN** every document, index, registry, schema, relationship, and asset reference resolves under `data/v2/`

### Requirement: Legacy path migration guide
The repository SHALL document each previously public root data path and its new location, identify known legacy issues, and recommend version-pinned v2 endpoints for new integrations.

#### Scenario: Existing consumer finds replacement URL
- **WHEN** a consumer looks up an old root path in the migration guide
- **THEN** it receives the tagged compatibility URL and the appropriate new path or v2 alternative

### Requirement: Tagged compatibility boundary
Before the breaking root-path removal is treated as released, the previous layout SHALL be preservable through a documented immutable tag. Implementation SHALL NOT silently create or push a Git tag without explicit release authorization.

#### Scenario: Consumer needs the previous layout
- **WHEN** the breaking layout is released with an authorized compatibility tag
- **THEN** the consumer can continue using the previous path through a version-pinned URL

#### Scenario: Implementation runs without release authorization
- **WHEN** repository restructuring is implemented but no explicit permission to commit or tag was given
- **THEN** code and migration documentation are prepared while tag creation remains an explicit release step
