<script setup>
import { computed, ref } from 'vue'
import { getSurah, getSurahList, rawUrl } from '../../data'
import PageHero from '../layout/PageHero.vue'

const props = defineProps({ locale: String, text: Object })
const query = ref('')
const selectedNumber = ref(null)
const selectedSurah = ref(null)
const loading = ref(false)
const copied = ref('')
const surahs = getSurahList()
const filtered = computed(() => {
  const needle = query.value.toLocaleLowerCase()
  return surahs.filter((item) => [item.id, item.latin, item.transliteration, item.translation, item.arabic].some((value) => String(value ?? '').toLocaleLowerCase().includes(needle)))
})

async function openSurah(number) {
  selectedNumber.value = number
  selectedSurah.value = null
  loading.value = true
  try { selectedSurah.value = await getSurah(number) } finally { loading.value = false }
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
async function copyAyah(arabic, translation, number) {
  await navigator.clipboard.writeText(`${arabic}\n${translation}`)
  copied.value = number
  window.setTimeout(() => { copied.value = '' }, 1600)
}
function closeSurah() { selectedNumber.value = null; selectedSurah.value = null }
</script>

<template>
  <PageHero title="Al-Qur’an" :description="text.quranDesc" />
  <section class="browser section-wrap">
    <div v-if="!selectedNumber" class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ filtered.length }} {{ locale === 'id' ? 'item' : 'items' }}</span></div>
    <div v-if="selectedNumber" class="surah-reader">
      <button class="back-button" @click="closeSurah">← {{ text.back }}</button><p v-if="loading" class="state">{{ text.loading }}</p>
      <template v-else-if="selectedSurah">
        <header class="surah-header"><div><span>{{ selectedSurah.number }}</span><h2>{{ selectedSurah.name_latin }}</h2><p>{{ selectedSurah.translations.id.name }} · {{ selectedSurah.number_of_ayah }} {{ text.verses }}</p></div><strong dir="rtl">{{ selectedSurah.name }}</strong><a :href="rawUrl(`holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${selectedNumber}.json`)" target="_blank">{{ text.raw }} ↗</a></header>
        <article v-for="(arabic, number) in selectedSurah.text" :key="number" class="ayah-card"><div class="ayah-meta"><span>{{ selectedNumber }}:{{ number }}</span><button @click="copyAyah(arabic, selectedSurah.translations.id.text[number], number)">{{ copied === number ? text.copied : text.copy }}</button></div><p class="arabic-text" dir="rtl">{{ arabic }} <i>﴿{{ number }}﴾</i></p><p class="translation-text">{{ selectedSurah.translations.id.text[number] }}</p></article>
      </template>
    </div>
    <div v-else class="surah-grid"><button v-for="surah in filtered" :key="surah.id" class="surah-item" @click="openSurah(surah.id)"><span class="number-badge">{{ surah.id }}</span><div><h3>{{ surah.transliteration }}</h3><p>{{ surah.translation }} · {{ surah.num_ayah }} {{ text.verses }}</p></div><strong dir="rtl">{{ surah.arabic }}</strong></button></div>
  </section>
</template>
