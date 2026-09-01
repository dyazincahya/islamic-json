<script setup>
import { computed, onMounted, ref } from 'vue'
import AsmaulHusnaView from './components/asmaul-husna/AsmaulHusnaView.vue'
import DuaView from './components/dua/DuaView.vue'
import HomeView from './components/home/HomeView.vue'
import AppFooter from './components/layout/AppFooter.vue'
import AppHeader from './components/layout/AppHeader.vue'
import MobileNav from './components/layout/MobileNav.vue'
import PillarsView from './components/pillars/PillarsView.vue'
import QuranView from './components/quran/QuranView.vue'
import { sections } from './data'

const locale = ref('id')
const activeSection = ref('home')
const text = computed(() => ({
  id: {
    eyebrow: 'Data Islam terbuka', hero: 'Satu ruang untuk menjelajahi pengetahuan Islam.', intro: 'Baca Al-Qur’an dan terjemahannya, temukan doa sehari-hari, Asmaul Husna, serta panduan ibadah dari data JSON terbuka.',
    explore: 'Mulai menjelajah', source: 'Lihat repositori', search: 'Cari dalam koleksi…', surah: 'Surah', ayah: 'Ayat', dua: 'Doa', names: 'Nama Allah', collection: 'Koleksi pilihan',
    quranDesc: 'Teks Al-Qur’an, terjemahan Bahasa Indonesia, dan tafsir Kemenag.', duaDesc: 'Doa yang menemani aktivitas sehari-hari.', asmaulDesc: '99 nama Allah beserta arti dan transliterasi.', pillarsDesc: 'Niat dan tuntunan ringkas untuk rukun Islam.',
    translation: 'Terjemahan', benefit: 'Faidah', notes: 'Catatan', sourceLabel: 'Sumber', verses: 'ayat', back: 'Daftar surah', copy: 'Salin', copied: 'Tersalin', raw: 'Lihat JSON', empty: 'Data tidak ditemukan.', loading: 'Memuat data…',
  },
  en: {
    eyebrow: 'Open Islamic data', hero: 'One place to explore Islamic knowledge.', intro: 'Read the Qur’an and its translation, discover daily duas, the Beautiful Names, and worship guides from open JSON data.',
    explore: 'Start exploring', source: 'View repository', search: 'Search this collection…', surah: 'Surahs', ayah: 'Ayahs', dua: 'Duas', names: 'Names of Allah', collection: 'Curated collections',
    quranDesc: 'Qur’an text, Indonesian translation, and Kemenag tafsir.', duaDesc: 'Supplications for everyday moments.', asmaulDesc: 'The 99 names of Allah with meanings and transliterations.', pillarsDesc: 'Intentions and concise guidance for the pillars of Islam.',
    translation: 'Translation', benefit: 'Benefit', notes: 'Notes', sourceLabel: 'Source', verses: 'ayahs', back: 'Surah list', copy: 'Copy', copied: 'Copied', raw: 'View JSON', empty: 'No data found.', loading: 'Loading data…',
  },
}[locale.value]))

function navigate(section) {
  activeSection.value = section
  window.location.hash = section === 'home' ? '' : section
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  const hash = window.location.hash.slice(1)
  if (sections.some((item) => item.id === hash)) activeSection.value = hash
})
</script>

<template>
  <div class="app-shell">
    <AppHeader v-model:locale="locale" :active-section="activeSection" @navigate="navigate" />
    <main>
      <HomeView v-if="activeSection === 'home'" :locale="locale" :text="text" @navigate="navigate" />
      <QuranView v-else-if="activeSection === 'quran'" :locale="locale" :text="text" />
      <DuaView v-else-if="activeSection === 'dua'" :locale="locale" :text="text" />
      <AsmaulHusnaView v-else-if="activeSection === 'asmaul'" :locale="locale" :text="text" />
      <PillarsView v-else-if="activeSection === 'pillars'" :locale="locale" :text="text" />
    </main>
    <MobileNav :active-section="activeSection" :locale="locale" @navigate="navigate" />
    <AppFooter />
  </div>
</template>
