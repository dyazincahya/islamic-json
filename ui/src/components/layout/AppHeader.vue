<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { localized, repositoryUrl, sections } from '../../data'

const props = defineProps({ activeSection: String, locale: String })
const emit = defineEmits(['navigate', 'update:locale'])
const dropdown = ref(null)
const primarySections = sections.filter((item) => ['home', 'quran', 'developer'].includes(item.id))
const collectionSections = sections.filter((item) => !['home', 'quran', 'developer'].includes(item.id))
const collectionActive = computed(() => collectionSections.some((item) => item.id === props.activeSection))

function navigate(section) {
  dropdown.value?.removeAttribute('open')
  emit('navigate', section)
}
function closeOnOutsideClick(event) {
  if (dropdown.value && !dropdown.value.contains(event.target)) dropdown.value.removeAttribute('open')
}
function closeOnEscape(event) {
  if (event.key === 'Escape') dropdown.value?.removeAttribute('open')
}
onMounted(() => {
  document.addEventListener('pointerdown', closeOnOutsideClick)
  document.addEventListener('keydown', closeOnEscape)
})
onBeforeUnmount(() => {
  document.removeEventListener('pointerdown', closeOnOutsideClick)
  document.removeEventListener('keydown', closeOnEscape)
})
</script>

<template>
  <header class="site-header">
    <button class="brand" aria-label="Islamic JSON home" @click="emit('navigate', 'home')">
      <span class="brand-mark">ا</span><span>Islamic <b>JSON</b></span>
    </button>
    <nav class="desktop-nav" aria-label="Main navigation">
      <button v-for="item in primarySections" :key="item.id" :class="{ active: activeSection === item.id }" @click="navigate(item.id)">{{ localized(item.label, locale) }}</button>
      <details ref="dropdown" class="nav-dropdown">
        <summary :class="{ active: collectionActive }">{{ locale === 'id' ? 'Koleksi' : 'Collections' }} <font-awesome-icon icon="chevron-down" /></summary>
        <div class="dropdown-menu">
          <button v-for="item in collectionSections" :key="item.id" :class="{ active: activeSection === item.id }" @click="navigate(item.id)"><span><font-awesome-icon :icon="item.icon" /></span><span><b>{{ localized(item.label, locale) }}</b><small>{{ item.id === 'dua' ? (locale === 'id' ? 'Doa sehari-hari' : 'Daily supplications') : item.id === 'asmaul' ? '99 Asmaul Husna' : item.id === 'pillars' ? (locale === 'id' ? 'Lima dasar Islam' : 'Five foundations of Islam') : (locale === 'id' ? 'Enam dasar iman' : 'Six foundations of faith') }}</small></span></button>
        </div>
      </details>
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
