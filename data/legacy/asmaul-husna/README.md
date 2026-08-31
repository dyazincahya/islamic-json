# Asmaul Husna

## Database Format

Create new Table, Avaliable for SQLite, MySQL, MariaDB & PostgreSQL.

### SQLite

```sql
CREATE TABLE asmaul_husna (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arab TEXT NOT NULL,
    indo TEXT NOT NULL,
    latin TEXT NOT NULL
);
```

### MySQL

```sql
CREATE TABLE asmaul_husna (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_arab VARCHAR(255) NOT NULL,
    nama_indo VARCHAR(255) NOT NULL,
    nama_latin VARCHAR(255) NOT NULL,
    deskripsi TEXT
);
```

### MariaDB

```sql
CREATE TABLE asmaul_husna (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_arab VARCHAR(255) NOT NULL,
    nama_indo VARCHAR(255) NOT NULL,
    nama_latin VARCHAR(255) NOT NULL,
    deskripsi TEXT
);
```

### PostgreSQL

```sql
CREATE TABLE asmaul_husna (
    id SERIAL PRIMARY KEY,
    nama_arab VARCHAR(255) NOT NULL,
    nama_indo VARCHAR(255) NOT NULL,
    nama_latin VARCHAR(255) NOT NULL,
    deskripsi TEXT
);
```

## Insert data SQL

99 Asmaul Husna.

