<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { localized, repositoryUrl, sections } from '../../data'

const props = defineProps({ activeSection: String, locale: String })
const emit = defineEmits(['navigate', 'update:locale'])
const collectionDropdown = ref(null)
const developerDropdown = ref(null)
const primarySections = sections.filter((item) => ['home', 'quran', 'library'].includes(item.id))
const collectionSections = sections.filter((item) => ['dua', 'asmaul', 'pillars', 'faith'].includes(item.id))
const developerSections = sections.filter((item) => ['developer', 'relationships'].includes(item.id))
const collectionActive = computed(() => collectionSections.some((item) => item.id === props.activeSection))
const developerActive = computed(() => developerSections.some((item) => item.id === props.activeSection))

function menuDescription(id) {
  const descriptions = {
    dua: { id: 'Doa sehari-hari', en: 'Daily supplications' },
    asmaul: { id: '99 Asmaul Husna', en: '99 Beautiful Names' },
    pillars: { id: 'Lima dasar Islam', en: 'Five foundations of Islam' },
    faith: { id: 'Enam dasar iman', en: 'Six foundations of faith' },
    developer: { id: 'Endpoint dan GitCDN', en: 'Endpoints and GitCDN' },
    relationships: { id: 'Diagram keterkaitan data', en: 'Data relationship diagram' },
  }
  return descriptions[id]?.[props.locale] ?? ''
}
function closeDropdowns() {
  collectionDropdown.value?.removeAttribute('open')
  developerDropdown.value?.removeAttribute('open')
}
function navigate(section) {
  closeDropdowns()
  emit('navigate', section)
}
function closeOnOutsideClick(event) {
  const clickedInside = collectionDropdown.value?.contains(event.target) || developerDropdown.value?.contains(event.target)
  if (!clickedInside) closeDropdowns()
}
function closeOnEscape(event) {
  if (event.key === 'Escape') closeDropdowns()
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
      <details ref="collectionDropdown" class="nav-dropdown">
        <summary :class="{ active: collectionActive }">{{ locale === 'id' ? 'Koleksi' : 'Collections' }} <font-awesome-icon icon="chevron-down" /></summary>
        <div class="dropdown-menu">
          <button v-for="item in collectionSections" :key="item.id" :class="{ active: activeSection === item.id }" @click="navigate(item.id)"><span><font-awesome-icon :icon="item.icon" /></span><span><b>{{ localized(item.label, locale) }}</b><small>{{ menuDescription(item.id) }}</small></span></button>
        </div>
      </details>
      <details ref="developerDropdown" class="nav-dropdown developer-dropdown">
        <summary :class="{ active: developerActive }">Developer <font-awesome-icon icon="chevron-down" /></summary>
        <div class="dropdown-menu">
          <button v-for="item in developerSections" :key="item.id" :class="{ active: activeSection === item.id }" @click="navigate(item.id)"><span><font-awesome-icon :icon="item.icon" /></span><span><b>{{ localized(item.label, locale) }}</b><small>{{ menuDescription(item.id) }}</small></span></button>
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
