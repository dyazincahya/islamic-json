<script setup>
import { computed, ref } from 'vue'
import { getAsmaulHusna } from '../../../data'
import PageHero from '../../layout/PageHero.vue'

const props = defineProps({ locale: String, text: Object })
const query = ref('')
const names = getAsmaulHusna()
const filtered = computed(() => { const needle = query.value.toLocaleLowerCase(); return names.filter((item) => [item.latin, item.indo, item.arab].some((value) => String(value ?? '').toLocaleLowerCase().includes(needle))) })
</script>

<template>
  <PageHero title="Asmaul Husna" :description="text.asmaulDesc" api-path="asmaul-husna/asmaul-husna.json" />
  <section class="browser section-wrap"><div class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ filtered.length }} {{ locale === 'id' ? 'item' : 'items' }}</span></div><div class="asmaul-grid"><article v-for="item in filtered" :key="item.id" class="name-card"><span>{{ String(item.id).padStart(2, '0') }}</span><p class="arabic-name" dir="rtl">{{ item.arab }}</p><h2>{{ item.latin }}</h2><p>{{ item.indo }}</p></article><p v-if="!filtered.length" class="state">{{ text.empty }}</p></div></section>
</template>
