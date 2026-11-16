# Islamic Data Library

`library/` berisi koleksi bacaan, data referensi, dan ringkasan pengetahuan. Contohnya Al-Qur'an, doa, dzikir, Asmaul Husna, rukun Islam dan iman, zakat, kalender, serta data para nabi.

Setiap topik memiliki subdirektori sendiri agar konten terkait tetap terkelompok. Gunakan [`../catalog.json`](../catalog.json) untuk menemukan dataset dan endpoint JSON-nya; skema katalog tersedia di [`../catalog.schema.json`](../catalog.schema.json).

Saat menambah koleksi, letakkan data di `library/<topik>/`, sediakan README yang menjelaskan format datanya, lalu daftarkan metadata koleksi pada `COLLECTIONS` di `scripts/generate_catalog.py` dan jalankan:

```bash
python scripts/generate_catalog.py
```
