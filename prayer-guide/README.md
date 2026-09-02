# Prayer Guide Dataset

Panduan bilingual Indonesia–Inggris untuk urutan gerakan dan bacaan salat wajib. Dataset ini ringkas dan ditujukan sebagai data referensi aplikasi, bukan pengganti bimbingan guru.

## Files

- `data/obligatory-prayer.json` — urutan gerakan dan bacaan dari niat hingga salam.

## Schema

Koleksi berisi `schemaVersion`, slug stabil `id`, `title`, `description`, dan `items`. Setiap item memiliki `id`, `order`, `title { id, en }`, `description { id, en }`, `content { arabic, latin, translation { id, en } }`, serta `sources`. String bacaan boleh kosong ketika langkah tidak memerlukan lafaz tertentu.

## CDN

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/prayer-guide/data/obligatory-prayer.json
```
