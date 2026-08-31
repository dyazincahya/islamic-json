# Compatibility release procedure

Moving the public dataset directories under `data/` is a breaking path change. Before publishing that change, a release maintainer must preserve the current root-level layout in an immutable tag.

## Required authorization

Do not run the following commands until a maintainer explicitly authorizes creating a commit, tag, and push. This repository change prepares the documentation only; it does not create or publish a tag.

## Suggested sequence

1. Start from the reviewed commit that still contains the root-level layout.
2. Create an annotated compatibility tag. Replace `<compatibility-tag>` with the release name selected by the maintainer.

```sh
git tag -a <compatibility-tag> -m "Preserve pre-data-layout public paths"
git push origin <compatibility-tag>
```

3. Commit and push the reorganized `data/` layout after validation.
4. Create and publish a new immutable release tag for the reorganized layout.
5. Verify version-pinned CDN endpoints for both tags before announcing the migration.

## Consumer contract

- Existing integrations may use the old path only through the compatibility tag.
- New integrations must use the relocated `data/` paths and pin a published release tag.
- Never use mutable `main` URLs as a production compatibility guarantee.
