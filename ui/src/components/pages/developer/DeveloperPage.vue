<script setup>
import { computed, onMounted, ref } from 'vue'
import { getPillars, getSurahList, knowledgeCollections, localized } from '../../../data'
import PageHero from '../../layout/PageHero.vue'
import ApiButton from '../../ui/ApiButton.vue'
import LoadingState from '../../ui/LoadingState.vue'

const props = defineProps({ locale: String, text: Object })
const query = ref('')
const pillarFiles = ref([])
const loading = ref(true)
const surahs = getSurahList()
const coreFiles = [
  { name: 'Asmaul Husna', path: 'asmaul-husna/asmaul-husna.json', detail: '99 names' },
  { name: 'Daily Dua', path: 'dua/data/daily-dua.json', detail: '55 duas' },
  { name: 'Qur’an Surah Index', path: 'holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah.json', detail: '114 surahs' },
  { name: 'Pillars of Faith', path: 'pillars-of-faith/main.json', detail: '6 pillars' },
]
const matches = (item) => `${item.name} ${item.path} ${item.detail ?? ''}`.toLocaleLowerCase().includes(query.value.toLocaleLowerCase())
const knowledgeFiles = computed(() => knowledgeCollections.flatMap((collection) => collection.files.map((file) => ({ name: localized(file.title, props.locale), detail: localized(collection.title, props.locale), path: file.path }))))
const filteredCore = computed(() => coreFiles.filter(matches))
const filteredKnowledge = computed(() => knowledgeFiles.value.filter(matches))
const filteredPillars = computed(() => pillarFiles.value.filter(matches))
const filteredSurahs = computed(() => surahs.map((surah) => ({ name: `${surah.id}. ${surah.transliteration}`, detail: `${surah.translation} · ${surah.num_ayah} ayat`, path: `holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${surah.id}.json` })).filter(matches))
const resultCount = computed(() => filteredCore.value.length + filteredKnowledge.value.length + filteredPillars.value.length + filteredSurahs.value.length)

onMounted(async () => {
  try {
    const pillars = await getPillars()
    const uniquePaths = [...new Map(pillars.map((item) => [item.path, item])).values()]
    pillarFiles.value = uniquePaths.map((item) => ({ name: item.title.id, detail: item.category, path: item.path }))
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <PageHero title="Developer API" :description="text.apiDesc" />
  <section class="browser section-wrap developer-browser">
    <div class="developer-notice"><font-awesome-icon icon="code" /><div><strong>GitCDN Generator</strong><p>{{ locale === 'id' ? 'Setiap tombol API membuka GitCDN Generator dengan URL file GitHub yang sudah terisi.' : 'Every API button opens GitCDN Generator with the GitHub file URL pre-filled.' }}</p></div></div>
    <RouterLink class="relationship-link" :to="{ name: 'relationships' }"><span><font-awesome-icon icon="diagram-project" /></span><div><strong>{{ locale === 'id' ? 'Lihat Relasi Data' : 'View Data Relationships' }}</strong><small>{{ locale === 'id' ? 'Pelajari keterkaitan antar-dataset melalui diagram Mermaid.' : 'Explore dataset connections through a Mermaid diagram.' }}</small></div><b>→</b></RouterLink>
    <div class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="locale === 'id' ? 'Cari endpoint atau path…' : 'Search endpoint or path…'" /></label><span class="result-count">{{ resultCount }} endpoints</span></div>
        <LoadingState v-if="loading" :label="text.loading" compact />

    <section v-if="filteredCore.length" class="api-group"><div class="group-title"><span>{{ locale === 'id' ? 'Dataset utama' : 'Core datasets' }}</span><div></div></div><div class="api-list"><article v-for="item in filteredCore" :key="item.path" class="api-row"><div><h2>{{ item.name }}</h2><p>{{ item.detail }}</p><code>{{ item.path }}</code></div><ApiButton :source="item.path" /></article></div></section>
    <section v-if="filteredKnowledge.length" class="api-group"><div class="group-title"><span>{{ locale === 'id' ? 'Pustaka Islam' : 'Islamic Library' }}</span><div></div></div><div class="api-list"><article v-for="item in filteredKnowledge" :key="item.path" class="api-row"><div><h2>{{ item.name }}</h2><p>{{ item.detail }}</p><code>{{ item.path }}</code></div><ApiButton :source="item.path" /></article></div></section>
    <section v-if="filteredPillars.length" class="api-group"><div class="group-title"><span>{{ locale === 'id' ? 'Rukun Islam' : 'Pillars of Islam' }}</span><div></div></div><div class="api-list"><article v-for="item in filteredPillars" :key="item.path" class="api-row"><div><h2>{{ item.name }}</h2><p class="api-category">{{ item.detail }}</p><code>{{ item.path }}</code></div><ApiButton :source="item.path" /></article></div></section>
    <section v-if="filteredSurahs.length" class="api-group"><div class="group-title"><span>Al-Qur’an</span><div></div></div><div class="api-list"><article v-for="item in filteredSurahs" :key="item.path" class="api-row"><div><h2>{{ item.name }}</h2><p>{{ item.detail }}</p><code>{{ item.path }}</code></div><ApiButton :source="item.path" /></article></div></section>
    <p v-if="!resultCount" class="state">{{ text.empty }}</p>
  </section>
</template>
