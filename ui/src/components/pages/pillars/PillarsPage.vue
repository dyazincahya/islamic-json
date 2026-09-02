<script setup>
import { computed, onMounted, ref } from 'vue'
import { getPillars, localized } from '../../../data'
import ApiButton from '../../ui/ApiButton.vue'
import LoadingState from '../../ui/LoadingState.vue'
import PageHero from '../../layout/PageHero.vue'

const props = defineProps({ locale: String, text: Object })
const query = ref('')
const pillars = ref([])
const loading = ref(true)
const categories = computed(() => [...new Set(pillars.value.map((item) => item.category))])
const filtered = computed(() => { const needle = query.value.toLocaleLowerCase(); return pillars.value.filter((item) => [localized(item.title, props.locale), localized(item.content?.translation, props.locale), localized(item.content?.context, props.locale), item.category].some((value) => String(value ?? '').toLocaleLowerCase().includes(needle))) })
onMounted(async () => { try { pillars.value = await getPillars() } finally { loading.value = false } })
</script>

<template>
  <PageHero :title="locale === 'id' ? 'Rukun Islam' : 'Pillars of Islam'" :description="text.pillarsDesc" />
  <section class="browser section-wrap"><div class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ filtered.length }} {{ locale === 'id' ? 'item' : 'items' }}</span></div><LoadingState v-if="loading" :label="text.loading" /><template v-else><section v-for="category in categories" :key="category" class="pillar-group"><div class="group-title"><span>{{ category }}</span><div></div></div><div class="content-grid"><article v-for="item in filtered.filter((record) => record.category === category)" :key="item.key" class="content-card pillar-card"><div class="card-top"><span>◆</span><ApiButton :source="item.path" compact /></div><h2>{{ localized(item.title, locale) }}</h2><p v-if="item.content?.arrabic" class="arabic-text compact" dir="rtl">{{ item.content.arrabic }}</p><p v-if="item.content?.latin" class="latin-text">{{ item.content.latin }}</p><div v-if="localized(item.content?.translation, locale) || localized(item.content?.context, locale)" class="translation-block"><small>{{ text.translation }}</small><p>{{ localized(item.content?.translation, locale) || localized(item.content?.context, locale) }}</p></div><div v-if="localized(item.content?.extras, locale)" class="extras" v-html="localized(item.content.extras, locale)"></div></article></div></section><p v-if="!filtered.length" class="state">{{ text.empty }}</p></template></section>
</template>
