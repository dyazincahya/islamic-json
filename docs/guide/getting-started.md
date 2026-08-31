# Memulai

1. Muat root [`manifest.json`](../../manifest.json) untuk menemukan dataset.
2. Muat `data/v2/manifest.json` sebagai entry point data terstruktur.
3. Pilih locale `id` atau `en`; jika terjemahan tidak tersedia, gunakan `defaultLocale` manifest.
4. Muat collection index yang dideklarasikan manifest, lalu gunakan `path` setiap item untuk memuat detail.

```js
const base = "https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@<tag>/data/v2/";
const manifest = await fetch(`${base}manifest.json`).then((response) => response.json());
const index = await fetch(`${base}${manifest.collections[0].indexPath}`).then((response) => response.json());
const detail = await fetch(`${base}${index.items[0].path}`).then((response) => response.json());
```

Gunakan tag rilis immutable, bukan `main`, untuk produksi.