```sql
INSERT INTO asmaul_husna (arab, indo, latin) VALUES
('الرَّحْمـٰنُ', 'Yang Maha Pengasih', 'Ar-Rahmânu'),
('الرَّحِيْمُ', 'Yang Maha Penyayang', 'Ar-Raḫîmu'),
('الْمَلِكُ', 'Yang Maha Merajai/Memerintah', 'Al-Maliku'),
('الْقُدُّوْسُ', 'Yang Mahasuci', 'Al-Quddûsu'),
('السَّلاَمُ', 'Yang Maha Memberi Kesejahteraan', 'As-Salâmu'),
('الْمُؤْمِنُ', 'Yang Maha Memberi Keamanan', 'Al-Mu’minu'),
('الْمُهَيْمِنُ', 'Yang Maha Pemelihara', 'Al-Muhaiminu'),
('الْعَزِيْزُ', 'Yang Memiliki Mutlak Kegagahan', 'Al-`Azizu'),
('الْجَبَّارُ', 'Yang Maha Perkasa', 'Al-Jabbâru'),
('الْمُتَكَبِّرُ', 'Yang Maha Megah', 'Al-Mutakabbiru'),
('الْخَالِقُ', 'Yang Maha Pencipta', 'Al-Ḫâliqu'),
('الْبَارِئُ', 'Yang Maha Melepaskan (Membuat, Membentuk)', 'Al-Bâri`u'),
('الْمُصَوِّرُ', 'Yang Maha Membentuk Rupa (Makhluknya)', 'Al-Muṣawwiru'),
('الْغَفَّارُ', 'Yang Maha Pengampun', 'Al-Ḡaffâru'),
('الْقَهَّارُ', 'Yang Maha Memaksa', 'Al-Qahhâru'),
('الْوَهَّابُ', 'Yang Maha Pemberi Karunia', 'Al-Wahhâbu'),
('الرَّزَّاقُ', 'Yang Maha Pemberi Rezeki', 'Ar-Razzâqu'),
('الْفَتَّاحُ', 'Yang Maha Pembuka Rahmat', 'Al-Fattâḥu'),
('اَلْعَلِيْمُ', 'Yang Maha Mengetahui', 'Al-‘Alîmu'),
('الْقَابِضُ', 'Yang Maha Menyempitkan (makhluknya)', 'Al-Qâbiḍu'),
('الْبَاسِطُ', 'Yang Maha Melapangkan (makhluknya)', 'Al-Bâsiṭu'),
('الْخَافِضُ', 'Yang Maha Merendahkan (makhluknya)', 'Al-Ḫâfiḍu'),
('الرَّافِعُ', 'Yang Maha Meninggikan (makhluknya)', 'Ar-Râfi‘u'),
('المعز', 'Yang Maha Memuliakan (makhluknya)', 'Al-Mu‘izzu'),
('المذل', 'Yang Maha Menghinakan (makhluknya)', 'Al-Muzilu'),
('السميع', 'Yang Maha Mendengar', 'As-Samî‘u'),
('البصير', 'Yang Maha Melihat', 'Al-Baṣîru'),
('الحكم', 'Yang Maha Menetapkan', 'Al-Ḥakâmu'),
('العدل', 'Yang Maha Adil', 'Al-‘Adlu'),
('اللطيف', 'Yang Maha Lembut', 'Al-Laṭîfu'),
('الخبير', 'Yang Maha Mengenal', 'Al-Ḫabîru'),
('الحليم', 'Yang Maha Penyantun', 'Al-Ḥalîmu'),
('العظيم', 'Yang Maha Agung', 'Al-‘Aẓîmu'),
('الغفور', 'Yang Maha Memberi Pengampunan', 'Al-Ḡafûru'),
('الشكور', 'Yang Maha Pembalas Budi (menghargai)', 'As-Syakûru'),
('العلي', 'Yang Maha Tinggi', 'Al-‘Aliyyu'),
('الكبير', 'Yang Maha Besar', 'Al-Kabîru'),
('الحفيظ', 'Yang Maha Memelihara', 'Al-Ḥafiẓu'),
('المقيت', 'Yang Maha Pemberi Kecukupan', 'Al-Muqîtu'),
('الحسيب', 'Yang Maha Membuat Perhitungan', 'Al-Ḥasîbu'),
('الجليل', 'Yang Maha Luhur', 'Al-Jalîlu'),
('الكريم', 'Yang Maha Pemurah', 'Al-Karîmu'),
('الرقيب', 'Yang Maha Mengawasi', 'Ar-Raqîbu'),
('المجيب', 'Yang Maha Mengabulkan', 'Al-Mujîbu'),
('الواسع', 'Yang Maha Luas', 'Al-Wâsi‘u'),
('الحكيم', 'Yang Maha Bijaksana', 'Al-Ḥakîmu'),
('الودود', 'Yang Maha Mengasihi', 'Al-Wadûdu'),
('المجيد', 'Yang Maha Mulia', 'Al-Majîdu'),
('الباعث', 'Yang Maha Membangkitkan', 'Al-Bâ‘iṡu'),
('الشهيد', 'Yang Maha Menyaksikan', 'Asy-Syahîdu'),
('الحق', 'Yang Maha Benar', 'Al-Ḥaqq'),
('الوكي', 'Yang Maha Memelihara', 'Al-Wakîlu'),
('القوي', 'Yang Maha Kuat', 'Al-Qawiyyu'),
('المتين', 'Yang Maha Kokoh', 'Al-Matînu'),
('الولي', 'Yang Maha Melindungi', 'Al-Waliyyu'),
('الحميد', 'Yang Maha Terpuji', 'Al-Ḥamîdu'),
('المحصي', 'Yang Maha Mengalkulasi', 'Al-Muḥṣî'),
('المبدئ', 'Yang Maha Memulai', 'Al-Mubdi`u'),
('المعيد', 'Yang Maha Mengembalikan Kehidupan', 'Al-Mu‘îdu'),
('المحي', 'Yang Maha Menghidupkan', 'Al-Muḥyî'),
('المميت', 'Yang Maha Mematikan', 'Al-Mumîtu'),
('الحي', 'Yang Maha Hidup', 'Al-Ḥayy'),
('القيوم', 'Yang Maha Berdiri Sendiri', 'Al-Qayyûm'),
('الواجد', 'Yang Maha Menemukan', 'Al-Wâjidu'),
('الماجد', 'Yang Maha Mulia', 'Al-Mâjidu'),
('الواحد', 'Yang Maha Tunggal', 'Al-Wâḥid'),
('الاحد', 'Yang Maha Esa', 'Al-Aḥad'),
('الصمد', 'Yang Maha Dibutuhkan', 'As-Ṣamad'),
('القادر', 'Yang Maha Menentukan', 'Al-Qâdiru'),
('المقتدر', 'Yang Maha Berkuasa', 'Al-Muqtadir'),
('المقدم', 'Yang Maha Mendahulukan', 'Al-Muqaddimu'),
('المؤخر', 'Yang Maha Mengakhirkan', 'Al-Mu’akhiru'),
('الأول', 'Yang Maha Awal', 'Al-Awwalu'),
('الأخر', 'Yang Maha Akhir', 'Al-Âkhiru'),
('الظاهر', 'Yang Maha Nyata', 'Aẓ-Ẓâhiru'),
('الباطن', 'Yang Maha Ghaib', 'Al-Bâṭinu'),
('الوالي', 'Yang Maha Memerintah', 'Al-Wâliy'),
('المتعال', 'Yang Maha Tinggi', 'Al-Muta‘âli'),
('البر', 'Yang Maha Dermawan', 'Al-Barru'),
('التواب', 'Yang Maha Penerima Tobat', 'At-Tawwâbu'),
('المنتقم', 'Yang Maha Penuntut Balas', 'Al-Muntaqimu'),
('العفو', 'Yang Maha Pemaaf', 'Al-‘Afuw'),
('الرؤوف', 'Yang Maha Pengasih', 'Ar-Ra’ûfu'),
('مالك الملك', 'Yang Maha Penguasa Kerajaan', 'Mâlikul-Mulk'),
('ذوالجلال', 'Yang Maha Pemilik Keagungan', 'Dhûl-Jalâli wal-Ikrâm'),
('المقسط', 'Yang Maha Adil', 'Al-Muqsiṭu'),
('الجامع', 'Yang Maha Mengumpulkan', 'Al-Jâmi‘u'),
('الغني', 'Yang Maha Kaya', 'Al-Ḡhaniyyu'),
('المغني', 'Yang Maha Memberi Kekayaan', 'Al-Muḡniyu'),
('المانع', 'Yang Maha Mencegah', 'Al-Mâni‘u'),
('الضار', 'Yang Maha Memberi Kemudharatan', 'Aḍ-Ḍârru'),
('النافع', 'Yang Maha Memberi Manfaat', 'An-Nâfi‘u'),
('النور', 'Yang Maha Bercahaya (Menerangi)', 'An-Nûru'),
('الهادي', 'Yang Maha Pemberi Petunjuk', 'Al-Hâdi'),
('البديع', 'Yang Maha Pencipta', 'Al-Badî‘u'),
('الباقي', 'Yang Maha Kekal', 'Al-Bâqî'),
('الوارث', 'Yang Maha Pewaris', 'Al-Wârithu'),
('الرشيد', 'Yang Maha Pandai', 'Ar-Rasyîdu'),
('الصبور', 'Yang Maha Sabar', 'Aṣ-Ṣabûru');
```

## JSON Format

[See Here](https://github.com/dyazincahya/islamic-json/blob/main/asmaul-husna/asmaul-husna.json)
