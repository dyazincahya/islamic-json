# Prophets

Dataset bilingual Indonesia–Inggris tentang 25 nabi dan rasul yang dikenal luas dalam tradisi Islam.

## JSON

- [`prophets.json`](./prophets.json) — 25 entri

## Struktur

Setiap entri memiliki `id`, `order`, `name` (`id`, `en`, `ar`), `description` (`id`, `en`), dan `references`. Referensi ayat memakai format `surah:ayat` atau `surah:ayat-awal-ayat-akhir` dan mengacu ke sumber pada array `sources`.

Deskripsi sengaja ringkas dan tidak memuat kisah, kronologi, silsilah, atau lokasi yang tidak dinyatakan secara jelas dalam Al-Quran.

## CDN

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/prophets/prophets.json
```
