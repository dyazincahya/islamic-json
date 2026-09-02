# Purification

Dataset bilingual Indonesia–Inggris tentang dasar-dasar bersuci yang disebutkan dalam Al-Quran.

## Files

| File | Contents | Items |
| --- | --- | ---: |
| `wudu.json` | Langkah wudu yang disebutkan dalam Al-Quran | 4 |
| `tayammum.json` | Dasar dan langkah tayammum | 2 |
| `ghusl.json` | Mandi untuk bersuci dari hadas besar | 1 |
| `impurities.json` | Panduan umum terkait kebersihan dan keadaan yang memerlukan bersuci | 2 |

## Schema

Each file contains a JSON array. Every item uses a stable slug in `id`, a numeric `order`, bilingual `title.id` and `title.en`, optional Arabic `title.ar`, bilingual `description`, `category`, `type`, and a `sources` array.

Quran sources use this shape:

```json
{
  "type": "quran",
  "reference": "5:6"
}
```

The dataset intentionally does not attempt to encode detailed differences among schools of Islamic jurisprudence.
