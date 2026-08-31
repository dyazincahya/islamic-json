<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

type Dataset = "v2" | "legacy" | "quran";
type Json = Record<string, unknown>;
const dataset = ref<Dataset>("v2");
const loading = ref(false);
const error = ref("");
const v2Items = ref<Array<Json>>([]);
const legacyManifest = ref<Json | null>(null);
const selectedLegacy = ref("data/legacy/asmaul-husna/asmaul-husna.json");
const legacyData = ref<unknown>(null);
const juz = ref<Array<Json>>([]);
const selectedSurah = ref(1);
const selectedJuz = ref(1);
const surahQuery = ref("");
const surah = ref<Json | null>(null);

const base = import.meta.env.BASE_URL;
const quranPrefix = "data/holy-quran/ministry-of-religion-of-the-republic-of-indonesia";
const sourcePath = computed(() => dataset.value === "legacy" ? selectedLegacy.value : dataset.value === "quran" ? `${quranPrefix}/surah/${selectedSurah.value}.json` : "data/v2/indexes/lessons.json");
const inspectUrl = computed(() => `${base}api/?path=${encodeURIComponent(sourcePath.value)}`);
const legacyCollections = computed(() => Array.isArray(legacyManifest.value?.collections) ? legacyManifest.value.collections as Json[] : []);
const selectedSurahDocument = computed(() => surah.value?.[String(selectedSurah.value)] as Json | undefined);
const visibleSurahNumbers = computed(() => Array.from({ length: 114 }, (_, index) => index + 1).filter((number) => String(number).includes(surahQuery.value.trim())));
const ayah = computed(() => Object.entries((selectedSurahDocument.value?.text as Json | undefined) ?? {}));

async function loadJson<T>(path: string): Promise<T> {
  const result = await fetch(`${base}${path}`);
  if (!result.ok) throw new Error(`${path}: HTTP ${result.status}`);
  return result.json() as Promise<T>;
}
async function loadV2() {
  loading.value = true; error.value = "";
  try {
    const manifest = await loadJson<{ collections: Array<{ indexPath: string }> }>("data/manifest.json");
    const indexes = await Promise.all(manifest.collections.map((collection) => loadJson<{ items: Json[] }>(`data/${collection.indexPath}`)));
    v2Items.value = indexes.flatMap((index) => index.items);
  } catch (cause) { error.value = cause instanceof Error ? cause.message : "Gagal memuat data v2."; } finally { loading.value = false; }
}
async function loadLegacyManifest() {
  loading.value = true; error.value = "";
  try { legacyManifest.value = await loadJson<Json>("data/legacy/manifest.json"); await loadLegacy(); } catch (cause) { error.value = cause instanceof Error ? cause.message : "Gagal memuat manifest legacy."; } finally { loading.value = false; }
}
async function loadLegacy() {
  loading.value = true; error.value = ""; legacyData.value = null;
  try { legacyData.value = await loadJson(selectedLegacy.value); } catch (cause) { error.value = `Resource legacy dipertahankan apa adanya dan tidak dapat diparse: ${cause instanceof Error ? cause.message : "unknown error"}`; } finally { loading.value = false; }
}
async function loadQuran() {
  loading.value = true; error.value = "";
  try { juz.value = (await loadJson<{ data: Json[] }>(`${quranPrefix}/juz.json`)).data; await loadSurah(); } catch (cause) { error.value = cause instanceof Error ? cause.message : "Gagal memuat katalog Quran."; } finally { loading.value = false; }
}
function goToJuz() {
  const selected = juz.value.find((item) => Number(item.index) === selectedJuz.value);
  const start = selected?.start as Json | undefined;
  if (start?.index) {
    selectedSurah.value = Number(start.index);
    void loadSurah();
  }
}
async function loadSurah() {
  loading.value = true; error.value = ""; surah.value = null;
  try { surah.value = await loadJson<Json>(`${quranPrefix}/surah/${selectedSurah.value}.json`); } catch (cause) { error.value = cause instanceof Error ? cause.message : "Gagal memuat surah."; } finally { loading.value = false; }
}
async function choose(next: Dataset) {
  dataset.value = next;
  if (next === "v2" && !v2Items.value.length) await loadV2();
  if (next === "legacy" && !legacyManifest.value) await loadLegacyManifest();
  if (next === "quran" && !juz.value.length) await loadQuran();
}
onMounted(() => { void loadV2(); });
</script>

