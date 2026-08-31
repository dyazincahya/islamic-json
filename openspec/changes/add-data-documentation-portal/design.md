## Context

The repository is a static-data project consumed through GitHub-backed CDN URLs. A standardized `v2/` dataset, validators, generated indexes, semantic icon assets, and hundreds of bilingual documents now exist, while older collections and the Quran dataset remain at root-level paths. The active standardization change has one release-dependent CDN verification task remaining.

The new portal must serve both nontechnical learners exploring content structure and developers integrating JSON. It must run as a static GitHub Pages site under a repository subpath, validate data before deployment, and avoid equating schema validity with scholarly review. See `proposal.md` for motivation and scope.

## Goals / Non-Goals

**Goals:**

- Make repository and public paths self-explanatory.
- Provide one static documentation application with prose, interactive Vue views, and direct endpoint access.
- Render the v2 contract generically from manifests, indexes, types, and blocks rather than hardcoding individual lessons.
- Keep portal preview data aligned with the exact deployed commit while teaching stable release-pinned CDN integration.
- Establish repeatable PR checks and main-branch Pages deployment.

**Non-Goals:**

- Building a backend, authenticated API, database, CMS, or user-progress service.
- Modifying Quran text or treating the Quran dataset as legacy.
- Scholarly approval of draft curriculum.
- Providing a full Quran reader, hadith library browser, or Postman-equivalent HTTP client in the first portal release.
- Automatically committing, tagging, or pushing a release without explicit authorization.

## Decisions

### 1. Use `data/` as the public dataset root

The target hierarchy is:

```text
data/
├── legacy/
│   ├── asmaul-husna/
│   ├── dhikr/
│   ├── dua/
│   └── pillars-of-islam/
├── v2/
└── holy-quran/
```

`legacy` is preferred over `v1` because the old collections do not share one formal version-one contract. Quran is independent rather than deprecated. A root manifest becomes the starting point.

Direct movement is intentionally breaking. Duplicating every legacy directory indefinitely was rejected because copies drift and leave the root cluttered. The compatibility boundary is an immutable pre-move release tag plus a migration table; creating that tag is a separately authorized release operation.

### 2. Build the portal in `docs/` with VitePress, Vue 3, TypeScript, and Tailwind

VitePress supplies Markdown documentation, static generation, local search, routing, and Vue component embedding. Custom Vue pages/components provide the dashboard and explorers. A plain Vite SPA was rejected because it would require recreating documentation navigation and Markdown integration; a stock docs theme without custom Vue was rejected because visualization and API interaction are core requirements.

Dependencies are isolated in `docs/package.json` with a committed lockfile. Generated output, copied data, and `node_modules` remain ignored.

### 3. Apply the Obsidian Emerald semantic design system

The visual language uses GitHub Primer-inspired density and hierarchy without cloning GitHub components: neutral canvas/surface/border/text tokens, restrained emerald primary/focus/selection, blue links, amber review warnings, red errors/deprecations, small radii, minimal shadows, system sans, monospace code, and Noto Naskh Arabic fallback.

Tokens are CSS variables consumed through semantic Tailwind utilities, allowing light/dark/system modes without color literals throughout templates. Status always includes text, keyboard focus is explicit, Arabic uses RTL, motion respects reduced preferences, and layouts collapse from header + left navigation + content + right TOC to accessible drawers on narrow screens.

### 4. Treat manifests, indexes, and original resource paths as the portal's data API

A data service loads root/v2 manifests, stages, indexes, registries, legacy collection paths, and Quran juz/surah paths. It caches requests, resolves v2 locale fallback, and fetches detail documents on demand. Statistics, filters, navigation, and endpoint paths are derived from those files. Runtime validation is lightweight and user-facing errors identify missing, malformed, or unsupported resources; repository validation remains the authoritative build gate.

The portal separates API documentation from a click-through Demo UI. The Demo UI provides a v2 dashboard, journey, collection search, and typed block views; a legacy browser that uses collection-specific adapters and never mutates original shapes; and an independent Quran browser that navigates juz, 114-surah metadata, and selected ayah documents. Every view can hand its exact source path to the API inspector. Dynamic details use static-safe query parameters rather than generating hundreds of dedicated routes.

### 5. Bundle commit-matched datasets with lazy detail loading

A preparation script clears `docs/public/data/` and copies public `data/v2` files needed at runtime: manifest, stages, indexes, content, registries, schemas, and selected assets. It also copies legacy collections and Quran resources under distinct generated namespaces. Fixtures and migration checksums remain excluded. VitePress emits these files under the Pages site, so each browser previews the same checkout even before a CDN tag exists.

