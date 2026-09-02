# Islamic Calendar

Dataset bilingual Indonesia–Inggris untuk 12 bulan Hijriah dan hari atau periode Islam penting.

## JSON

- [`calendar.json`](./calendar.json) — 12 bulan dan 8 event

## Struktur

Bulan berada pada `months`; event berada pada `events`. Setiap entri memiliki `id`, `order`, `name` atau `title`, `description`, dan `references`. Nilai `date` selalu berupa tanggal Hijriah dan tidak berisi konversi Masehi dinamis.

## Catatan penetapan tanggal

Awal bulan dapat ditentukan melalui rukyat hilal atau perhitungan menurut metode dan otoritas yang diikuti. Akibatnya, awal bulan dan event terkait dapat berbeda satu hari antarwilayah atau organisasi. Tanggal tradisional yang tidak ditetapkan secara eksplisit oleh Al-Quran ditandai melalui `certainty`; tanggal Lailatulqadar tidak dipastikan dan menggunakan rentang malam.

## CDN

```text
https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json/islamic-calendar/calendar.json
```
