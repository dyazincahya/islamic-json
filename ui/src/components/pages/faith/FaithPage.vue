<script setup>
import { computed, ref } from 'vue'
import { getPillarsOfFaith, localized } from '../../../data'
import ApiButton from '../../ui/ApiButton.vue'
import PageHero from '../../layout/PageHero.vue'

const props = defineProps({ locale: String, text: Object })
const query = ref('')
const pillars = getPillarsOfFaith()
const faithIcon = (icon) => icon.includes('book') ? 'book-open' : icon.includes('hourglass') ? 'hourglass-half' : icon.includes('balance') ? 'scale-balanced' : icon.includes('feather') ? 'feather' : icon.includes('user') ? 'user-check' : icon.includes('star') ? 'star-and-crescent' : 'shield-heart'
const filtered = computed(() => {
  const needle = query.value.toLocaleLowerCase()
  return pillars.filter((item) => [localized(item.title, props.locale), localized(item.content?.context, props.locale)].some((value) => String(value ?? '').toLocaleLowerCase().includes(needle)))
})
</script>

<template>
  <PageHero :title="locale === 'id' ? 'Rukun Iman' : 'Pillars of Faith'" :description="text.faithDesc" api-path="pillars-of-faith/main.json" />
  <section class="browser section-wrap">
    <div class="toolbar"><label class="search"><span>⌕</span><input v-model="query" :placeholder="text.search" /></label><span class="result-count">{{ filtered.length }} {{ locale === 'id' ? 'item' : 'items' }}</span></div>
    <div class="content-grid faith-grid">
      <article v-for="(item, index) in filtered" :key="item.title.id" class="content-card faith-card">
        <div class="card-top"><span>{{ String(index + 1).padStart(2, '0') }}</span><ApiButton source="pillars-of-faith/main.json" compact /></div>
        <div class="faith-icon"><font-awesome-icon :icon="faithIcon(item.icon)" /></div>
        <h2>{{ localized(item.title, locale) }}</h2>
        <div class="translation-block"><small>{{ locale === 'id' ? 'Penjelasan' : 'Explanation' }}</small><p>{{ localized(item.content.context, locale) }}</p></div>
      </article>
      <p v-if="!filtered.length" class="state">{{ text.empty }}</p>
    </div>
  </section>
</template>
