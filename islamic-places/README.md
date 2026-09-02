# Islamic Places

Dataset bilingual Indonesia–Inggris untuk lokasi utama yang berkaitan dengan ibadah, sejarah awal Islam, atau tempat yang disebut dalam Al-Quran.

## JSON

- [`places.json`](./places.json) — 15 entri

## Struktur

Setiap entri memiliki `id`, `order`, `name` (`id`, `en`, `ar`), `description` (`id`, `en`), `location`, `coordinates`, dan `references`. Referensi mengacu ke array `sources`.

Koordinat adalah titik representatif dengan format derajat desimal, bukan batas kawasan. `coordinates` bernilai `null` ketika lokasi atau satu titik geografis tidak cukup pasti. Penyebutan negara pada lokasi berfungsi sebagai label geografis dataset dan tidak dimaksudkan sebagai penetapan batas politik.

## CDN

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/islamic-places/places.json
```
