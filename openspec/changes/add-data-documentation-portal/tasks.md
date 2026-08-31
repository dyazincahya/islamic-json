## 1. Restructuring Baseline

- [x] 1.1 Record current public paths and checksums and generate an explicit old-to-new migration map before moving files.
- [x] 1.2 Document the command sequence for creating the immutable pre-move compatibility tag without creating or pushing it automatically.
- [x] 1.3 Create `data/legacy/`, `data/v2/`, and `data/holy-quran/` with explanatory dataset README files.
- [x] 1.4 Move Asmaul Husna, dhikr, dua, and pillars-of-Islam directories into `data/legacy/` without changing file bytes.
- [x] 1.5 Move `v2/` to `data/v2/` without changing content documents.
- [x] 1.6 Move `holy-quran/` to `data/holy-quran/` without changing Quran file bytes or labeling the dataset deprecated.

## 2. Manifests, Tooling, and Compatibility

- [x] 2.1 Add a root discovery manifest for current v2, legacy, Quran, and documentation entry points.
- [x] 2.2 Add a legacy manifest listing collections, paths, known issues, deprecation status, and v2 alternatives where available.
- [x] 2.3 Update the v2 manifest, asset base URL, public paths, and version metadata for the `data/v2/` location.
- [x] 2.4 Update index generation, validation, tests, fixtures, and checksum tooling to use relocated paths.
- [x] 2.5 Regenerate compatibility baselines and verify every moved legacy/Quran file retains its pre-move checksum.
- [x] 2.6 Update root README CDN examples, repository map, breaking-change notice, and migration links.
- [x] 2.7 Add a complete migration guide mapping old root URLs to compatibility-tag and new-layout URLs.
- [x] 2.8 Run the full Python validator and unit test suite against the relocated structure and resolve all errors.

## 3. Documentation Portal Foundation

- [x] 3.1 Scaffold `docs/` with VitePress, Vue 3, TypeScript, Tailwind CSS, package scripts, and a committed npm lockfile.
- [x] 3.2 Add Git ignores for dependencies, generated portal data, VitePress cache, and build output.
- [x] 3.3 Configure the portal base path for `/islamic-json/`, local development, future custom-domain override, and local search.
- [x] 3.4 Create the overview, guide, reference, explorer, API, migration, and contributing page hierarchy and navigation.
- [ ] 3.5 Add bilingual documentation labels and locale selection with Indonesian default and English fallback.

## 4. Obsidian Emerald Design System

- [x] 4.1 Define light and dark semantic CSS tokens for canvas, surfaces, borders, text, emerald accent, links, statuses, focus, and code.
- [x] 4.2 Connect semantic tokens to Tailwind utilities without scattering raw color values through Vue templates.
- [ ] 4.3 Implement the custom VitePress theme, GitHub Primer-inspired header, left navigation, right table of contents, footer, and responsive mobile drawers.
- [ ] 4.4 Add light, dark, and system theme controls with persisted preference and no incorrect-theme flash.
- [ ] 4.5 Add locale controls, semantic status badges, callouts, cards, buttons, tabs, loading/error/empty states, and accessible feedback primitives.
- [ ] 4.6 Add system sans, monospace, and Arabic typography with RTL rendering, readable recitation sizing, and font fallbacks.
- [ ] 4.7 Verify keyboard navigation, focus management, skip links, reduced motion, touch targets, and WCAG AA color contrast in light and dark modes.

## 5. Portal Data Preparation and Access

- [x] 5.1 Add a deterministic preparation script that clears stale output and copies only public manifest, stages, indexes, content, registries, schemas, and selected SVGs from `data/v2/`.
- [x] 5.2 Revise portal preparation to include lazy-loadable legacy and Quran browser resources while excluding fixtures and migration checksums.
- [ ] 5.3 Add TypeScript models for root/v2 manifests, indexes, stages, registries, typed content, structured blocks, and publication states.
- [ ] 5.4 Implement a cached data service for bundled paths, locale fallback, collection loading, detail loading, registries, and actionable load/parse errors.
- [ ] 5.5 Add tests proving prepared portal data comes from the current checkout and that removed source files cannot remain stale in output.

## 6. Documentation Content

- [ ] 6.1 Write getting-started documentation for root discovery, v2 manifest loading, locale selection, collection indexes, and detail retrieval.
- [ ] 6.2 Document IDs, slugs, statuses, relationships, feature links, localization, recitations, and every structured block type with JSON examples.
- [ ] 6.3 Document collection, stage, source, feature, icon, schema, and asset registries.
- [ ] 6.4 Document technical validation versus scholarly review, contributor translation/review flow, deprecation, and publication states.
- [ ] 6.5 Document legacy compatibility, Quran dataset boundaries, release tags, CDN provider roles, and GitHub Pages preview behavior.
- [ ] 6.6 Add prominent contextual draft/under-review disclaimers to documentation and explorer detail layouts.

## 7. Dataset Visualization

- [ ] 7.1 Build a manifest-derived dashboard showing dataset version, locales, collection totals, stage totals, and publication-state summaries.
- [ ] 7.2 Build a responsive seven-stage timeline with localized goals, entry content, ordered membership, adaptive Quran paths, and detail links.
- [ ] 7.3 Build a collection explorer with locale-aware search and filters for type, stage, status, group, and seasonal tags.
- [ ] 7.4 Build collection/content cards with semantic icons, explicit statuses, metadata, visual detail links, and compact API action menus.
- [ ] 7.5 Implement generic lesson, practice, supplication, sequence, and glossary-entry detail views.
- [ ] 7.6 Implement renderers for headings, paragraphs, ordered/unordered lists, quotations, callouts, recitations, steps, checklists, image, audio, and source-reference blocks.
- [ ] 7.7 Add source, relationship, feature-link, completion-prompt, review, and semantic-icon presentations with fallback behavior.
- [ ] 7.8 Add preview, raw JSON, API, sources, and relationships tabs with syntax highlighting, copy, and download actions.
- [ ] 7.9 Add responsive loading, error, empty, missing-item, and invalid-query states for all explorer pages.

