## 1. Compatibility Baseline and Tooling

- [x] 1.1 Inventory all public non-Quran/non-hadith JSON paths, root shapes, and field variants, and save the inventory as a migration reference.
- [x] 1.2 Add compatibility fixtures or checksums that detect unintended changes to existing legacy JSON files and excluded `holy-quran` or hadith-library paths.
- [x] 1.3 Establish the repository validation toolchain and one documented command that can validate JSON Schema plus dataset-wide integrity.
- [x] 1.4 Add automated checks that reject malformed or empty JSON in v2 and report the file and parse error.

## 2. V2 Structure and Core Schemas

- [x] 2.1 Create the `v2/` directory structure for manifests, indexes, typed content, registries, schemas, and optional icon assets without moving legacy files.
- [x] 2.2 Define shared schemas for semantic identifiers, BCP 47 localized fields, slugs, relative paths, publication states, relationships, feature links, review metadata, and document envelopes.
- [x] 2.3 Define schemas for manifest, collection index, stage, lesson, practice, supplication, sequence, and glossary-entry documents.
- [x] 2.4 Define and document the structured block vocabulary for headings, paragraphs, lists, quotations, callouts, recitations, steps, checklists, images, audio references, and source references.
- [x] 2.5 Define standardized recitation schemas for Arabic script, localized transliteration, localized translation, and optional audio metadata.
- [x] 2.6 Add positive fixtures for every document and block type and negative fixtures for invalid IDs, missing locales, unsupported blocks, empty Arabic values, and embedded HTML.

## 3. Manifest, Indexes, and Cross-File Validation

- [x] 3.1 Add the v2 manifest with schema version, dataset version, default locale, supported locales, collection discovery paths, and optional version-pinned asset base URL metadata.
- [x] 3.2 Add initial collection indexes that expose item IDs, types, slugs, statuses, and relative document paths.
- [x] 3.3 Implement validation for globally unique identifiers, index-to-file agreement, valid relative paths, and document type compatibility.
- [x] 3.4 Implement validation for stage membership and prerequisite, next, related, recitation, source, feature, and icon reference resolution.
- [x] 3.5 Implement reviewed-state gates for required Indonesian and English fields, structured sources, review outcomes, reviewer attribution, and review dates.
- [x] 3.6 Ensure validation explicitly excludes content inspection or rewriting under `holy-quran` and any hadith-library dataset while still detecting accidental modifications through compatibility checks.

## 4. Provenance and Editorial Review

- [x] 4.1 Define source records for Quran references, hadith references, books, articles, and web resources with stable IDs and bilingual citation labels.
- [x] 4.2 Create the initial reusable source registry and add validation for source-type-specific locators and unresolved source IDs.
- [x] 4.3 Add publication and review metadata examples for `draft`, `translated`, `under-review`, `reviewed`, and `deprecated` items.
- [x] 4.4 Add validation that free-form source strings cannot satisfy reviewed readiness and that deprecated items retain IDs, reasons, and valid optional replacement references.
- [x] 4.5 Document the contributor workflow for translation, source verification, content review, locale review, deprecation, and promotion to reviewed status.

## 5. Semantic Icon Registry

- [x] 5.1 Define the controlled semantic icon ID vocabulary for general, faith, worship, purification, Quran-learning, daily-life, location, and time concepts.
- [x] 5.2 Create the icon registry with bilingual accessible labels, semantic fallbacks, optional Font Awesome and Material Symbols mappings, and optional SVG metadata.
- [x] 5.3 Add validation for unknown icon IDs, missing registry references, invalid provider metadata, and circular fallback chains.
- [x] 5.4 Define SVG safety, view-box, style, provenance, license, attribution, and relative-path rules in schema and contributor documentation.
- [x] 5.5 Implement SVG checks that reject scripts, external resources, font-dependent text, presentation-library classes, and missing required licensing metadata.
- [ ] 5.6 Add a small representative SVG subset only for semantic concepts that need a repository default, and verify each asset resolves through a version-pinned CDN URL; leave other entries provider- or application-mapped.

## 6. Seven-Stage Journey Catalog

- [x] 6.1 Create the bilingual catalog for the seven ordered stages with stable IDs, numeric order, goals, entry-content IDs, and index membership.
- [x] 6.2 Add semantic feature-link definitions for prayer schedules, location, audio, reminders, calculators, reading, bookmarks, and continuation history.
- [x] 6.3 Add completion-prompt models and examples for acknowledgements and practice checklists without introducing user state into the dataset.
- [x] 6.4 Add semantic seasonal tags and index behavior for Ramadan, Eid al-Fitr, and Hajj-season discovery.
- [x] 6.5 Add the four adaptive Quran-learning entry paths and references to application Quran features without editing or embedding `holy-quran` data.
- [x] 6.6 Add the thematic hadith-guidance journey shape with explanation, life example, action, and bibliographic reference without editing or duplicating a hadith-library dataset.
- [x] 6.7 Validate complete stage membership, stage ordering, entry IDs, relationship targets, feature identifiers, and seasonal tags.

## 7. Existing Data Migration

