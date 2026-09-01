<script setup>
import { localized, sections } from '../../data'

defineProps({ activeSection: String, locale: String })
const emit = defineEmits(['navigate'])
</script>

<template>
  <nav class="mobile-nav" aria-label="Mobile navigation">
    <button v-for="item in sections" :key="item.id" :class="{ active: activeSection === item.id }" @click="emit('navigate', item.id)">
      <span>{{ item.icon }}</span>{{ localized(item.label, locale) }}
    </button>
  </nav>
</template>
