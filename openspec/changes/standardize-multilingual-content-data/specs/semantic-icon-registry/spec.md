## Purpose

Defines provider-neutral semantic icon identifiers and optional reusable assets so content remains portable across web, mobile, native, and CDN consumers.

## ADDED Requirements

### Requirement: Provider-neutral semantic icon references
Content that declares an icon SHALL reference a controlled semantic `iconId` and SHALL NOT store a Font Awesome class, Material Symbols name, framework component, SVG markup, or vendor-specific presentation value as its primary icon contract.

#### Scenario: Prayer content declares an icon
- **WHEN** prayer content needs a visual category marker
- **THEN** it references a semantic identifier such as `worship.prayer` that remains stable if the visual provider changes

### Requirement: Discoverable icon registry
The dataset SHALL publish an icon registry containing each semantic identifier, bilingual accessible label, fallback identifier when applicable, optional provider mappings, and optional asset metadata.

#### Scenario: Application resolves a known icon
- **WHEN** an application loads a content item's `iconId`
- **THEN** it can find that identifier and its metadata in the registry

#### Scenario: Content references an unknown icon
- **WHEN** validation encounters an `iconId` absent from the registry
- **THEN** validation fails with the content identifier and unknown icon identifier

### Requirement: Optional application provider mappings
A registry entry MAY map a semantic identifier to supported third-party provider names, but consumers SHALL remain free to ignore those mappings and use local components or assets.

#### Scenario: Application uses Material Symbols
- **WHEN** a registry entry provides a Material Symbols mapping and the application supports it
- **THEN** the application can render the mapped icon without downloading a repository SVG

#### Scenario: Application uses its own design system
- **WHEN** the application has a local mapping for the semantic identifier
- **THEN** it can ignore registry provider mappings without changing content data

### Requirement: Optional versioned SVG assets
A registry entry MAY provide a relative path to a default SVG asset. When a manifest provides a version-pinned asset base URL, consumers SHALL be able to resolve that relative path into a stable CDN URL.

#### Scenario: Consumer loads a default SVG
- **WHEN** an icon entry has an SVG path and the manifest has a versioned asset base URL
- **THEN** the consumer can resolve and fetch the SVG without using a mutable branch URL

#### Scenario: Registry entry has no SVG
- **WHEN** an icon entry provides only semantic and provider metadata
- **THEN** it remains valid and consumers can use a provider mapping, local mapping, or fallback

### Requirement: SVG portability and safety
Repository-provided SVG icons SHALL use a consistent view box and visual style, SHALL avoid embedded scripts, external resource references, text dependent on fonts, and presentation-library classes, and SHALL be suitable for remote image delivery. Monochrome assets SHALL support consumer-controlled coloring where the rendering mode permits it.

#### Scenario: Unsafe SVG is added
- **WHEN** asset validation detects script, an external resource reference, or another prohibited construct
- **THEN** validation fails and identifies the asset and prohibited construct

### Requirement: Asset provenance and licensing
Every repository-provided or third-party-mapped icon SHALL record its provider or origin and applicable license metadata. Third-party assets SHALL NOT be included unless their license permits repository distribution and CDN delivery.

#### Scenario: Font Awesome Free SVG is included
- **WHEN** an SVG derived from Font Awesome Free is added
- **THEN** its registry or centralized license metadata records the original icon name, provider, license, and required attribution

#### Scenario: Unlicensed asset is added
- **WHEN** an asset lacks required provenance or distributable licensing metadata
- **THEN** validation fails before publication

### Requirement: Resilient fallback behavior
Icon registry entries SHALL support a semantic fallback chain that terminates at a valid generic icon or no-icon outcome without cycles.

#### Scenario: Remote SVG cannot be loaded
- **WHEN** an application cannot fetch the preferred SVG
- **THEN** registry metadata enables it to use a local provider mapping, fallback icon, or accessible no-icon presentation

#### Scenario: Fallback cycle is introduced
- **WHEN** validation encounters circular icon fallback references
- **THEN** validation fails and reports the cycle
