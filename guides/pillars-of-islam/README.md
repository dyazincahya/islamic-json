# Pillars of Islam Guides

Panduan bilingual Indonesia–Inggris yang menjelaskan makna dan praktik umum lima rukun Islam. Dataset ini adalah pengantar, bukan pengganti bimbingan guru atau ketentuan otoritas agama setempat.

## Files

- `shahada.json` — makna dan pengamalan dua kesaksian.
- `salah.json` — persiapan dan gambaran umum salat wajib. Panduan gerakan dan bacaan terperinci tersedia di [`prayer/data/obligatory-prayer.json`](../prayer/data/obligatory-prayer.json).
- `zakat.json` — jenis, perhitungan umum, dan penyaluran zakat.
- `fasting.json` — panduan umum puasa Ramadan.
- `hajj.json` — persiapan dan gambaran tahapan utama haji.

## Schema

Setiap berkas mengikuti pola dataset panduan salat (`guides/prayer`): `schemaVersion`, slug stabil `id`, `title { id, en }`, `description { id, en }`, dan `items`. Setiap item memiliki `id`, `order`, `title { id, en }`, `description { id, en }`, `content { arabic, latin, translation { id, en } }`, serta `sources`. `arabic` dan `latin` dikosongkan jika langkah tersebut tidak memiliki bacaan khusus. Sumber dicatat per item.

Perincian fikih—termasuk perhitungan zakat, uzur puasa, dan tata cara haji dalam keadaan khusus—dapat berbeda menurut keadaan dan bimbingan yang diikuti. Konfirmasikan penerapannya kepada pembimbing tepercaya atau otoritas setempat.
