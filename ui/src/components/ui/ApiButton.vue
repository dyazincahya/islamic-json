<script setup>
import { computed } from 'vue'
import { apiUrl } from '../../data'

const props = defineProps({
  source: { type: String, required: true },
  label: { type: String, default: 'API' },
  compact: Boolean,
})
const href = computed(() => apiUrl(props.source))
</script>

<template>
  <a class="api-button" :class="{ compact }" :href="href" target="_blank" rel="noreferrer" title="Open in GitCDN Generator">
    <font-awesome-icon icon="code" />
    <span>{{ label }}</span>
    <span class="api-button-arrow">↗</span>
  </a>
</template>
