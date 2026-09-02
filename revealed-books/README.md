# Revealed Books

Dataset bilingual Indonesia–Inggris tentang empat kitab utama yang dikenal dalam ajaran Islam.

## Files

| File | Contents | Items |
| --- | --- | ---: |
| `revealed-books.json` | Taurat, Zabur, Injil, dan Al-Quran | 4 |

## Schema

The file contains a JSON array. Every item uses a stable slug in `id`, a numeric `order`, bilingual `name.id` and `name.en`, Arabic `name.ar`, bilingual `description`, `category`, `type`, and a `sources` array.

Quran sources use this shape:

```json
{
  "type": "quran",
  "reference": "5:44"
}
```
