---
layout: home
hero:
  name: Islamic JSON
  text: Data Islam yang terstruktur dan dapat diakses
  tagline: Dokumentasi, visualisasi v2, dan shortcut API/CDN dalam satu portal.
  actions:
    - theme: brand
      text: Mulai menjelajah
      link: /explorer/
    - theme: alt
      text: API & CDN
      link: /api/
features:
  - title: Multibahasa
    details: Kontrak v2 mendukung bahasa Indonesia dan English dengan fallback yang terdokumentasi.
  - title: Terstruktur
    details: Manifest, index, schema, registry, dan blok konten typed untuk integrasi yang dapat diprediksi.
  - title: Version-pinned
    details: Gunakan tag rilis immutable untuk URL CDN produksi yang stabil.
---

## Status data

<DataDashboard />

<script setup>
import DataDashboard from './components/DatasetDashboard.vue'
</script>

> **Catatan review:** validasi teknis memastikan struktur data. Validasi tersebut bukan persetujuan ilmiah atau fatwa; periksa status `draft`, `translated`, `under-review`, dan `reviewed` pada setiap konten.
