# Angels

Dataset bilingual Indonesia–Inggris tentang malaikat yang namanya disebut secara eksplisit dalam Al-Quran.

## Files

| File | Contents | Items |
| --- | --- | ---: |
| `angels.json` | Jibril, Mikail, Malik, Harut, dan Marut | 5 |

## Schema

The file contains a JSON array. Every item uses a stable slug in `id`, a numeric `order`, bilingual `name.id` and `name.en`, Arabic `name.ar`, bilingual `description`, `category`, `type`, and a `sources` array.

Quran sources use this shape:

```json
{
  "type": "quran",
  "reference": "2:97"
}
```

The scope is deliberately conservative. It excludes popular names and assigned duties that are not explicitly established by the cited Quran passages.
