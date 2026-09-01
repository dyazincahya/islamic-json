<script setup>
defineProps({ title: String, description: String })
</script>

<template>
  <section class="page-hero">
    <p class="eyebrow"><span></span>Islamic JSON</p>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
  </section>
</template>
