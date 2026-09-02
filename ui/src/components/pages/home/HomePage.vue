<script setup>
import { localized, repositoryUrl, sections, stats } from '../../../data'

defineProps({ locale: String, text: Object })
const emit = defineEmits(['navigate'])
</script>

<template>
  <section class="hero">
    <div class="hero-copy">
      <p class="eyebrow"><span></span>{{ text.eyebrow }}</p><h1>{{ text.hero }}</h1><p class="hero-intro">{{ text.intro }}</p>
      <div class="hero-actions"><button class="primary-button" @click="emit('navigate', 'quran')">{{ text.explore }} <span>→</span></button><a class="text-link" :href="repositoryUrl" target="_blank" rel="noreferrer">{{ text.source }} ↗</a></div>
    </div>
    <div class="hero-art" aria-hidden="true"><div class="arch"><div class="quran-mark">اقْرَأْ</div><div class="ornament">✦</div><p>Bacalah dengan nama Tuhanmu</p></div></div>
  </section>
  <section class="stats-grid" aria-label="Dataset statistics">
    <div><strong>{{ stats.surah }}</strong><span>{{ text.surah }}</span></div><div><strong>{{ stats.ayah.toLocaleString('id-ID') }}</strong><span>{{ text.ayah }}</span></div><div><strong>{{ stats.dua }}</strong><span>{{ text.dua }}</span></div><div><strong>{{ stats.asmaul }}</strong><span>{{ text.names }}</span></div>
  </section>
  <section class="collections section-wrap">
    <div class="section-heading"><p class="eyebrow"><span></span>{{ text.collection }}</p><h2>{{ locale === 'id' ? 'Jelajahi berdasarkan topik' : 'Explore by topic' }}</h2></div>
    <div class="collection-grid">
      <button class="collection-card quran-card" @click="emit('navigate', 'quran')"><span class="card-icon"><font-awesome-icon icon="book-quran" /></span><div><h3>Al-Qur’an</h3><p>{{ text.quranDesc }}</p><small>{{ stats.surah }} {{ text.surah }} · {{ stats.ayah.toLocaleString('id-ID') }} {{ text.ayah }}</small></div><b>→</b></button>
      <button class="collection-card" @click="emit('navigate', 'dua')"><span class="card-icon"><font-awesome-icon icon="hands-praying" /></span><div><h3>{{ localized(sections[2].label, locale) }}</h3><p>{{ text.duaDesc }}</p><small>{{ stats.dua }} {{ text.dua }}</small></div><b>→</b></button>
      <button class="collection-card" @click="emit('navigate', 'asmaul')"><span class="card-icon"><font-awesome-icon icon="star-and-crescent" /></span><div><h3>Asmaul Husna</h3><p>{{ text.asmaulDesc }}</p><small>99 {{ text.names }}</small></div><b>→</b></button>
      <button class="collection-card" @click="emit('navigate', 'pillars')"><span class="card-icon"><font-awesome-icon icon="kaaba" /></span><div><h3>{{ localized(sections.find((item) => item.id === 'pillars').label, locale) }}</h3><p>{{ text.pillarsDesc }}</p><small>5 {{ locale === 'id' ? 'pilar' : 'pillars' }}</small></div><b>→</b></button>
      <button class="collection-card" @click="emit('navigate', 'faith')"><span class="card-icon"><font-awesome-icon icon="shield-heart" /></span><div><h3>{{ localized(sections.find((item) => item.id === 'faith').label, locale) }}</h3><p>{{ text.faithDesc }}</p><small>6 {{ locale === 'id' ? 'pilar' : 'pillars' }}</small></div><b>→</b></button>
      <button class="collection-card" @click="emit('navigate', 'library')"><span class="card-icon"><font-awesome-icon icon="layer-group" /></span><div><h3>{{ localized(sections.find((item) => item.id === 'library').label, locale) }}</h3><p>{{ text.libraryDesc }}</p><small>12 {{ locale === 'id' ? 'koleksi' : 'collections' }}</small></div><b>→</b></button>
    </div>
  </section>
</template>
