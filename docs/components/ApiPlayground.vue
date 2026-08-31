<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

type ProviderId = "jsdelivr" | "statically" | "github-raw" | "pages";
type Endpoint = { label: string; path: string; category: string };
type ResponseState = "idle" | "loading" | "success" | "error";

const repository = "dyazincahya/islamic-json";
const stableTag = "v2.0.0";
const provider = ref<ProviderId>("jsdelivr");
const version = ref<"stable" | "main">("stable");
const customPath = ref("");
const selectedPath = ref("data/v2/manifest.json");
const endpoints = ref<Endpoint[]>([
  { label: "Root discovery manifest", path: "manifest.json", category: "Discovery" },
  { label: "V2 manifest", path: "data/v2/manifest.json", category: "V2" },
  { label: "Seven learning stages", path: "data/v2/stages.json", category: "V2" },
  { label: "Lessons index", path: "data/v2/indexes/lessons.json", category: "Indexes" },
  { label: "Practices index", path: "data/v2/indexes/practices.json", category: "Indexes" },
  { label: "Supplications index", path: "data/v2/indexes/supplications.json", category: "Indexes" },
  { label: "Glossary index", path: "data/v2/indexes/glossary.json", category: "Indexes" },
  { label: "Icon registry", path: "data/v2/registries/icons.json", category: "Registries" },
  { label: "Content schema", path: "data/v2/schemas/content.schema.json", category: "Schemas" }
]);
const state = ref<ResponseState>("idle");
const response = ref<unknown>(null);
const responseText = ref("");
const responseMeta = ref("");
const error = ref("");
const feedback = ref("");
const activeSnippet = ref<"javascript" | "typescript" | "curl" | "powershell">("javascript");

const path = computed(() => (customPath.value.trim() || selectedPath.value).replace(/^\/+/, ""));
const revision = computed(() => version.value === "stable" ? stableTag : "main");
const providerLabel = computed(() => ({ jsdelivr: "jsDelivr", statically: "Statically", "github-raw": "GitHub Raw", pages: "GitHub Pages" })[provider.value]);
const url = computed(() => {
  if (provider.value === "jsdelivr") return `https://cdn.jsdelivr.net/gh/${repository}@${revision.value}/${path.value}`;
  if (provider.value === "statically") return `https://cdn.statically.io/gh/${repository}/${revision.value}/${path.value}`;
  if (provider.value === "github-raw") return `https://raw.githubusercontent.com/${repository}/${revision.value}/${path.value}`;
  return `${import.meta.env.BASE_URL}${path.value}`;
});
const prettyJson = computed(() => response.value === null ? "" : JSON.stringify(response.value, null, 2));
const snippets = computed(() => ({
  javascript: `const response = await fetch(${JSON.stringify(url.value)});\nif (!response.ok) throw new Error(\`HTTP \${response.status}\`);\nconst data = await response.json();`,
  typescript: `const response = await fetch(${JSON.stringify(url.value)});\nif (!response.ok) throw new Error(\`HTTP \${response.status}\`);\nconst data: unknown = await response.json();`,
  curl: `curl --fail-with-body ${JSON.stringify(url.value)}`,
  powershell: `Invoke-RestMethod -Uri ${JSON.stringify(url.value)} -Method Get`
}));
const activeSnippetContent = computed(() => snippets.value[activeSnippet.value]);

function setFeedback(message: string) {
  feedback.value = message;
  window.setTimeout(() => { feedback.value = ""; }, 3000);
}

async function copy(value: string, label: string) {
  try {
    await navigator.clipboard.writeText(value);
    setFeedback(`${label} disalin.`);
  } catch {
    setFeedback(`Tidak dapat menyalin otomatis. Pilih dan salin ${label.toLowerCase()} secara manual.`);
  }
}

function openRaw() {
  window.open(url.value, "_blank", "noopener,noreferrer");
}

function download() {
  const output = prettyJson.value || responseText.value;
  if (!output) return setFeedback("Jalankan request terlebih dahulu untuk mengunduh respons.");
  const anchor = document.createElement("a");
  anchor.href = URL.createObjectURL(new Blob([output], { type: "application/json" }));
  anchor.download = `${path.value.split("/").at(-1) || "response"}`;
  anchor.click();
  URL.revokeObjectURL(anchor.href);
}

