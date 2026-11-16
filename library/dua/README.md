# Daily Dua Collection

Kumpulan doa harian dengan teks Arab, transliterasi, terjemahan Indonesia, catatan, dan rujukan. Metadata kategori menyediakan label Indonesia dan Inggris; isi doa pada dataset saat ini terutama berbahasa Arab dan Indonesia.

## Files

- `categories.json` — kategori doa dan slug koleksi.
- `data/daily-dua.json` — daftar doa harian.

## Schema

`categories.json` adalah array objek dengan label `id`, label `en`, dan `slug`. `data/daily-dua.json` adalah array objek doa dengan `title`, `arabic`, `latin`, `translation`, `notes`, `fawaid`, dan `source`. Beberapa nilai opsional dapat bernilai `null`.

Lihat [`../../catalog.json`](../../catalog.json) untuk endpoint unduhan terkini.