<template>
  <section class="demo-browser" aria-labelledby="demo-browser-title">
    <header class="demo-browser__header"><div><p class="demo-browser__eyebrow">Click-through Demo UI</p><h2 id="demo-browser-title">Jelajahi data tanpa menulis JSON</h2><p>Demo ini memakai resource dari checkout yang sama. Pilih versi dataset, lalu buka detailnya.</p></div><a :href="inspectUrl">Inspect JSON/API →</a></header>
    <div class="demo-browser__switcher" role="tablist" aria-label="Dataset demo"><button type="button" role="tab" :aria-selected="dataset === 'v2'" :class="{active: dataset === 'v2'}" @click="choose('v2')">V2 Learning <small>Current</small></button><button type="button" role="tab" :aria-selected="dataset === 'legacy'" :class="{active: dataset === 'legacy'}" @click="choose('legacy')">Legacy Browser <small>Compatibility</small></button><button type="button" role="tab" :aria-selected="dataset === 'quran'" :class="{active: dataset === 'quran'}" @click="choose('quran')">Holy Quran <small>Independent</small></button></div>
    <p v-if="loading" class="demo-browser__notice">Memuat resource…</p><p v-if="error" class="demo-browser__error">{{ error }}</p>
    <div v-if="dataset === 'v2'" class="demo-browser__panel"><p class="demo-browser__notice">Konten v2 berstatus draft/under-review tetap diberi label; validasi teknis bukan persetujuan ilmiah.</p><div class="demo-browser__grid"><article v-for="item in v2Items.slice(0, 24)" :key="String(item.id)" class="demo-browser__card"><span class="oe-status" :class="`oe-status--${item.status}`">{{ item.status }}</span><strong>{{ item.id }}</strong><small>{{ item.type }} · {{ item.path }}</small></article></div><p v-if="v2Items.length > 24" class="demo-browser__notice">Menampilkan 24 dari {{ v2Items.length }} item; collection explorer lengkap menyusul.</p></div>
    <div v-else-if="dataset === 'legacy'" class="demo-browser__panel"><p class="demo-browser__warning"><strong>Legacy compatibility:</strong> format sumber tidak dinormalisasi. Resource malformed akan dilaporkan, bukan diperbaiki.</p><label class="demo-browser__field">Koleksi legacy<select v-model="selectedLegacy" @change="loadLegacy"><option v-for="collection in legacyCollections" :key="String(collection.id)" :value="String(collection.path)">{{ collection.id }}</option></select></label><pre v-if="legacyData"><code>{{ JSON.stringify(legacyData, null, 2) }}</code></pre></div>
    <div v-else class="demo-browser__panel"><p class="demo-browser__notice">Quran adalah dataset independen, bukan legacy. Ayat ditampilkan RTL dari file sumber tanpa perubahan.</p><div class="demo-browser__quran-controls"><label class="demo-browser__field">Cari nomor surah<input v-model="surahQuery" inputmode="numeric" placeholder="Contoh: 2 atau 114"></label><label class="demo-browser__field">Surah<select v-model.number="selectedSurah" @change="loadSurah"><option v-for="number in visibleSurahNumbers" :key="number" :value="number">Surah {{ number }}</option></select></label><label class="demo-browser__field">Juz tersedia<select v-model.number="selectedJuz" @change="goToJuz"><option v-for="item in juz" :key="String(item.index)" :value="Number(item.index)">Juz {{ item.index }} · Surah {{ (item.start as Json).index }}:{{ (item.start as Json).verse }}</option></select></label></div><article v-if="selectedSurahDocument" class="demo-browser__surah"><h3>{{ selectedSurahDocument.name_latin }} <span lang="ar" dir="rtl">{{ selectedSurahDocument.name }}</span></h3><p>{{ selectedSurahDocument.number_of_ayah }} ayat · {{ selectedSurahDocument.translations && 'Terjemahan Indonesia tersedia' }}</p><ol><li v-for="[number, text] in ayah" :key="number"><span>{{ number }}</span><p class="oe-arabic" lang="ar" dir="rtl">{{ text }}</p><small>{{ ((selectedSurahDocument.translations as Json | undefined)?.id as Json | undefined)?.text && (((selectedSurahDocument.translations as Json).id as Json).text as Json)[number] }}</small></li></ol></article></div>
  </section>
