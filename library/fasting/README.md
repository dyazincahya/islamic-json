# Fasting Dataset

Dataset bilingual Indonesia–Inggris tentang jenis puasa, pembatal, keringanan, dan amalan yang dianjurkan.

## Files

- `types.json` — jenis dan klasifikasi umum puasa.
- `invalidators.json` — hal-hal yang membatalkan puasa.
- `exemptions.json` — keringanan sementara, jangka panjang, dan darurat.
- `recommended-actions.json` — amalan yang dianjurkan selama berpuasa.

## Schema

Setiap file berisi array objek dengan `id`, `order`, `title`, `description`, `category`, dan `sources`. `title` dan `description` masing-masing memiliki nilai `id` dan `en`.

## Notes

Dataset ini merupakan ringkasan edukatif dan bukan fatwa medis atau agama. Batas perjalanan, penilaian bahaya, fidyah, qada, kafarat, prosedur medis, dan rincian pembatal dapat berbeda menurut keadaan, mazhab, lembaga fikih, dan otoritas lokal. Tidak ada data hadis atau klaim nomor/derajat hadis di dalam dataset.
