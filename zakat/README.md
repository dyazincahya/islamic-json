# Zakat Dataset

Dataset bilingual Indonesia–Inggris tentang kategori zakat, delapan golongan penerima, zakat fitrah, dan gambaran zakat harta.

## Files

- `categories.json` — kategori utama zakat.
- `recipients.json` — delapan golongan penerima berdasarkan Qur'an 9:60.
- `fitrah.json` — kewajiban, bentuk, takaran, waktu, dan penyaluran zakat fitrah.
- `wealth-overview.json` — gambaran umum harta, emas/perak, perdagangan, dan pertanian.

## Schema

Setiap file berisi array objek dengan bidang:

- `id`: slug stabil dan unik dalam file.
- `order`: urutan tampil, dimulai dari 1.
- `title`: label bilingual `{ "id", "en" }`.
- `description`: uraian bilingual `{ "id", "en" }`.
- `category`: kategori machine-readable.
- `sources`: array referensi non-hadis.

## Notes

Dataset ini bersifat ringkasan edukatif, bukan kalkulator atau fatwa. Nilai uang dinamis tidak disimpan. Harga acuan, konversi satuan, nisab dalam mata uang, metode penilaian, prioritas distribusi, serta rincian yang diperselisihkan harus mengikuti mazhab, regulasi, dan otoritas zakat lokal yang berwenang.