The initial Demo UI route loads root/v2 discovery data only. Legacy data and Quran juz/surah detail JSON remain separate static resources fetched after the user selects a dataset or item. `docs/public/data/` is generated and ignored. The runtime base comes from VitePress site base and environment configuration, avoiding absolute-root bugs under `/islamic-json/`.

### 6. Centralize CDN provider and release configuration

A provider registry owns URL templates for jsDelivr, Statically, GitHub Raw, and GitHub Pages. Input consists of repository owner/name, selected stable tag or `main`, and a path supplied by a manifest/index. No component hand-builds paths.

jsDelivr is recommended; Statically is alternative; GitHub Raw is debugging fallback; Pages is commit-matched preview. Stable tag is the default production mode. Selecting `main` shows a warning. Provider CORS behavior is verified during implementation; copy/open remain available even if preview fetch is blocked.

The API panel supports Clipboard API with manual fallback, `target=_blank` with `noopener noreferrer`, explicit provider failures, JSON preview/download, and generated JavaScript, TypeScript, cURL, and PowerShell snippets. It never silently switches providers.

### 7. Use one Pages workflow with build and conditional deploy jobs

The workflow triggers on pull request, pushes to `main`, and manual dispatch. Build checks out code, installs Python dependencies, validates data and validator tests, installs Node dependencies with `npm ci`, type-checks, builds VitePress, and verifies static output. PRs stop there.

For successful `main` pushes (and authorized dispatch against the deployment branch), the workflow configures Pages, uploads `docs/.vitepress/dist`, and deploys through the `github-pages` environment using official Pages artifact actions. Permissions are least-privilege, deployment has concurrency control, and no secret is required. Repository Pages source must be configured to GitHub Actions.

### 8. Sequence restructuring before portal endpoint finalization

Implementation first records current paths and updates all Python tooling atomically with data moves. It then creates manifests/migration docs and revalidates. Portal loaders and CDN templates target the finalized `data/` hierarchy. This avoids writing a UI against temporary paths.

The existing standardization change's last CDN task cannot be truthfully completed until an authorized tag is published. This portal can implement and locally verify all URL construction, then release verification closes both efforts.

## Risks / Trade-offs

- [Breaking old unpinned CDN URLs] → Preserve the old tree in an immutable tag, publish a complete migration table, and make stable tagged URLs the documented default.
- [Moving hundreds of files obscures content changes] → Perform path-only moves separately from content edits and verify checksums before and after.
- [Portal bundles legacy and Quran resources] → Copy only browser-required public resources, lazy-load all legacy and Quran detail documents, and enforce artifact-size checks in CI.
- [CDN CORS or availability differs by provider] → Verify providers, show errors explicitly, retain copy/open actions, and use bundled Pages data for the portal itself.
- [VitePress theme customization becomes brittle] → Keep overrides in a custom theme layer and avoid patching framework internals.
- [Dark theme harms Arabic/code readability] → Use semantic contrast tests, dedicated Arabic typography, and both theme build previews.
- [GitHub Pages subpath causes broken links] → Centralize base-path construction and test built output under `/islamic-json/`.
- [Draft religious content appears authoritative] → Render status and review disclaimers prominently and default filters without hiding draft state.
- [Release tag is unavailable during implementation] → Validate URL templates locally; leave tag creation and external CDN verification as explicit release tasks.

## Migration Plan

1. Record the current Git tree, hashes, and old-to-new mapping; prepare an explicit compatibility-tag release instruction.
2. Move old non-Quran collections to `data/legacy/`, `v2/` to `data/v2/`, and `holy-quran/` to `data/holy-quran/` without altering dataset contents.
3. Update root/v2 manifests, indexes, source paths, Python tools, fixtures, checksums, README, and validation tests; run complete validation.
4. Add root and legacy manifests plus migration documentation.
5. Scaffold `docs/`, design tokens, theme, layouts, navigation, localization, and documentation sections.
6. Add data preparation/loading, dashboard, journey, collection/content explorers, block renderer, raw JSON, and API/CDN tools.
7. Add portal tests, type checks, production build, and base-path verification.
8. Add the GitHub Actions workflow and document one-time Pages repository settings.
9. Add the Demo UI routes, v2 learning experience, legacy adapters, Quran browser, and inspection bridge; test lazy resource loading and malformed legacy states.
10. With explicit release authorization, preserve the prior layout tag, commit the breaking layout, publish the new release tag, deploy Pages, and verify version-pinned CDN and SVG endpoints.

Rollback before release restores the path moves and documentation workflow. After tagged release, old consumers stay on the compatibility tag while corrections ship in a new immutable version.

## Open Questions

- A future custom domain can replace the repository Pages base through configuration without changing portal behavior.
- The current Quran dataset exposes static files rather than a dedicated normalized index; browser metadata can be derived at preparation time without changing Quran source bytes.
