# Dhikr Dataset

Dataset dzikir bilingual Indonesia–Inggris. Gunakan `categories.json` sebagai indeks dan file di `data/` sebagai koleksi bacaan.

## Files

- `categories.json` — indeks kategori dan lokasi file.
- `data/morning-dhikr.json` — dzikir pagi.
- `data/evening-dhikr.json` — dzikir petang.
- `data/after-prayer-dhikr.json` — dzikir setelah salat wajib.
- `data/general-dhikr.json` — dzikir umum.

## Schema

Setiap koleksi berisi `schemaVersion`, `id`, `title { id, en }`, dan `items`. Setiap item memiliki slug stabil `id`, `order`, `title`, `context`, `content { arabic, latin, translation { id, en } }`, serta `sources`. `sources` kosong bila referensi yang presisi tidak dicantumkan.

## CDN

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/dhikr/categories.json
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/dhikr/data/morning-dhikr.json
```

Ganti bagian path terakhir untuk mengakses file lain.
