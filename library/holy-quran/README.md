# Qur'an Dataset

Data Al-Qur'an dari Kementerian Agama Republik Indonesia, termasuk indeks surah dan juz serta file surah individual. Setiap data surah memuat teks Arab, terjemahan Indonesia dan English, serta tafsir Kemenag.

## Files

- `ministry-of-religion-of-the-republic-of-indonesia/surah.json` — indeks 114 surah.
- `ministry-of-religion-of-the-republic-of-indonesia/juz.json` — pembagian juz.
- `ministry-of-religion-of-the-republic-of-indonesia/surah/{number}.json` — data satu surah; nomor file mengikuti nomor surah dari 1 sampai 114.

Di dalam data surah, `translations.id` dan `translations.en` berisi nama surah dan teks terjemahan yang dikunci berdasarkan nomor ayat. `tafsir.id.text` berisi teks tafsir per ayat. Gunakan indeks surah untuk menemukan nomor dan metadata surah, lalu ambil file bernomor untuk membaca teks, terjemahan, dan tafsirnya. Endpoint lengkap tercantum di [`../../catalog.json`](../../catalog.json).

## Sources

- Teks Arab, terjemahan Indonesia, dan tafsir: [Qur'an Kemenag](https://quran.kemenag.go.id), dengan data tafsir tersedia di [quran-api-with-php-codeigniter](https://github.com/dyazincahya/quran-api-with-php-codeigniter/tree/master/public/assets/quran/kemenag/surah).
- Terjemahan English oleh Talal Itani, bersumber dari [Tanzil.net](https://tanzil.net) melalui [data terjemahan English](https://github.com/dyazincahya/quran-api-with-php-codeigniter/tree/master/public/assets/quran/other/translation/en). File sumber `.sources` mencatat nama penerjemah dan sumber tersebut.
