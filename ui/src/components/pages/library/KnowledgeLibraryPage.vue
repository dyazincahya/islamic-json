<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getKnowledgeFile, knowledgeCollections, localized } from '../../../data'
import PageHero from '../../layout/PageHero.vue'
import ApiButton from '../../ui/ApiButton.vue'
import LoadingState from '../../ui/LoadingState.vue'

const props = defineProps({ locale: String, text: Object })
const route = useRoute()
const router = useRouter()
const query = ref('')
const data = ref(null)
const loading = ref(false)
const loadError = ref('')
const collection = computed(() => knowledgeCollections.find((item) => item.id === route.params.collection))
const file = computed(() => collection.value?.files.find((item) => item.id === route.params.file) ?? collection.value?.files[0])

const groups = computed(() => {
  if (!data.value) return []
  if (Array.isArray(data.value)) return [{ id: file.value?.id, title: file.value?.title, items: data.value }]
  if (Array.isArray(data.value.items)) return [{ id: data.value.id, title: data.value.title, items: data.value.items }]
  return Object.entries(data.value)
    .filter(([key, value]) => key !== 'sources' && Array.isArray(value))
    .map(([key, items]) => ({ id: key, title: { id: groupLabel(key, 'id'), en: groupLabel(key, 'en') }, items }))
})
const filteredGroups = computed(() => {
  const needle = query.value.toLocaleLowerCase()
  return groups.value.map((group) => ({
    ...group,
    items: group.items.filter((item) => `${item.id ?? ''} ${localized(item.title ?? item.name, props.locale)} ${localized(item.description ?? item.context, props.locale)} ${item.type ?? ''} ${item.category ?? ''}`.toLocaleLowerCase().includes(needle)),
  })).filter((group) => group.items.length)
})
const resultCount = computed(() => filteredGroups.value.reduce((total, group) => total + group.items.length, 0))

function groupLabel(key, locale) {
  const labels = { months: { id: 'Bulan Hijriah', en: 'Hijri Months' }, events: { id: 'Peristiwa Penting', en: 'Important Occasions' }, categories: { id: 'Kategori', en: 'Categories' } }
  return labels[key]?.[locale] ?? key.replaceAll('-', ' ')
}
function openCollection(id) {
  router.push({ name: 'library', params: { collection: id } })
}
function openFile(id) {
  router.push({ name: 'library', params: { collection: collection.value.id, file: id } })
}
function itemArabic(item) {
  return item.content?.arabic ?? item.title?.ar ?? item.name?.ar ?? ''
}
function itemDescription(item) {
  return localized(item.description ?? item.context ?? item.content?.translation, props.locale)
}
function sourceText(source) {
  if (typeof source === 'string') return source
  return source.reference ?? source.verses?.join(', ') ?? source.source_id ?? source.id ?? ''
}

watch(
  () => file.value?.path,
  async (path) => {
    query.value = ''
    data.value = null
    loadError.value = ''
    if (!path) return
    loading.value = true
    try {
      data.value = await getKnowledgeFile(path)
    } catch (error) {
      console.error('Failed to load knowledge file', error)
      loadError.value = props.locale === 'id' ? 'Data gagal dimuat. Silakan coba kembali.' : 'The data could not be loaded. Please try again.'
    } finally {
      loading.value = false
    }
  },
  { immediate: true },
)
</script>

<template>
  <PageHero :title="locale === 'id' ? 'Pustaka Islam' : 'Islamic Library'" :description="text.libraryDesc" :api-path="file?.path" />
  <section class="browser section-wrap knowledge-browser">
    <template v-if="!collection">
      <div class="section-heading"><p class="eyebrow"><span></span>{{ locale === 'id' ? 'Koleksi data' : 'Data collections' }}</p><h2>{{ locale === 'id' ? 'Pilih topik untuk dipelajari' : 'Choose a topic to explore' }}</h2></div>
      <div class="knowledge-grid">
        <button v-for="item in knowledgeCollections" :key="item.id" class="knowledge-collection" @click="openCollection(item.id)"><span><font-awesome-icon :icon="item.icon" /></span><div><h2>{{ localized(item.title, locale) }}</h2><p>{{ localized(item.description, locale) }}</p><small>{{ item.files.length }} {{ locale === 'id' ? 'dataset' : 'datasets' }}</small></div><b>→</b></button>
      </div>
    </template>
    <template v-else>
      <button class="back-button" @click="router.push({ name: 'library' })">← {{ locale === 'id' ? 'Semua koleksi' : 'All collections' }}</button>
      <div class="library-heading"><span><font-awesome-icon :icon="collection.icon" /></span><div><h2>{{ localized(collection.title, locale) }}</h2><p>{{ localized(collection.description, locale) }}</p></div></div>
      <div v-if="collection.files.length > 1" class="dataset-tabs"><button v-for="item in collection.files" :key="item.id" :class="{ active: file?.id === item.id }" @click="openFile(item.id)">{{ localized(item.title, locale) }}</button></div>
      <div class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ resultCount }} {{ locale === 'id' ? 'item' : 'items' }}</span></div>
      <LoadingState v-if="loading" :label="text.loading" />
      <div v-else-if="loadError" class="load-error"><p>{{ loadError }}</p></div>
      <template v-else>
        <section v-for="group in filteredGroups" :key="group.id" class="knowledge-group"><div v-if="groups.length > 1" class="group-title"><span>{{ localized(group.title, locale) }}</span><div></div></div><div class="knowledge-items"><article v-for="item in group.items" :key="item.id" class="knowledge-card"><div class="card-top"><span>{{ String(item.order ?? '').padStart(2, '0') }}</span><small>{{ item.type ?? item.category ?? '' }}</small></div><p v-if="itemArabic(item)" class="knowledge-arabic" dir="rtl">{{ itemArabic(item) }}</p><h3>{{ localized(item.title ?? item.name, locale) }}</h3><p class="knowledge-description">{{ itemDescription(item) }}</p><template v-if="item.content"><p v-if="item.content.latin" class="latin-text">{{ item.content.latin }}</p><div v-if="localized(item.content.translation, locale)" class="translation-block"><small>{{ text.translation }}</small><p>{{ localized(item.content.translation, locale) }}</p></div></template><div v-if="item.location" class="knowledge-meta">{{ localized(item.location.city, locale) }}<span v-if="item.location.city && item.location.country"> · </span>{{ localized(item.location.country, locale) }}</div><div v-if="item.date" class="knowledge-meta">{{ locale === 'id' ? 'Bulan' : 'Month' }} {{ item.date.month }}<span v-if="item.date.day"> · {{ locale === 'id' ? 'Hari' : 'Day' }} {{ item.date.day }}</span></div><div v-if="item.sources?.length || item.references?.length" class="knowledge-sources"><span v-for="source in (item.sources ?? item.references)" :key="sourceText(source)">{{ sourceText(source) }}</span></div></article></div></section>
        <p v-if="!resultCount" class="state">{{ text.empty }}</p>
      </template>
    </template>
  </section>
</template>
