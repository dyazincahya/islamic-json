# Qur'an Kemenag Dataset

Data Al-Qur'an dari Kementerian Agama Republik Indonesia, termasuk indeks surah dan juz serta file surah individual. Teks Arab dan terjemahan Indonesia disediakan pada data surah.

## Files

- `ministry-of-religion-of-the-republic-of-indonesia/surah.json` — indeks 114 surah.
- `ministry-of-religion-of-the-republic-of-indonesia/juz.json` — pembagian juz.
- `ministry-of-religion-of-the-republic-of-indonesia/surah/{number}.json` — data satu surah; nomor file mengikuti nomor surah dari 1 sampai 114.

Gunakan indeks surah untuk menemukan nomor dan metadata surah, lalu ambil file bernomor untuk membaca teks dan terjemahannya. Endpoint lengkap tercantum di [`../../catalog.json`](../../catalog.json).

Sumber resmi: [Qur'an Kemenag](https://quran.kemenag.go.id). Informasi sumber dan proses pengambilan data juga dijelaskan pada README proyek utama.