</template>

<style scoped>
.demo-browser { display:grid; gap:1rem; padding:1.25rem; border:1px solid var(--oe-border); border-radius:8px; background:var(--oe-surface); }.demo-browser__header { display:flex; justify-content:space-between; gap:1rem; align-items:start; }.demo-browser__header h2 { margin:0; }.demo-browser__header p { color:var(--oe-muted); }.demo-browser__header a { white-space:nowrap; font-weight:700; }.demo-browser__eyebrow { color:var(--oe-accent)!important; text-transform:uppercase; font-size:.8rem; font-weight:700; letter-spacing:.06em; }.demo-browser__switcher { display:grid; grid-template-columns:repeat(3,1fr); gap:.5rem; }.demo-browser__switcher button { display:grid; gap:.15rem; padding:.75rem; border:1px solid var(--oe-border); border-radius:6px; background:var(--oe-canvas); color:var(--oe-fg); text-align:left; font-weight:700; cursor:pointer; }.demo-browser__switcher button.active { border-color:var(--oe-accent); box-shadow:inset 3px 0 var(--oe-accent); }.demo-browser__switcher small { color:var(--oe-muted); font-weight:500; }.demo-browser__panel { display:grid; gap:1rem; }.demo-browser__grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(13rem,1fr)); gap:.75rem; }.demo-browser__card { display:grid; gap:.4rem; padding:.75rem; border:1px solid var(--oe-border); border-radius:6px; background:var(--oe-canvas); }.demo-browser__card small { overflow-wrap:anywhere; color:var(--oe-muted); }.demo-browser__notice,.demo-browser__warning,.demo-browser__error { margin:0; padding:.75rem; border-left:3px solid var(--oe-link); background:color-mix(in srgb,var(--oe-link) 8%,transparent); }.demo-browser__warning { border-color:var(--oe-warning); background:color-mix(in srgb,var(--oe-warning) 10%,transparent); }.demo-browser__error { border-color:var(--oe-danger); background:color-mix(in srgb,var(--oe-danger) 10%,transparent); }.demo-browser__field { display:grid; gap:.35rem; max-width:35rem; font-weight:700; }.demo-browser__field select,.demo-browser__field input { padding:.55rem; border:1px solid var(--oe-border); border-radius:6px; background:var(--oe-canvas); color:var(--oe-fg); }.demo-browser pre { max-height:28rem; overflow:auto; margin:0; padding:1rem; border:1px solid var(--oe-border); border-radius:6px; background:var(--oe-canvas); font-size:.78rem; }.demo-browser__quran-controls { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:.75rem; }.demo-browser__surah h3 span { margin-inline-start:.5rem; }.demo-browser__surah ol { padding:0; list-style:none; }.demo-browser__surah li { padding:1rem 0; border-top:1px solid var(--oe-border); }.demo-browser__surah li > span { color:var(--oe-muted); font-size:.8rem; }.demo-browser__surah li small { color:var(--oe-muted); }.oe-arabic { text-align:right; }
@media (max-width:640px) { .demo-browser__header,.demo-browser__switcher,.demo-browser__quran-controls { display:grid; grid-template-columns:1fr; }.demo-browser__header a { white-space:normal; } }
</style>
