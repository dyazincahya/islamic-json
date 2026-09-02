# Sunnah Prayers Dataset

Daftar bilingual Indonesia–Inggris tentang salat sunah utama. Isinya sengaja ringkas dan mengakui perbedaan rincian antartradisi fikih.

## Files

- `data/sunnah-prayers.json` — daftar salat sunah, waktu/konteks, dan ringkasan pelaksanaan.

## Schema

Koleksi berisi `schemaVersion`, slug stabil `id`, `title`, `description`, dan `items`. Setiap item memiliki `id`, `order`, `title { id, en }`, `description { id, en }`, `context { id, en }`, `content { arabic, latin, translation { id, en } }`, serta `sources`. Array `sources` dibiarkan kosong bila referensi presisi tidak dicantumkan.

## CDN

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/sunnah-prayers/data/sunnah-prayers.json
```