async function send() {
  state.value = "loading";
  error.value = "";
  response.value = null;
  responseText.value = "";
  responseMeta.value = "";
  try {
    const result = await fetch(url.value, { headers: { Accept: "application/json" } });
    const contentType = result.headers.get("content-type") ?? "unknown content type";
    responseMeta.value = `${providerLabel.value} · HTTP ${result.status} ${result.statusText} · ${contentType}`;
    const body = await result.text();
    responseText.value = body;
    try { response.value = JSON.parse(body); } catch { response.value = null; }
    if (!result.ok) throw new Error(`Provider mengembalikan HTTP ${result.status}.`);
    if (response.value === null) throw new Error("Respons bukan JSON yang dapat diparse.");
    state.value = "success";
  } catch (cause) {
    state.value = "error";
    error.value = cause instanceof Error ? cause.message : "Request gagal.";
  }
}

onMounted(() => {
  const requestedPath = new URLSearchParams(window.location.search).get("path");
  if (requestedPath) {
    customPath.value = requestedPath;
    setFeedback("Path dari Demo UI dimuat ke API inspector.");
  }
});
</script>

<template>
  <section class="api-playground oe-card" aria-labelledby="api-playground-title">
    <div class="api-playground__heading">
      <div>
        <p class="api-playground__eyebrow">Interactive API explorer</p>
        <h2 id="api-playground-title">Coba endpoint secara langsung</h2>
        <p>Pilih resource, provider, dan versi. Tidak ada provider yang diganti otomatis ketika request gagal.</p>
      </div>
      <span class="oe-status">{{ providerLabel }}</span>
    </div>

    <div class="api-controls">
      <label><span>Provider</span><select v-model="provider"><option value="jsdelivr">jsDelivr — recommended</option><option value="statically">Statically — alternative</option><option value="github-raw">GitHub Raw — debugging</option><option value="pages">GitHub Pages — checkout preview</option></select></label>
      <label><span>Versi</span><select v-model="version" :disabled="provider === 'pages'"><option value="stable">Stable: {{ stableTag }}</option><option value="main">Latest: main</option></select></label>
      <label class="api-controls__wide"><span>Endpoint</span><select v-model="selectedPath" :disabled="Boolean(customPath)"><option v-for="endpoint in endpoints" :key="endpoint.path" :value="endpoint.path">{{ endpoint.category }} · {{ endpoint.label }}</option></select></label>
      <label class="api-controls__wide"><span>Atau path kustom</span><input v-model="customPath" placeholder="data/v2/content/lessons/...json" spellcheck="false"></label>
    </div>

    <p v-if="version === 'main' && provider !== 'pages'" class="api-warning"><strong>Mutable main:</strong> URL ini dapat berubah tanpa pemberitahuan. Gunakan release tag untuk produksi.</p>
    <div class="api-url"><code>{{ url }}</code><button type="button" @click="copy(url, 'URL')">Copy URL</button><button type="button" @click="openRaw">Open raw ↗</button><button class="api-url__run" type="button" :disabled="state === 'loading'" @click="send">{{ state === 'loading' ? 'Loading…' : 'Send request' }}</button></div>
    <p class="sr-only" aria-live="polite">{{ feedback }}</p><p v-if="feedback" class="api-feedback">{{ feedback }}</p>

    <div v-if="state !== 'idle'" class="api-result">
      <header><strong>Response</strong><span>{{ responseMeta }}</span><button type="button" :disabled="!responseText" @click="copy(prettyJson || responseText, 'JSON')">Copy JSON</button><button type="button" :disabled="!responseText" @click="download">Download JSON</button></header>
      <p v-if="state === 'error'" class="api-error"><strong>Request gagal:</strong> {{ error }} Coba provider lain secara eksplisit dari pilihan di atas.</p>
      <pre v-else><code>{{ prettyJson || responseText }}</code></pre>
    </div>

    <details class="api-snippets">
      <summary>Integration snippets</summary>
      <div class="api-snippets__panel">
        <div class="api-snippets__tabs" role="tablist" aria-label="Snippet language">
          <button v-for="(_, name) in snippets" :id="`snippet-tab-${name}`" :key="name" type="button" role="tab" :aria-selected="activeSnippet === name" :class="{ 'is-active': activeSnippet === name }" @click="activeSnippet = name as typeof activeSnippet">{{ name }}</button>
        </div>
        <header><strong>{{ activeSnippet }}</strong><button type="button" @click="copy(activeSnippetContent, `${activeSnippet} snippet`)">Copy</button></header>
        <pre><code>{{ activeSnippetContent }}</code></pre>
      </div>
    </details>
  </section>