## 8. CDN API Explorer

- [ ] 8.1 Add centralized repository/release configuration and URL templates for jsDelivr, Statically, GitHub Raw, and GitHub Pages.
- [ ] 8.2 Build provider and stable/main version selectors, default to stable jsDelivr, and display a mutable-main warning.
- [ ] 8.3 Build reusable API access panels for manifest, stages, indexes, registries, schemas, SVG assets, and content details using exact manifest/index paths.
- [ ] 8.4 Implement accessible URL copy feedback with manual-selection fallback and safe raw links using new-tab opener isolation.
- [ ] 8.5 Implement JSON download and raw JSON copy actions for locally bundled and remote-preview documents.
- [ ] 8.6 Implement remote response preview with loading, HTTP metadata, JSON parsing, CORS/network/error states, and explicit alternative-provider actions.
- [ ] 8.7 Generate synchronized JavaScript, TypeScript, cURL, and PowerShell snippets from the selected provider, version, and endpoint.
- [ ] 8.8 Build the API playground with common endpoint picker, indexed-content picker, send request, response viewer, URL copy, raw open, and snippets.
- [ ] 8.9 Verify supported provider URL formats and CORS behavior and document any provider-specific preview limitations.

## 9. Portal Testing and Production Build

- [ ] 9.1 Add unit tests for locale fallback, data statistics, filters, semantic icon fallback, URL generation, snippets, clipboard fallback, and API response states.
- [ ] 9.2 Add component tests for status visibility, Arabic RTL rendering, journey interaction, content blocks, API menus, and accessible feedback.
- [ ] 9.3 Run TypeScript checks and production VitePress builds for both light/dark-capable output and resolve all build errors.
- [ ] 9.4 Verify generated routes, scripts, styles, bundled JSON, and SVGs work under the `/islamic-json/` base path.
- [ ] 9.5 Audit keyboard behavior, mobile layouts, contrast, raw new-tab safety, and draft-review disclaimers.

## 10. GitHub Actions and Pages

- [x] 10.1 Add a GitHub Actions workflow triggered by pull requests, `main` pushes, and manual dispatch.
- [x] 10.2 Configure Python dependency caching, dataset validation, validator unit tests, Node setup, npm lockfile caching, `npm ci`, type checking, and production docs build.
- [x] 10.3 Configure least-privilege Pages permissions, deployment concurrency, `github-pages` environment, official artifact upload, and deploy jobs.
- [x] 10.4 Ensure pull requests run every quality gate but cannot execute the production deployment path.
- [x] 10.5 Ensure successful `main` pushes deploy `docs/.vitepress/dist` and expose the resulting Pages environment URL.
- [x] 10.6 Document the one-time repository setting to select GitHub Actions as the Pages source and the manual redeploy procedure.
- [ ] 10.7 Validate the workflow syntax and simulate or run the build commands locally using the same versions and working directories.

## 11. Release Readiness

- [ ] 11.1 Confirm the final diff represents path-only moves for legacy and Quran data and contains no unintended source-content changes.
- [ ] 11.2 Run complete data validation, Python tests, portal unit/component tests, type checking, static build, and generated artifact inspection.
- [ ] 11.3 Record final old/new paths, Pages URL, provider URL templates, expected compatibility tag, and release rollback procedure.
- [ ] 11.4 With explicit release authorization, create and push the pre-move compatibility tag, commit the new layout, and publish the new immutable release tag.
- [ ] 11.5 After tags and Pages deployment exist, verify version-pinned manifest, collection, content, schema, and SVG URLs through jsDelivr, Statically where supported, and GitHub Pages.
- [ ] 11.6 Mark the remaining CDN verification task in `standardize-multilingual-content-data` complete only after its tagged SVG URLs resolve successfully.

## 12. Multi-dataset Demo UI

- [x] 12.1 Add a distinct Demo UI navigation section and dataset switcher for v2 Learning, Legacy Browser, and Holy Quran Browser.
- [x] 12.2 Extend the generated portal-data preparation pipeline with isolated lazy-loadable legacy and Quran namespaces without changing source dataset bytes.
- [ ] 12.3 Build the v2 Learning Demo UI with dashboard, seven-stage progression, collection browsing, content details, and data-inspection actions.
- [ ] 12.4 Build Legacy Browser adapters for Asmaul Husna, dhikr, dua, and pillars-of-Islam data, including explicit legacy status, known issues, and malformed-resource states.
- [x] 12.5 Build Holy Quran Browser navigation for juz and surah, selected-surah metadata and ayah rendering, Arabic RTL, search, and independent-dataset labeling.
- [x] 12.6 Connect every Demo UI view to the API inspector using its exact source path, provider controls, raw opening, JSON preview, and download actions.
- [ ] 12.7 Add tests for dataset switching, lazy resource loading, legacy parse-error presentation, Quran Arabic RTL, and Demo UI-to-inspector path handoff.
- [ ] 12.8 Validate bundle size, generated data boundaries, responsive Demo UI behavior, type checking, and production build.

## 13. Remove Unrequested Editorial UI

- [ ] 13.1 Remove draft, under-review, reviewed, translated, and publication-status labels, filters, statistics, disclaimers, and review language from the portal.
- [ ] 13.2 Present v2 content using localized titles, types, stages, and source paths rather than editorial status or technical IDs as the primary Demo UI presentation.
- [ ] 13.3 Update API, guide, reference, and contributing pages to describe technical JSON validation without an invented reviewer workflow.
