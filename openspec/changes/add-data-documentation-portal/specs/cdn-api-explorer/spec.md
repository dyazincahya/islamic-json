## Purpose

Defines direct, provider-aware access to static JSON API endpoints so developers can preview, copy, open, and integrate dataset URLs without constructing paths manually.

## ADDED Requirements

### Requirement: Provider-aware endpoint generation
The portal SHALL build endpoints from repository configuration and manifest/index paths for jsDelivr, Statically, GitHub Raw, and GitHub Pages. jsDelivr SHALL be recommended for production, while GitHub Raw SHALL be identified as a debugging fallback rather than the primary CDN.

#### Scenario: User selects jsDelivr
- **WHEN** a user selects a content item and jsDelivr
- **THEN** the generated URL uses the configured owner, repository, version, relocated data root, and exact indexed item path

### Requirement: Stable and latest version modes
The portal SHALL offer a configured stable release tag and mutable `main` mode, default production examples to the stable tag, and display a warning when `main` is selected.

#### Scenario: User selects main
- **WHEN** the user changes version mode to `main`
- **THEN** the URL is regenerated and a visible warning explains that the endpoint can change without notice

### Requirement: API shortcuts throughout portal
Collection cards, content cards, detail pages, registry references, schemas, manifest, and stages SHALL expose appropriate API actions without requiring navigation to a separate playground.

#### Scenario: User opens content API menu
- **WHEN** the user opens API actions for a lesson
- **THEN** copy URL, open raw, preview response, download, and snippet actions are available

### Requirement: Clipboard and raw navigation
The portal SHALL copy generated URLs with accessible success/failure feedback and SHALL open external raw endpoints in a new tab using safe opener isolation.

#### Scenario: URL copy succeeds
- **WHEN** the Clipboard API accepts the endpoint
- **THEN** an `aria-live` confirmation identifies that the URL was copied

#### Scenario: Clipboard API is unavailable
- **WHEN** programmatic copy fails
- **THEN** the URL remains selectable for manual copying and the failure is explained

### Requirement: Response preview and fallback guidance
The API explorer SHALL fetch selected endpoints when cross-origin access permits, display loading, HTTP status, content type, parsed JSON, network/parse errors, and an explicit option to try another provider without silently switching.

#### Scenario: CDN returns 404
- **WHEN** preview receives HTTP 404
- **THEN** the portal displays the failing provider/status and offers explicit alternative-provider actions

### Requirement: Copyable integration snippets
The portal SHALL generate copyable JavaScript, TypeScript, cURL, and PowerShell examples from the currently selected provider, version, and endpoint.

#### Scenario: Provider selection changes
- **WHEN** a user switches from jsDelivr to Statically
- **THEN** every displayed snippet updates to the Statically endpoint

### Requirement: API playground
The portal SHALL provide a dedicated playground where users can choose provider, version, common endpoint or indexed content, send a request, inspect the response, copy the URL, and open the raw resource.

#### Scenario: User previews lessons index
- **WHEN** the user selects the lessons index and sends the request
- **THEN** the response metadata and JSON index are displayed in the portal
