<script setup>
import ApiButton from '../ui/ApiButton.vue'

defineProps({ title: String, description: String, apiPath: String })
</script>

<template>
  <section class="page-hero">
    <p class="eyebrow"><span></span>Islamic JSON</p>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <ApiButton v-if="apiPath" :source="apiPath" />
  </section>
</template>
