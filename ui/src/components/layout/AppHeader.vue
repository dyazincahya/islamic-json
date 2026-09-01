<script setup>
import { localized, repositoryUrl, sections } from '../../data'

defineProps({ activeSection: String, locale: String })
const emit = defineEmits(['navigate', 'update:locale'])
</script>

<template>
  <header class="site-header">
    <button class="brand" aria-label="Islamic JSON home" @click="emit('navigate', 'home')">
      <span class="brand-mark">ا</span><span>Islamic <b>JSON</b></span>
    </button>
    <nav class="desktop-nav" aria-label="Main navigation">
      <button v-for="item in sections" :key="item.id" :class="{ active: activeSection === item.id }" @click="emit('navigate', item.id)">{{ localized(item.label, locale) }}</button>
    </nav>
    <div class="header-actions">
      <div class="locale-switch" aria-label="Language">
        <button :class="{ active: locale === 'id' }" @click="emit('update:locale', 'id')">ID</button>
        <button :class="{ active: locale === 'en' }" @click="emit('update:locale', 'en')">EN</button>
      </div>
      <a class="github-link" :href="repositoryUrl" target="_blank" rel="noreferrer" aria-label="GitHub">↗</a>
    </div>
  </header>
</template>
