# Model data

Setiap dokumen konten memiliki `id`, `type`, `slug`, `status`, title lokal, dan dapat memiliki `sourceIds`, `featureIds`, `iconId`, relasi, serta `blocks` terstruktur.

Status publikasi:

- `draft`: belum siap dipakai sebagai materi review.
- `translated`: terjemahan tersedia tetapi review dapat belum lengkap.
- `under-review`: sedang ditinjau.
- `reviewed`: metadata review lengkap; bukan klaim otoritas ilmiah universal.
- `deprecated`: gunakan pengganti yang dideklarasikan.

Gunakan schemas di `data/v2/schemas/` untuk validasi penuh.
