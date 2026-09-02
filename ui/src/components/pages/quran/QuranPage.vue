<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getSurah, getSurahList } from '../../../data'
import ApiButton from '../../ui/ApiButton.vue'
import LoadingState from '../../ui/LoadingState.vue'
import PageHero from '../../layout/PageHero.vue'

const props = defineProps({ locale: String, text: Object })
const route = useRoute()
const router = useRouter()
const query = ref('')
const selectedNumber = ref(null)
const selectedSurah = ref(null)
const loading = ref(false)
const loadError = ref('')
const copied = ref('')
const surahs = getSurahList()
const filtered = computed(() => {
  const needle = query.value.toLocaleLowerCase()
  return surahs.filter((item) => [item.id, item.latin, item.transliteration, item.translation, item.arabic].some((value) => String(value ?? '').toLocaleLowerCase().includes(needle)))
})

async function loadSurah(number) {
  selectedNumber.value = number
  selectedSurah.value = null
  loadError.value = ''
  loading.value = true
  try {
    selectedSurah.value = await getSurah(number)
  } catch (error) {
    console.error('Failed to load surah', error)
    loadError.value = props.locale === 'id' ? 'Data surah gagal dimuat. Silakan coba lagi.' : 'The surah could not be loaded. Please try again.'
  } finally {
    loading.value = false
  }
}
function openSurah(number) {
  router.push({ name: 'quran', params: { surah: number } })
}
async function copyAyah(arabic, translation, number) {
  await navigator.clipboard.writeText(`${arabic}\n${translation}`)
  copied.value = number
  window.setTimeout(() => { copied.value = '' }, 1600)
}
function closeSurah() { router.push({ name: 'quran' }) }
watch(
  () => route.params.surah,
  (number) => {
    if (number) loadSurah(Number(number))
    else {
      selectedNumber.value = null
      selectedSurah.value = null
      loadError.value = ''
    }
  },
  { immediate: true },
)
</script>

<template>
  <PageHero title="Al-Qur’an" :description="text.quranDesc" api-path="holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah.json" />
  <section class="browser section-wrap">
    <div v-if="!selectedNumber" class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ filtered.length }} {{ locale === 'id' ? 'item' : 'items' }}</span></div>
    <div v-if="selectedNumber" class="surah-reader">
      <button class="back-button" @click="closeSurah">← {{ text.back }}</button><LoadingState v-if="loading" :label="text.loading" />
      <div v-else-if="loadError" class="load-error"><p>{{ loadError }}</p><button class="primary-button" @click="loadSurah(selectedNumber)">{{ locale === 'id' ? 'Coba lagi' : 'Try again' }}</button></div>
      <template v-else-if="selectedSurah">
        <header class="surah-header"><div><span>{{ selectedSurah.number }}</span><h2>{{ selectedSurah.name_latin }}</h2><p>{{ selectedSurah.translations.id.name }} · {{ selectedSurah.number_of_ayah }} {{ text.verses }}</p></div><strong dir="rtl">{{ selectedSurah.name }}</strong><ApiButton :source="`holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${selectedNumber}.json`" compact /></header>
        <article v-for="(arabic, number) in selectedSurah.text" :key="number" class="ayah-card"><div class="ayah-meta"><span>{{ selectedNumber }}:{{ number }}</span><button @click="copyAyah(arabic, selectedSurah.translations.id.text[number], number)">{{ copied === number ? text.copied : text.copy }}</button></div><p class="arabic-text" dir="rtl">{{ arabic }} <i>﴿{{ number }}﴾</i></p><p class="translation-text">{{ selectedSurah.translations.id.text[number] }}</p></article>
      </template>
    </div>
    <div v-else class="surah-grid"><button v-for="surah in filtered" :key="surah.id" class="surah-item" @click="openSurah(surah.id)"><span class="number-badge">{{ surah.id }}</span><div><h3>{{ surah.transliteration }}</h3><p>{{ surah.translation }} · {{ surah.num_ayah }} {{ text.verses }}</p></div><strong dir="rtl">{{ surah.arabic }}</strong></button></div>
  </section>
</template>
