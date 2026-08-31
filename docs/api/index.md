# API & CDN explorer

Gunakan jsDelivr sebagai CDN produksi yang direkomendasikan dan pin tag rilis immutable. Statically adalah alternatif; GitHub Raw hanya untuk debugging. GitHub Pages menampilkan snapshot data dari commit dokumentasi, bukan API rilis.

<ApiPlayground />

<script setup>
import ApiPlayground from '../components/ApiPlayground.vue'
</script>

## Provider URL patterns

| Provider     | Template                                                                  |
| ------------ | ------------------------------------------------------------------------- |
| jsDelivr     | `https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@<tag>/<path>`       |
| Statically   | `https://cdn.statically.io/gh/dyazincahya/islamic-json/<tag>/<path>`      |
| GitHub Raw   | `https://raw.githubusercontent.com/dyazincahya/islamic-json/<tag>/<path>` |
| GitHub Pages | `https://dyazincahya.github.io/islamic-json/<path>`                       |

Jika preview lintas-origin gagal karena CORS, URL tetap dapat disalin atau dibuka di tab baru. Pilih provider alternatif sendiri—portal tidak berpindah provider secara diam-diam.
