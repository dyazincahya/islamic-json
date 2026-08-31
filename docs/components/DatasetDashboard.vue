<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

type Collection = { id: string; itemType: string; indexPath: string };
type Index = { items?: Array<{ status?: string }> };

type Manifest = { datasetVersion: string; defaultLocale: string; supportedLocales: string[]; collections: Collection[] };
const manifest = ref<Manifest | null>(null);
const indexes = ref<Index[]>([]);
const stages = ref<{ stages?: unknown[] } | null>(null);
const error = ref("");

const total = computed(() => indexes.value.reduce((count, index) => count + (index.items?.length ?? 0), 0));
const states = computed(() => indexes.value.flatMap((index) => index.items ?? []).reduce<Record<string, number>>((all, item) => {
  const status = item.status ?? "unknown";
  all[status] = (all[status] ?? 0) + 1;
  return all;
}, {}));

onMounted(async () => {
  try {
    const load = async <T,>(path: string) => {
      const response = await fetch(`${import.meta.env.BASE_URL}data/${path}`);
      if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
      return response.json() as Promise<T>;
    };
    manifest.value = await load<Manifest>("manifest.json");
    stages.value = await load("stages.json");
    indexes.value = await Promise.all(manifest.value.collections.map((item) => load<Index>(item.indexPath)));
  } catch (cause) {
    error.value = cause instanceof Error ? cause.message : "Data portal tidak dapat dimuat.";
  }
});
</script>

<template>
  <p v-if="error" class="oe-card text-danger">Gagal memuat data: {{ error }}</p>
  <p v-else-if="!manifest" class="oe-card">Memuat ringkasan dataset…</p>
  <div v-else class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
    <section class="oe-card"><strong>Versi</strong><p>{{ manifest.datasetVersion }}</p></section>
    <section class="oe-card"><strong>Konten</strong><p>{{ total }}</p></section>
    <section class="oe-card"><strong>Tahap</strong><p>{{ stages?.stages?.length ?? 0 }}</p></section>
    <section class="oe-card"><strong>Locale</strong><p>{{ manifest.supportedLocales.join(", ") }} · default {{ manifest.defaultLocale }}</p></section>
    <section v-for="(count, status) in states" :key="status" class="oe-card">
      <span :class="`oe-status oe-status--${status}`">{{ status }}</span><p>{{ count }} item</p>
    </section>
  </div>
</template>
