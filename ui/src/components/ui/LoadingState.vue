<script setup>
defineProps({
  label: { type: String, default: 'Loading data…' },
  compact: Boolean,
})
</script>

<template>
  <div class="loading-state" :class="{ compact }" role="status" aria-live="polite">
    <span class="loading-spinner" aria-hidden="true"></span>
    <div>
      <strong>{{ label }}</strong>
      <span class="loading-dots" aria-hidden="true"><i></i><i></i><i></i></span>
    </div>
  </div>
</template>
