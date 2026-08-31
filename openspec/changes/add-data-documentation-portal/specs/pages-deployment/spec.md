## Purpose

Defines reproducible quality checks and secure static deployment so the documentation portal and its bundled dataset are published automatically through GitHub Pages.

## ADDED Requirements

### Requirement: Commit-matched portal datasets

The documentation build SHALL copy the public v2 manifest, stages, indexes, content, registries, schemas, and selected assets from the current commit. It SHALL also copy the legacy and Quran resources needed by their Demo UI browsers while excluding fixtures and migration checksums. Dataset resources SHALL be loaded on demand by the browser so the initial Demo UI route does not fetch the full Quran or legacy payload.

#### Scenario: Portal is built locally

- **WHEN** the documentation build runs
- **THEN** stale generated data is cleared and the resulting portal uses v2, legacy, and Quran resources from that checkout

#### Scenario: User opens the v2 Demo UI

- **WHEN** a user only navigates current v2 learning content
- **THEN** the browser does not request Quran or legacy detail payloads until the user selects those dataset browsers

### Requirement: Pull request quality gates

Pull requests SHALL run dataset validation, validator tests, dependency installation from a lockfile, TypeScript checking, and a production documentation build without deploying to GitHub Pages.

#### Scenario: Pull request contains invalid relationship

- **WHEN** dataset validation fails in a pull request
- **THEN** the workflow fails and no deploy job runs

### Requirement: Main branch deployment

A successful push to `main` SHALL build the portal, upload the static output as a GitHub Pages artifact, and deploy it through the protected `github-pages` environment.

#### Scenario: Main build succeeds

- **WHEN** all checks pass for a push to `main`
- **THEN** the generated artifact is deployed and the environment reports the published Pages URL

### Requirement: Least-privilege workflow

The build job SHALL require read-only repository access, and Pages write plus identity-token permissions SHALL be limited to the deployment workflow needs. Concurrent deployments SHALL not corrupt or race published output.

#### Scenario: Pull request workflow runs

- **WHEN** the event is a pull request
- **THEN** it has no effective path to deploy a Pages artifact to production

### Requirement: Repository-subpath-safe build

The portal SHALL build links, routes, scripts, styles, images, bundled data, and SVG assets correctly beneath the repository Pages base path `/islamic-json/`, with configuration available for a future custom domain.

#### Scenario: Portal opens from GitHub Pages

- **WHEN** a user opens `https://dyazincahya.github.io/islamic-json/`
- **THEN** navigation, assets, explorer data, and deep documentation links resolve under the repository subpath

### Requirement: Manual deployment trigger

The workflow SHALL support an authorized manual trigger for rerunning checks and deployment behavior without requiring an unrelated source change.

#### Scenario: Maintainer dispatches workflow

- **WHEN** an authorized maintainer runs the workflow manually against the deployment branch
- **THEN** the same validation and build gates execute before any deployment
