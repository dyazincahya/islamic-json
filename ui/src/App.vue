<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppFooter from './components/layout/AppFooter.vue'
import AppHeader from './components/layout/AppHeader.vue'
import MobileNav from './components/layout/MobileNav.vue'
import LoadingState from './components/ui/LoadingState.vue'

const localeStorageKey = 'islamic-json-locale'
const supportedLocales = ['id', 'en']
const getSavedLocale = () => {
  try {
    const savedLocale = localStorage.getItem(localeStorageKey)
    return supportedLocales.includes(savedLocale) ? savedLocale : 'id'
  } catch {
    return 'id'
  }
}

const locale = ref(getSavedLocale())
const route = useRoute()
const router = useRouter()
const activeSection = computed(() => route.meta.section ?? 'home')
const seo = {
  home: {
    id: ['Islamic JSON Explorer', "Jelajahi data Islam terbuka: Al-Qur'an, doa, dzikir, Asmaul Husna, dan rukun Islam."],
    en: ['Islamic JSON Explorer', 'Explore open Islamic data including the Qur’an, duas, dhikr, Asmaul Husna, and the pillars of Islam.'],
  },
  quran: {
    id: ['Al-Qur’an dan Terjemahan | Islamic JSON', 'Baca 114 surah Al-Qur’an lengkap dengan terjemahan Bahasa Indonesia dan tafsir Kemenag.'],
    en: ['Qur’an and Translation | Islamic JSON', 'Read all 114 Qur’an surahs with Indonesian translations and Kemenag commentary.'],
  },
  dua: {
    id: ['Kumpulan Doa Harian | Islamic JSON', 'Baca kumpulan doa sehari-hari dalam teks Arab, transliterasi, terjemahan, dan sumbernya.'],
    en: ['Daily Dua Collection | Islamic JSON', 'Read daily duas with Arabic text, transliteration, translation, and sources.'],
  },
  asmaul: {
    id: ['99 Asmaul Husna | Islamic JSON', 'Pelajari 99 nama Allah beserta tulisan Arab, transliterasi, dan artinya.'],
    en: ['99 Names of Allah | Islamic JSON', 'Explore the 99 names of Allah with Arabic text, transliteration, and meanings.'],
  },
  pillars: {
    id: ['Rukun Islam | Islamic JSON', 'Pelajari lima rukun Islam beserta niat dan panduan ibadah ringkas.'],
    en: ['Pillars of Islam | Islamic JSON', 'Learn the five pillars of Islam with intentions and concise worship guidance.'],
  },
  faith: {
    id: ['Rukun Iman | Islamic JSON', 'Pelajari enam rukun iman yang menjadi dasar keyakinan seorang Muslim.'],
    en: ['Pillars of Faith | Islamic JSON', 'Learn the six pillars of faith that form the foundation of Muslim belief.'],
  },
  library: {
    id: ['Pustaka Pengetahuan Islam | Islamic JSON', 'Jelajahi koleksi data ibadah, akidah, sejarah Islam, kalender, dan adab.'],
    en: ['Islamic Knowledge Library | Islamic JSON', 'Explore open datasets about worship, belief, Islamic history, calendars, and manners.'],
  },
  relationships: {
    id: ['Relasi Data | Islamic JSON', 'Lihat hubungan antara sumber, konsep utama, koleksi pengetahuan Islam, dan akses developer.'],
    en: ['Data Relationships | Islamic JSON', 'See how sources, core concepts, Islamic knowledge collections, and developer access relate.'],
  },
  developer: {
    id: ['API Data Islam | Islamic JSON', 'Gunakan dataset Islamic JSON melalui GitCDN Generator untuk aplikasi dan proyek Anda.'],
    en: ['Islamic Data API | Islamic JSON', 'Use Islamic JSON datasets through GitCDN Generator in your applications and projects.'],
  },
}
const text = computed(() => ({
  id: {
    eyebrow: 'Data Islam terbuka', hero: 'Satu ruang untuk menjelajahi pengetahuan Islam.', intro: 'Baca Al-Qur’an dan terjemahannya, temukan doa sehari-hari, Asmaul Husna, serta panduan ibadah dari data JSON terbuka.',
    explore: 'Mulai menjelajah', source: 'Lihat repositori', search: 'Cari dalam koleksi…', surah: 'Surah', ayah: 'Ayat', dua: 'Doa', names: 'Nama Allah', collection: 'Koleksi pilihan',
    quranDesc: 'Teks Al-Qur’an, terjemahan Bahasa Indonesia, dan tafsir Kemenag.', duaDesc: 'Doa yang menemani aktivitas sehari-hari.', asmaulDesc: '99 nama Allah beserta arti dan transliterasi.', pillarsDesc: 'Niat dan tuntunan ringkas untuk rukun Islam.', faithDesc: 'Enam dasar keyakinan yang menjadi landasan keimanan seorang Muslim.', libraryDesc: 'Jelajahi panduan ibadah, akidah, sejarah, kalender, dan adab dalam format data terbuka.', relationshipsDesc: 'Pahami hubungan antara sumber, konsep utama, koleksi pengetahuan, dan akses developer.', apiDesc: 'Akses seluruh dataset melalui GitCDN Generator untuk digunakan dalam aplikasi Anda.',
    translation: 'Terjemahan', benefit: 'Faidah', notes: 'Catatan', sourceLabel: 'Sumber', verses: 'ayat', back: 'Daftar surah', copy: 'Salin', copied: 'Tersalin', raw: 'Lihat JSON', empty: 'Data tidak ditemukan.', loading: 'Memuat data…',
  },
  en: {
    eyebrow: 'Open Islamic data', hero: 'One place to explore Islamic knowledge.', intro: 'Read the Qur’an and its translation, discover daily duas, the Beautiful Names, and worship guides from open JSON data.',
    explore: 'Start exploring', source: 'View repository', search: 'Search this collection…', surah: 'Surahs', ayah: 'Ayahs', dua: 'Duas', names: 'Names of Allah', collection: 'Curated collections',
    quranDesc: 'Qur’an text, Indonesian translation, and Kemenag tafsir.', duaDesc: 'Supplications for everyday moments.', asmaulDesc: 'The 99 names of Allah with meanings and transliterations.', pillarsDesc: 'Intentions and concise guidance for the pillars of Islam.', faithDesc: 'The six fundamental beliefs that form the foundation of a Muslim’s faith.', libraryDesc: 'Explore worship guides, beliefs, history, calendar, and manners as open data.', relationshipsDesc: 'Understand how sources, core concepts, knowledge collections, and developer access relate.', apiDesc: 'Access every dataset through GitCDN Generator for use in your application.',
    translation: 'Translation', benefit: 'Benefit', notes: 'Notes', sourceLabel: 'Source', verses: 'ayahs', back: 'Surah list', copy: 'Copy', copied: 'Copied', raw: 'View JSON', empty: 'No data found.', loading: 'Loading data…',
  },
}[locale.value]))

