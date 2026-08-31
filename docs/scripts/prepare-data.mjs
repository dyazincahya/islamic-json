import { cp, mkdir, rm } from "node:fs/promises";
import { basename, resolve } from "node:path";

const docsRoot = resolve(import.meta.dirname, "..");
const repositoryRoot = resolve(docsRoot, "..");
const dataRoot = resolve(repositoryRoot, "data");
const v2Root = resolve(dataRoot, "v2");
const legacyRoot = resolve(dataRoot, "legacy");
const quranRoot = resolve(dataRoot, "holy-quran");
const outputRoot = resolve(docsRoot, "public", "data");
const v2Entries = [
  "manifest.json",
  "stages.json",
  "indexes",
  "content",
  "registries",
  "schemas",
  "assets/icons",
];

await rm(outputRoot, { recursive: true, force: true });
await mkdir(outputRoot, { recursive: true });
for (const entry of v2Entries) {
  await cp(resolve(v2Root, entry), resolve(outputRoot, entry), {
    recursive: true,
  });
}

// These resources remain individual static files. The Demo UI fetches them only
// after a user chooses the Legacy or Holy Quran browser. Dataset README files
// remain documentation at the repository root and are not Pages data assets.
const isPublicDatasetFile = (path) =>
  !path.includes("migration") && basename(path).toLowerCase() !== "readme.md";
await cp(legacyRoot, resolve(outputRoot, "legacy"), {
  recursive: true,
  filter: isPublicDatasetFile,
});
await cp(quranRoot, resolve(outputRoot, "holy-quran"), {
  recursive: true,
  filter: isPublicDatasetFile,
});
console.log(`Prepared v2, legacy, and Holy Quran portal data from ${dataRoot}`);
