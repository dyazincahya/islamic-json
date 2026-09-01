<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import {
  getAsmaulHusna,
  getDua,
  getPillars,
  getSurah,
  getSurahList,
  localized,
  rawUrl,
  repositoryUrl,
  sections,
  stats,
} from './data'

const locale = ref('id')
const activeSection = ref('home')
const query = ref('')
const pillars = ref([])
const pillarsLoading = ref(false)
const selectedSurahNumber = ref(null)
const selectedSurah = ref(null)
const surahLoading = ref(false)
const copied = ref('')

const text = computed(() => ({
  id: {
    eyebrow: 'Data Islam terbuka', hero: 'Satu ruang untuk menjelajahi pengetahuan Islam.',
    intro: 'Baca Al-Qur’an dan terjemahannya, temukan doa sehari-hari, Asmaul Husna, serta panduan ibadah dari data JSON terbuka.',
    explore: 'Mulai menjelajah', source: 'Lihat repositori', search: 'Cari dalam koleksi…', all: 'Semua',
    surah: 'Surah', ayah: 'Ayat', dua: 'Doa', names: 'Nama Allah', collection: 'Koleksi pilihan',
    quranDesc: 'Teks Al-Qur’an, terjemahan Bahasa Indonesia, dan tafsir Kemenag.',
    duaDesc: 'Doa yang menemani aktivitas sehari-hari.', asmaulDesc: '99 nama Allah beserta arti dan transliterasi.',
    pillarsDesc: 'Niat dan tuntunan ringkas untuk rukun Islam.', translation: 'Terjemahan', benefit: 'Faidah', notes: 'Catatan', sourceLabel: 'Sumber',
    selectSurah: 'Pilih surah untuk mulai membaca', verses: 'ayat', back: 'Daftar surah', copy: 'Salin', copied: 'Tersalin', raw: 'Lihat JSON', empty: 'Data tidak ditemukan.', loading: 'Memuat data…',
  },
  en: {
    eyebrow: 'Open Islamic data', hero: 'One place to explore Islamic knowledge.',
    intro: 'Read the Qur’an and its translation, discover daily duas, the Beautiful Names, and worship guides from open JSON data.',
    explore: 'Start exploring', source: 'View repository', search: 'Search this collection…', all: 'All',
    surah: 'Surahs', ayah: 'Ayahs', dua: 'Duas', names: 'Names of Allah', collection: 'Curated collections',
    quranDesc: 'Qur’an text, Indonesian translation, and Kemenag tafsir.',
    duaDesc: 'Supplications for everyday moments.', asmaulDesc: 'The 99 names of Allah with meanings and transliterations.',
    pillarsDesc: 'Intentions and concise guidance for the pillars of Islam.', translation: 'Translation', benefit: 'Benefit', notes: 'Notes', sourceLabel: 'Source',
    selectSurah: 'Select a surah to start reading', verses: 'ayahs', back: 'Surah list', copy: 'Copy', copied: 'Copied', raw: 'View JSON', empty: 'No data found.', loading: 'Loading data…',
  },
}[locale.value]))

const dua = getDua()
const asmaul = getAsmaulHusna()
const surahList = getSurahList()
const normalize = (value) => String(value ?? '').toLocaleLowerCase()
const matches = (...values) => values.some((value) => normalize(value).includes(normalize(query.value)))

const filteredDua = computed(() => dua.filter((item) => matches(item.title, item.translation, item.latin, item.arabic)))
const filteredAsmaul = computed(() => asmaul.filter((item) => matches(item.latin, item.indo, item.arab)))
const filteredSurah = computed(() => surahList.filter((item) => matches(item.id, item.latin, item.transliteration, item.translation, item.arabic)))
const filteredPillars = computed(() => pillars.value.filter((item) => matches(localized(item.title, locale.value), localized(item.content?.translation, locale.value), localized(item.content?.context, locale.value), item.category)))
const categories = computed(() => [...new Set(pillars.value.map((item) => item.category))])

