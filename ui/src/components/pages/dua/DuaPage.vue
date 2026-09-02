<script setup>
import { computed, ref } from 'vue'
import { getDua } from '../../../data'
import PageHero from '../../layout/PageHero.vue'

const props = defineProps({ locale: String, text: Object })
const query = ref('')
const copied = ref('')
const dua = getDua()
const filtered = computed(() => { const needle = query.value.toLocaleLowerCase(); return dua.filter((item) => [item.title, item.translation, item.latin, item.arabic].some((value) => String(value ?? '').toLocaleLowerCase().includes(needle))) })
async function copyDua(item, index) { await navigator.clipboard.writeText(`${item.arabic}\n${item.translation}`); copied.value = index; window.setTimeout(() => { copied.value = '' }, 1600) }
</script>

<template>
  <PageHero :title="locale === 'id' ? 'Doa Harian' : 'Daily Dua'" :description="text.duaDesc" api-path="dua/data/daily-dua.json" />
  <section class="browser section-wrap">
    <div class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ filtered.length }} {{ locale === 'id' ? 'item' : 'items' }}</span></div>
    <div class="content-grid"><article v-for="(item, index) in filtered" :key="item.title" class="content-card"><div class="card-top"><span>{{ String(index + 1).padStart(2, '0') }}</span><button @click="copyDua(item, index)">{{ copied === index ? text.copied : text.copy }}</button></div><h2>{{ item.title }}</h2><p class="arabic-text compact" dir="rtl">{{ item.arabic }}</p><p class="latin-text">{{ item.latin }}</p><div class="translation-block"><small>{{ text.translation }}</small><p>{{ item.translation }}</p></div><details v-if="item.fawaid || item.notes"><summary>{{ text.benefit }} & {{ text.notes }}</summary><p>{{ item.fawaid || item.notes }}</p></details><footer v-if="item.source">{{ text.sourceLabel }}: {{ item.source }}</footer></article><p v-if="!filtered.length" class="state">{{ text.empty }}</p></div>
  </section>
</template>
