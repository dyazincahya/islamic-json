# Lokalisasi

Data v2 menggunakan field lokal seperti berikut:

```json
{ "id": "Apa itu Islam?", "en": "What is Islam?" }
```

Pilih bahasa yang diminta pengguna. Bila value tidak tersedia, gunakan `manifest.defaultLocale` (`id`) dan tampilkan fallback tersebut secara jujur.

Konten Arab berada dalam field `arabic`, bukan terjemahan. Render dengan `dir="rtl"`, font Arab yang sesuai, dan jangan mencampurnya dengan transliterasi atau arti.
