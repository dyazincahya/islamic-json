# Kontribusi

Jalankan validasi berikut sebelum mengusulkan perubahan data:

```sh
python scripts/build_v2_indexes.py
python scripts/validate_v2.py
python -m unittest discover -s scripts/tests -v
```

Sertakan kedua locale (`id` dan `en`), ID stabil, registry ID yang valid, sumber yang dapat ditelusuri, dan status review yang tepat. Jangan mengubah Quran atau data legacy ketika perubahan hanya menyasar v2.

## GitHub Pages

Satu kali saja, maintainer perlu memilih **Settings → Pages → Source: GitHub Actions**. Workflow `Validate data and deploy documentation` menjalankan validator Python, test, `npm ci`, type check, dan build untuk pull request tanpa deploy. Push sukses ke `main` atau dispatch pada branch tersebut mengunggah `docs/.vitepress/dist` ke environment `github-pages`.

Untuk deploy ulang, buka tab **Actions**, pilih workflow tersebut, lalu gunakan **Run workflow** pada `main`.
