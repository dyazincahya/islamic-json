<script setup>
import { dataRelationshipDiagram } from '../../../relationships'
import PageHero from '../../layout/PageHero.vue'
import MermaidDiagram from '../../ui/MermaidDiagram.vue'

defineProps({ locale: String, text: Object })
</script>

<template>
  <PageHero :title="locale === 'id' ? 'Relasi Data' : 'Data Relationships'" :description="text.relationshipsDesc" />
  <section class="browser section-wrap relationships-browser">
    <div class="relationship-intro">
      <div><span>01</span><h2>{{ locale === 'id' ? 'Sumber dan referensi' : 'Sources and references' }}</h2><p>{{ locale === 'id' ? 'Al-Qur’an menjadi sumber referensi ayat untuk berbagai koleksi akidah, ibadah, sejarah, dan adab.' : 'The Qur’an provides verse references for collections about belief, worship, history, and manners.' }}</p></div>
      <div><span>02</span><h2>{{ locale === 'id' ? 'Domain pengetahuan' : 'Knowledge domains' }}</h2><p>{{ locale === 'id' ? 'Rukun Islam dan Rukun Iman menghubungkan konsep utama dengan dataset penjelas yang lebih rinci.' : 'The pillars of Islam and faith connect core concepts to more detailed explanatory datasets.' }}</p></div>
      <div><span>03</span><h2>{{ locale === 'id' ? 'Akses developer' : 'Developer access' }}</h2><p>{{ locale === 'id' ? 'Pustaka menyajikan data untuk pembaca, sedangkan Developer API menyediakan akses GitCDN untuk aplikasi.' : 'The Library presents data to readers, while Developer API provides GitCDN access for applications.' }}</p></div>
    </div>
    <div class="diagram-panel">
      <div class="diagram-heading"><div><p class="eyebrow"><span></span>Entity Relationship</p><h2>{{ locale === 'id' ? 'Peta keterkaitan koleksi' : 'Collection relationship map' }}</h2></div></div>
      <MermaidDiagram :source="dataRelationshipDiagram" />
    </div>
  </section>
</template>