- [x] 7.1 Migrate all 99 Asmaul Husna entries to stable IDs, standardized Arabic and transliteration fields, bilingual meanings, source/review metadata, and a v2 collection index.
- [x] 7.2 Migrate daily dua entries to typed supplications with stable IDs, standardized recitations, bilingual titles/translations/benefits, structured sources, and explicit review status.
- [x] 7.3 Replace the empty morning-dhikr migration input with valid v2 draft metadata or migrated content while leaving the malformed legacy file unchanged until a separate compatibility decision.
- [x] 7.4 Migrate Shahada content into lesson and recitation structures, replacing HTML extras with blocks and assigning source/review metadata.
- [x] 7.5 Migrate the five obligatory prayer documents into reusable lesson, practice, facts, recitation, feature-link, and completion structures.
- [x] 7.6 Migrate fasting intention and breaking-fast documents, correcting content type labels where recitations are prayers rather than intentions and preserving uncertain claims as draft or under-review.
- [x] 7.7 Migrate zakat-fitrah documents into structured lessons and supplications, replacing HTML extras with blocks and representing amounts, timing, and recipients as structured facts where appropriate.
- [x] 7.8 Migrate the Hajj sequence into ordered stable steps, omit empty recitations, add bilingual context, and attach structured source/review metadata.
- [x] 7.9 Generate or update v2 indexes for every migrated collection and run schema, relationship, locale, provenance, icon, and compatibility validation.

## 8. Stage 1 and Stage 2 Content

- [x] 8.1 Add bilingual draft lessons for what Islam is, who Allah is, who Prophet Muhammad is, and why humans worship.
- [x] 8.2 Add bilingual draft lessons for the relationship between iman, Islam, and ihsan and for the roles of the Quran and hadith.
- [x] 8.3 Add the Shahada journey branching into knowing Allah, tawhid, purpose of worship, knowing Prophet Muhammad, following Sunnah, and understanding hadith.
- [x] 8.4 Add six bilingual foundations-of-faith lessons covering Allah, angels, revealed books, messengers, the Last Day, and divine decree.
- [x] 8.5 Connect Stage 1 and Stage 2 prerequisites, next links, related links, completion prompts, sources, and review metadata and validate the graph.

## 9. Stage 3 and Stage 4 Content

- [x] 9.1 Add bilingual purification lessons for cleanliness, najis, hadas, wudu, tayammum, and obligatory bathing.
- [x] 9.2 Add bilingual prayer lessons and practices for prayer times, movements, recitations, five obligatory prayers, congregational prayer, and voluntary prayer.
- [x] 9.3 Connect prayer content to semantic schedule, location, audio, reminder, and practice-checklist features and validate all references.
- [x] 9.4 Add bilingual fasting lessons for purpose, conditions, pillars, invalidators, suhur, breaking fast, Ramadan, voluntary fasts, qada, and fidyah.
- [x] 9.5 Add bilingual zakat lessons for purpose, zakat fitrah, zakat mal, obligation, eligible recipients, and non-authoritative calculator guidance.
- [x] 9.6 Add bilingual Hajj and Umrah lessons for rulings, conditions, ihram, ritual sequences, prohibitions, prayers, and travel guidance.
- [x] 9.7 Connect Stage 3 and Stage 4 order, prerequisites, seasonal tags, feature links, sources, review metadata, and completion prompts and validate the graph.

## 10. Stage 5, Stage 6, and Stage 7 Content

- [x] 10.1 Add bilingual supporting lessons for Iqra, Arabic letters, vowel marks, joined letters, basic tajwid, reading practice, translation, brief interpretation, thematic verses, and reading consistency without changing Quran data.
- [x] 10.2 Add bilingual thematic hadith-guidance drafts for intention, honesty, guarding speech, parents, compassion, eating, sleeping, neighbors, and seeking knowledge.
- [x] 10.3 Add bilingual daily-life content for daily dua, morning/evening dhikr, eating, sleeping, travel, family, parents, basic transactions, halal food, charity, health, cleanliness, sadness, anxiety, and life trials.
- [x] 10.4 Connect Stage 5 through Stage 7 adaptive paths, thematic links, practices, feature links, sources, review metadata, and completion prompts and validate the graph.
- [x] 10.5 Audit all seven stages for required topic coverage, unresolved links, duplicate content, missing Indonesian or English text, and inappropriate reviewed status.

## 11. Documentation and Release Validation

- [x] 11.1 Update the repository documentation with v2 architecture, naming conventions, localized fields, content types, structured blocks, source and review workflow, icon resolution, and legacy compatibility policy.
- [x] 11.2 Document jsDelivr and alternative CDN examples using version-pinned manifest, content, index, and SVG URLs plus application fallback guidance.
- [x] 11.3 Add consumer examples for locale selection, index discovery, content-block rendering, relationship navigation, source display, and semantic icon provider mapping.
- [x] 11.4 Run the complete validator over schemas, fixtures, v2 data, indexes, relationships, review gates, SVG assets, and compatibility protections and resolve every reported error.
- [x] 11.5 Confirm the implementation diff does not modify `holy-quran`, any hadith-library dataset, or existing legacy data shapes, and record the migration and validation summary for the v2 release.
