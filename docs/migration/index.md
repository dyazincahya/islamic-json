# Migrasi layout data

Direktori root lama dipindahkan ke `data/`. Panduan lengkap `MIGRATION.md` tersedia pada root repository.

Koleksi lama dipertahankan di `data/legacy/`; Quran berada mandiri di `data/holy-quran/` dan tidak deprecated. Integrasi baru sebaiknya memulai dari `data/v2/manifest.json`.

URL lama hanya dapat dipertahankan melalui compatibility tag immutable yang harus dibuat dan dipublikasikan oleh maintainer secara eksplisit.