</template>

<style scoped>
.api-playground { display: grid; gap: 1rem; padding: 1.25rem; }
.api-playground__heading { display: flex; justify-content: space-between; gap: 1rem; align-items: start; }.api-playground__heading h2 { margin: 0; }.api-playground__heading p { color: var(--oe-muted); }.api-playground__eyebrow { color: var(--oe-accent) !important; font-weight: 700; font-size: .8rem; text-transform: uppercase; letter-spacing: .06em; }
.api-controls { display: grid; gap: .75rem; grid-template-columns: repeat(2, minmax(0, 1fr)); }.api-controls label { display: grid; gap: .35rem; font-weight: 600; font-size: .875rem; }.api-controls select, .api-controls input { min-width: 0; padding: .55rem .65rem; border: 1px solid var(--oe-border); border-radius: 6px; background: var(--oe-canvas); color: var(--oe-fg); }.api-controls__wide { grid-column: span 2; }
.api-warning, .api-error { margin: 0; padding: .75rem; border-left: 3px solid var(--oe-warning); background: color-mix(in srgb, var(--oe-warning) 10%, transparent); }.api-error { border-color: var(--oe-danger); background: color-mix(in srgb, var(--oe-danger) 10%, transparent); }
.api-url { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }.api-url code { flex: 1 1 28rem; overflow-wrap: anywhere; padding: .6rem; border: 1px solid var(--oe-border); border-radius: 6px; background: var(--oe-canvas); }.api-playground button { padding: .5rem .7rem; border: 1px solid var(--oe-border); border-radius: 6px; background: var(--oe-surface-muted); color: var(--oe-fg); font-weight: 600; cursor: pointer; }.api-playground button:hover { border-color: var(--oe-accent); }.api-playground button:disabled { cursor: not-allowed; opacity: .6; }.api-url__run { border-color: var(--oe-accent) !important; background: var(--oe-accent) !important; color: white !important; }
.api-result { overflow: hidden; border: 1px solid var(--oe-border); border-radius: 6px; }.api-result header, .api-snippets header { display: flex; gap: .5rem; align-items: center; flex-wrap: wrap; padding: .6rem .75rem; background: var(--oe-surface-muted); }.api-result header span { flex: 1; color: var(--oe-muted); font-size: .8rem; }.api-result pre, .api-snippets pre { max-width: 100%; max-height: 28rem; overflow: auto; margin: 0; padding: 1rem; background: var(--oe-canvas); font-size: .8rem; white-space: pre; }.api-snippets summary { cursor: pointer; font-weight: 700; }.api-snippets__panel { display: grid; margin-top: .75rem; border: 1px solid var(--oe-border); border-radius: 6px; overflow: hidden; }.api-snippets__tabs { display: flex; gap: .25rem; overflow-x: auto; padding: .5rem; border-bottom: 1px solid var(--oe-border); background: var(--oe-surface); }.api-snippets__tabs button { flex: 0 0 auto; border-color: transparent; background: transparent; text-transform: capitalize; }.api-snippets__tabs button.is-active { border-color: var(--oe-accent); background: color-mix(in srgb, var(--oe-accent) 16%, transparent); color: var(--oe-accent); }.api-snippets header strong { flex: 1; text-transform: capitalize; }.api-feedback { margin: 0; color: var(--oe-success); font-weight: 600; }.sr-only { position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0,0,0,0); }
@media (max-width: 640px) { .api-controls { grid-template-columns: 1fr; }.api-controls__wide { grid-column: auto; }.api-playground__heading { display: grid; }.api-url > * { width: 100%; }.api-url code { flex-basis: 100%; } }
</style>