function navigate(section) {
  activeSection.value = section
  query.value = ''
  if (section !== 'quran') selectedSurahNumber.value = null
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function openSurah(number) {
  selectedSurahNumber.value = number
  selectedSurah.value = null
  surahLoading.value = true
  try { selectedSurah.value = await getSurah(number) } finally { surahLoading.value = false }
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function copyText(value, key) {
  await navigator.clipboard.writeText(value)
  copied.value = key
  window.setTimeout(() => { copied.value = '' }, 1600)
}

watch(activeSection, async (section) => {
  if (section === 'pillars' && !pillars.value.length) {
    pillarsLoading.value = true
    try { pillars.value = await getPillars() } finally { pillarsLoading.value = false }
  }
})

onMounted(() => {
  const hash = window.location.hash.slice(1)
  if (sections.some((item) => item.id === hash)) activeSection.value = hash
})
</script>

<template>
  <div class="app-shell">
    <header class="site-header">
      <button class="brand" aria-label="Islamic JSON home" @click="navigate('home')">
        <span class="brand-mark">ا</span><span>Islamic <b>JSON</b></span>
      </button>
      <nav class="desktop-nav" aria-label="Main navigation">
        <button v-for="item in sections" :key="item.id" :class="{ active: activeSection === item.id }" @click="navigate(item.id)">{{ localized(item.label, locale) }}</button>
      </nav>
      <div class="header-actions">
        <div class="locale-switch" aria-label="Language">
          <button :class="{ active: locale === 'id' }" @click="locale = 'id'">ID</button>
          <button :class="{ active: locale === 'en' }" @click="locale = 'en'">EN</button>
        </div>
        <a class="github-link" :href="repositoryUrl" target="_blank" rel="noreferrer" aria-label="GitHub">↗</a>
      </div>
    </header>

    <main>
      <template v-if="activeSection === 'home'">
        <section class="hero">
          <div class="hero-copy">
            <p class="eyebrow"><span></span>{{ text.eyebrow }}</p>
            <h1>{{ text.hero }}</h1>
            <p class="hero-intro">{{ text.intro }}</p>
            <div class="hero-actions">
              <button class="primary-button" @click="navigate('quran')">{{ text.explore }} <span>→</span></button>
              <a class="text-link" :href="repositoryUrl" target="_blank" rel="noreferrer">{{ text.source }} ↗</a>
            </div>
          </div>
          <div class="hero-art" aria-hidden="true">
            <div class="arch"><div class="quran-mark">اقْرَأْ</div><div class="ornament">✦</div><p>Bacalah dengan nama Tuhanmu</p></div>
          </div>
        </section>

        <section class="stats-grid" aria-label="Dataset statistics">
          <div><strong>{{ stats.surah }}</strong><span>{{ text.surah }}</span></div>
          <div><strong>{{ stats.ayah.toLocaleString('id-ID') }}</strong><span>{{ text.ayah }}</span></div>
          <div><strong>{{ stats.dua }}</strong><span>{{ text.dua }}</span></div>
          <div><strong>{{ stats.asmaul }}</strong><span>{{ text.names }}</span></div>
        </section>

        <section class="collections section-wrap">
          <div class="section-heading"><p class="eyebrow"><span></span>{{ text.collection }}</p><h2>{{ locale === 'id' ? 'Jelajahi berdasarkan topik' : 'Explore by topic' }}</h2></div>
          <div class="collection-grid">
            <button class="collection-card quran-card" @click="navigate('quran')"><span class="card-icon">۞</span><div><h3>Al-Qur’an</h3><p>{{ text.quranDesc }}</p><small>{{ stats.surah }} {{ text.surah }} · {{ stats.ayah.toLocaleString('id-ID') }} {{ text.ayah }}</small></div><b>→</b></button>
            <button class="collection-card" @click="navigate('dua')"><span class="card-icon">☾</span><div><h3>{{ localized(sections[2].label, locale) }}</h3><p>{{ text.duaDesc }}</p><small>{{ stats.dua }} {{ text.dua }}</small></div><b>→</b></button>
            <button class="collection-card" @click="navigate('asmaul')"><span class="card-icon">◈</span><div><h3>Asmaul Husna</h3><p>{{ text.asmaulDesc }}</p><small>99 {{ text.names }}</small></div><b>→</b></button>
            <button class="collection-card" @click="navigate('pillars')"><span class="card-icon">◆</span><div><h3>{{ localized(sections[4].label, locale) }}</h3><p>{{ text.pillarsDesc }}</p><small>5 {{ locale === 'id' ? 'pilar' : 'pillars' }}</small></div><b>→</b></button>
          </div>
        </section>
      </template>

      <template v-else>
        <section class="page-hero">
          <p class="eyebrow"><span></span>Islamic JSON</p>
          <h1>{{ localized(sections.find((item) => item.id === activeSection)?.label, locale) }}</h1>
          <p>{{ activeSection === 'quran' ? text.quranDesc : activeSection === 'dua' ? text.duaDesc : activeSection === 'asmaul' ? text.asmaulDesc : text.pillarsDesc }}</p>
        </section>

        <section class="browser section-wrap">
          <div v-if="!(activeSection === 'quran' && selectedSurahNumber)" class="toolbar">
            <label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label>
            <span class="result-count">{{ activeSection === 'quran' ? filteredSurah.length : activeSection === 'dua' ? filteredDua.length : activeSection === 'asmaul' ? filteredAsmaul.length : filteredPillars.length }} {{ locale === 'id' ? 'item' : 'items' }}</span>
          </div>

          <div v-if="activeSection === 'quran'">
            <div v-if="selectedSurahNumber" class="surah-reader">
              <button class="back-button" @click="selectedSurahNumber = null; selectedSurah = null">← {{ text.back }}</button>
              <p v-if="surahLoading" class="state">{{ text.loading }}</p>
              <template v-else-if="selectedSurah">
                <header class="surah-header"><div><span>{{ selectedSurah.number }}</span><h2>{{ selectedSurah.name_latin }}</h2><p>{{ selectedSurah.translations.id.name }} · {{ selectedSurah.number_of_ayah }} {{ text.verses }}</p></div><strong dir="rtl">{{ selectedSurah.name }}</strong><a :href="rawUrl(`holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${selectedSurahNumber}.json`)" target="_blank">{{ text.raw }} ↗</a></header>
                <article v-for="(arabic, number) in selectedSurah.text" :key="number" class="ayah-card">
                  <div class="ayah-meta"><span>{{ selectedSurahNumber }}:{{ number }}</span><button @click="copyText(`${arabic}\n${selectedSurah.translations.id.text[number]}`, `ayah-${number}`)">{{ copied === `ayah-${number}` ? text.copied : text.copy }}</button></div>
                  <p class="arabic-text" dir="rtl">{{ arabic }} <i>﴿{{ number }}﴾</i></p>
                  <p class="translation-text">{{ selectedSurah.translations.id.text[number] }}</p>
                </article>
              </template>
            </div>
            <div v-else class="surah-grid">
              <button v-for="surah in filteredSurah" :key="surah.id" class="surah-item" @click="openSurah(surah.id)"><span class="number-badge">{{ surah.id }}</span><div><h3>{{ surah.transliteration }}</h3><p>{{ surah.translation }} · {{ surah.num_ayah }} {{ text.verses }}</p></div><strong dir="rtl">{{ surah.arabic }}</strong></button>
            </div>
          </div>

          <div v-else-if="activeSection === 'dua'" class="content-grid">
            <article v-for="(item, index) in filteredDua" :key="item.title" class="content-card">
              <div class="card-top"><span>{{ String(index + 1).padStart(2, '0') }}</span><button @click="copyText(`${item.arabic}\n${item.translation}`, `dua-${index}`)">{{ copied === `dua-${index}` ? text.copied : text.copy }}</button></div>
              <h2>{{ item.title }}</h2><p class="arabic-text compact" dir="rtl">{{ item.arabic }}</p><p class="latin-text">{{ item.latin }}</p>
              <div class="translation-block"><small>{{ text.translation }}</small><p>{{ item.translation }}</p></div>
              <details v-if="item.fawaid || item.notes"><summary>{{ text.benefit }} & {{ text.notes }}</summary><p>{{ item.fawaid || item.notes }}</p></details>
              <footer v-if="item.source">{{ text.sourceLabel }}: {{ item.source }}</footer>
            </article>
            <p v-if="!filteredDua.length" class="state">{{ text.empty }}</p>
          </div>

          <div v-else-if="activeSection === 'asmaul'" class="asmaul-grid">
            <article v-for="item in filteredAsmaul" :key="item.id" class="name-card"><span>{{ String(item.id).padStart(2, '0') }}</span><p class="arabic-name" dir="rtl">{{ item.arab }}</p><h2>{{ item.latin }}</h2><p>{{ item.indo }}</p></article>
            <p v-if="!filteredAsmaul.length" class="state">{{ text.empty }}</p>
          </div>

          <div v-else-if="activeSection === 'pillars'">
            <p v-if="pillarsLoading" class="state">{{ text.loading }}</p>
            <template v-else>
              <section v-for="category in categories" :key="category" class="pillar-group">
                <div class="group-title"><span>{{ category }}</span><div></div></div>
                <div class="content-grid">
                  <article v-for="item in filteredPillars.filter((record) => record.category === category)" :key="item.key" class="content-card pillar-card">
                    <div class="card-top"><span>◆</span><a :href="rawUrl(item.path)" target="_blank" rel="noreferrer">JSON ↗</a></div><h2>{{ localized(item.title, locale) }}</h2>
                    <p v-if="item.content?.arrabic" class="arabic-text compact" dir="rtl">{{ item.content.arrabic }}</p><p v-if="item.content?.latin" class="latin-text">{{ item.content.latin }}</p>
                    <div v-if="localized(item.content?.translation, locale) || localized(item.content?.context, locale)" class="translation-block"><small>{{ text.translation }}</small><p>{{ localized(item.content?.translation, locale) || localized(item.content?.context, locale) }}</p></div>
                    <div v-if="localized(item.content?.extras, locale)" class="extras" v-html="localized(item.content.extras, locale)"></div>
                  </article>
                </div>
              </section>
              <p v-if="!filteredPillars.length" class="state">{{ text.empty }}</p>
            </template>
          </div>
        </section>
      </template>
    </main>

    <nav class="mobile-nav" aria-label="Mobile navigation"><button v-for="item in sections" :key="item.id" :class="{ active: activeSection === item.id }" @click="navigate(item.id)"><span>{{ item.icon }}</span>{{ localized(item.label, locale) }}</button></nav>
    <footer class="site-footer"><div class="brand"><span class="brand-mark">ا</span><span>Islamic <b>JSON</b></span></div><p>Open data, built for the ummah.</p><a :href="repositoryUrl" target="_blank" rel="noreferrer">GitHub ↗</a></footer>
  </div>
</template>