function setMetaContent(selector, content) {
  document.head.querySelector(selector)?.setAttribute('content', content)
}

watch([activeSection, locale], ([section, value]) => {
  const [title, description] = seo[section]?.[value] ?? seo.home[value]
  document.documentElement.lang = value
  document.title = title
  setMetaContent('meta[name="description"]', description)
  setMetaContent('meta[property="og:title"]', title)
  setMetaContent('meta[property="og:description"]', description)
  setMetaContent('meta[property="og:locale"]', value === 'id' ? 'id_ID' : 'en_US')
  setMetaContent('meta[name="twitter:title"]', title)
  setMetaContent('meta[name="twitter:description"]', description)
  try {
    localStorage.setItem(localeStorageKey, value)
  } catch {
    // The interface still works when browser storage is unavailable.
  }
}, { immediate: true })

function navigate(section) {
  router.push({ name: section })
}
</script>

<template>
  <div class="app-shell">
    <AppHeader v-model:locale="locale" :active-section="activeSection" @navigate="navigate" />
    <main>
      <RouterView v-slot="{ Component }">
        <Suspense>
          <component :is="Component" :locale="locale" :text="text" @navigate="navigate" />
          <template #fallback><LoadingState :label="text.loading" /></template>
        </Suspense>
      </RouterView>
    </main>
    <MobileNav :active-section="activeSection" :locale="locale" @navigate="navigate" />
    <AppFooter />
  </div>
</template>
