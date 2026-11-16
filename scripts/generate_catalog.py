#!/usr/bin/env python3
"""Generate the Schema.org JSON-LD catalog from library/ and guides/."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/dyazincahya/islamic-json"
CATALOG_ID = f"{REPOSITORY}/catalog.json"
CDN_BASE = "https://cdn.jsdelivr.net/gh/dyazincahya/islamic-json@main"
LICENSE_URL = f"{REPOSITORY}/blob/main/LICENSE"

COLLECTIONS = {
    "library/angels": (
        "Malaikat",
        "Angels",
        "Malaikat yang disebut dalam Al-Qur'an.",
        "Angels mentioned in the Quran.",
        ["Islam", "belief", "angels"],
        ["id", "en"],
    ),
    "library/asmaul-husna": (
        "Asmaul Husna",
        "Asma ul Husna",
        "Nama-nama Allah, transliterasi, dan artinya.",
        "Names of Allah with transliterations and meanings.",
        ["Islam", "names of Allah", "reference"],
        ["id", "ar"],
    ),
    "library/dhikr": (
        "Dzikir",
        "Dhikr",
        "Kumpulan bacaan dzikir beserta konteks, transliterasi, dan terjemahan.",
        "Collections of dhikr with context, transliteration, and translations.",
        ["Islam", "worship", "remembrance"],
        ["id", "en", "ar"],
    ),
    "library/dua": (
        "Doa",
        "Dua",
        "Kumpulan doa sehari-hari beserta bacaan dan terjemahannya.",
        "Daily supplications with recitations and translations.",
        ["Islam", "supplication", "dua"],
        ["id", "en", "ar"],
    ),
    "library/fasting": (
        "Referensi Puasa",
        "Fasting Reference",
        "Jenis puasa, pembatal, keringanan, dan amalan yang dianjurkan.",
        "Fasting types, invalidators, concessions, and recommended practices.",
        ["Islam", "worship", "fasting"],
        ["id", "en"],
    ),
    "library/holy-quran": (
        "Al-Qur'an Kemenag",
        "Quran Kemenag",
        "Teks Al-Qur'an, terjemahan Indonesia, tafsir, indeks surah, dan juz dari Kementerian Agama Republik Indonesia.",
        "Quran text, Indonesian translation, commentary, surah index, and juz data from Indonesia's Ministry of Religious Affairs.",
        ["Quran", "Kemenag", "scripture"],
        ["ar", "id"],
    ),
    "library/islamic-calendar": (
        "Kalender Islam",
        "Islamic Calendar",
        "Bulan Hijriah dan peristiwa penting beserta informasi kepastian tanggal.",
        "Hijri months and important occasions with date-certainty information.",
        ["Islam", "calendar", "Hijri"],
        ["id", "en"],
    ),
    "library/islamic-places": (
        "Tempat Islam",
        "Islamic Places",
        "Lokasi utama terkait ibadah dan sejarah Islam.",
        "Major locations related to Islamic worship and history.",
        ["Islam", "places", "geography"],
        ["id", "en"],
    ),
    "library/manners": (
        "Adab Islami",
        "Islamic Manners",
        "Adab dalam kegiatan sehari-hari, perjalanan, masjid, dan kehidupan sosial.",
        "Manners for daily activities, travel, mosques, and social life.",
        ["Islam", "manners", "adab"],
        ["id", "en"],
    ),
    "library/pillars-of-faith": (
        "Rukun Iman",
        "Pillars of Faith",
        "Ringkasan bilingual enam rukun iman.",
        "A bilingual overview of the six pillars of faith.",
        ["Islam", "belief", "faith"],
        ["id", "en"],
    ),
    "library/pillars-of-islam": (
        "Rukun Islam",
        "Pillars of Islam",
        "Ringkasan dan data pendukung lima rukun Islam.",
        "Overview and supporting data for the five pillars of Islam.",
        ["Islam", "worship", "pillars"],
        ["id", "en", "ar"],
    ),
    "library/prophets": (
        "Nabi dan Rasul",
        "Prophets and Messengers",
        "Data referensi tentang 25 nabi dan rasul.",
        "Reference data about 25 prophets and messengers.",
        ["Islam", "prophets", "reference"],
        ["id", "en"],
    ),
    "library/revealed-books": (
        "Kitab Wahyu",
        "Revealed Books",
        "Informasi tentang kitab-kitab wahyu dalam ajaran Islam.",
        "Information about the revealed books in Islamic teaching.",
        ["Islam", "scripture", "belief"],
        ["id", "en"],
    ),
    "library/sunnah-prayers": (
        "Salat Sunah",
        "Voluntary Prayers",
        "Daftar ringkas salat sunah utama dan konteks pelaksanaannya.",
        "A concise catalog of major voluntary prayers and their context.",
        ["Islam", "worship", "prayer"],
        ["id", "en", "ar"],
    ),
    "library/zakat": (
        "Referensi Zakat",
        "Zakat Reference",
        "Jenis zakat, penerima, zakat fitrah, dan gambaran zakat harta.",
        "Zakat types, recipients, zakat al-fitr, and an overview of zakat on wealth.",
        ["Islam", "worship", "zakat"],
        ["id", "en"],
    ),
    "guides/pillars-of-islam": (
        "Panduan Rukun Islam",
        "Pillars of Islam Guides",
        "Panduan pengantar bilingual untuk makna dan praktik umum lima rukun Islam.",
        "Bilingual introductory guides to the meaning and general practice of the five pillars of Islam.",
        ["Islam", "worship", "learning guide"],
        ["id", "en", "ar"],
    ),
    "guides/prayer": (
        "Panduan Salat",
        "Prayer Guides",
        "Panduan bilingual gerakan dan bacaan salat.",
        "Bilingual guides to prayer movements and recitations.",
        ["Islam", "worship", "prayer guide"],
        ["id", "en", "ar"],
    ),
    "guides/purification": (
        "Panduan Bersuci",
        "Purification Guides",
        "Panduan bilingual tentang wudu, tayamum, mandi wajib, dan bersuci.",
        "Bilingual guides to wudu, tayammum, ritual bathing, and purification.",
        ["Islam", "worship", "purification guide"],
        ["id", "en"],
    ),
    "guides/pilgrimage": (
        "Panduan Haji dan Umrah",
        "Hajj and Umrah Guides",
        "Panduan bilingual manasik haji dan tata cara umrah.",
        "Bilingual guides to Hajj rites and the Umrah procedure.",
        ["Islam", "worship", "pilgrimage", "hajj", "umrah"],
        ["id", "en", "ar"],
    ),
    "guides/zakat": (
        "Panduan Zakat",
        "Zakat Guides",
        "Panduan bilingual zakat fitrah dan zakat harta.",
        "Bilingual guides to zakat al-fitr and zakat on wealth.",
        ["Islam", "worship", "zakat", "guide"],
        ["id", "en"],
    ),
    "guides/fasting": (
        "Panduan Puasa",
        "Fasting Guides",
        "Panduan bilingual untuk mengelola puasa Ramadan yang terlewat.",
        "Bilingual guides for managing missed Ramadan fasts.",
        ["Islam", "worship", "fasting", "guide"],
        ["id", "en"],
    ),
    "guides/daily-worship": (
        "Panduan Ibadah Harian",
        "Daily Worship Guides",
        "Panduan bilingual untuk menggunakan koleksi dzikir dan doa dalam rutinitas ibadah.",
        "Bilingual guides for using dhikr and dua collections in daily worship.",
        ["Islam", "worship", "dhikr", "dua", "guide"],
        ["id", "en", "ar"],
    ),
    "guides/funeral": (
        "Panduan Salat Jenazah",
        "Funeral Prayer Guides",
        "Panduan bilingual salat jenazah dan adab umum pemakaman.",
        "Bilingual guides to the funeral prayer and general funeral etiquette.",
        ["Islam", "worship", "funeral", "guide"],
        ["id", "en", "ar"],
    ),
    "guides/learning": (
        "Panduan Belajar Islam",
        "Islamic Learning Guides",
        "Panduan bilingual belajar dasar Islam dan Asmaul Husna.",
        "Bilingual guides for learning Islamic basics and Asma ul Husna.",
        ["Islam", "learning", "education", "guide"],
        ["id", "en", "ar"],
    ),
    "guides/quran": (
        "Panduan Membaca Al-Qur'an",
        "Quran Reading Guides",
        "Panduan bilingual untuk memulai membaca dan memahami Al-Qur'an.",
        "Bilingual guides for beginning Quran reading and understanding.",
        ["Quran", "learning", "reading", "guide"],
        ["id", "en", "ar"],
    ),
}

RELATED_COLLECTIONS = {
    "library/dhikr": ["guides/daily-worship"],
    "library/dua": ["guides/daily-worship"],
    "library/asmaul-husna": ["guides/learning"],
    "library/fasting": ["guides/fasting", "guides/pillars-of-islam"],
    "library/holy-quran": ["guides/quran", "guides/learning"],
    "library/pillars-of-islam": ["guides/pillars-of-islam"],
    "library/sunnah-prayers": ["guides/prayer"],
    "library/zakat": ["guides/zakat", "guides/pillars-of-islam"],
    "library/pillars-of-faith": ["guides/learning"],
    "guides/daily-worship": ["library/dhikr", "library/dua"],
    "guides/fasting": ["library/fasting", "library/zakat"],
    "guides/funeral": ["library/manners", "guides/prayer"],
    "guides/learning": [
        "library/asmaul-husna",
        "library/holy-quran",
        "library/pillars-of-faith",
        "library/pillars-of-islam",
    ],
    "guides/pilgrimage": [
        "library/islamic-places",
        "library/islamic-calendar",
        "library/pillars-of-islam",
    ],
    "guides/pillars-of-islam": [
        "library/pillars-of-islam",
        "guides/prayer",
        "guides/zakat",
        "guides/fasting",
        "guides/pilgrimage",
    ],
    "guides/prayer": ["library/sunnah-prayers", "guides/purification", "library/dhikr"],
    "guides/purification": ["guides/prayer"],
    "guides/quran": ["library/holy-quran", "library/dhikr"],
    "guides/zakat": ["library/zakat", "guides/pillars-of-islam"],
}


def localized_text(indonesian, english):
    return [
        {"@value": indonesian, "@language": "id"},
        {"@value": english, "@language": "en"},
    ]


def build_catalog():
    collection_paths = {
        path.relative_to(ROOT).as_posix()
        for parent in (ROOT / "library", ROOT / "guides")
        for path in parent.iterdir()
        if path.is_dir()
    }
    unregistered = collection_paths - COLLECTIONS.keys()
    missing = COLLECTIONS.keys() - collection_paths
    if unregistered or missing:
        raise ValueError(
            f"Catalog metadata mismatch; unregistered={sorted(unregistered)}, "
            f"missing={sorted(missing)}"
        )

    datasets = []
    for collection_id, metadata in COLLECTIONS.items():
        collection_path = ROOT / collection_id
        if not collection_path.is_dir():
            raise FileNotFoundError(
                f"Missing catalog collection directory: {collection_id}"
            )

        name_id, name_en, description_id, description_en, keywords, languages = metadata
        relative_files = sorted(
            path.relative_to(ROOT).as_posix()
            for path in collection_path.rglob("*.json")
            if path.name not in {"catalog.json", "catalog.schema.json"}
        )
        if not relative_files:
            raise ValueError(f"No JSON data files found in {collection_id}")

        distributions = [
            {
                "@type": "DataDownload",
                "name": Path(path).relative_to(collection_id).as_posix(),
                "contentUrl": f"{CDN_BASE}/{path}",
                "encodingFormat": "application/json",
            }
            for path in relative_files
        ]
        related_paths = RELATED_COLLECTIONS.get(collection_id, [])
        unknown_related = set(related_paths) - collection_paths
        if unknown_related:
            raise ValueError(
                f"Unknown related collection(s) for {collection_id}: {sorted(unknown_related)}"
            )
        datasets.append(
            {
                "@type": "Dataset",
                "@id": f"{CATALOG_ID}#{collection_id.replace('/', '-')}",
                "identifier": collection_id,
                "name": localized_text(name_id, name_en),
                "description": localized_text(description_id, description_en),
                "url": f"{REPOSITORY}/tree/main/{collection_id}",
                "license": LICENSE_URL,
                "inLanguage": languages,
                "keywords": keywords,
                "relatedLink": [
                    f"{REPOSITORY}/tree/main/{path}" for path in related_paths
                ],
                "distribution": distributions,
            }
        )

    return {
        "@context": "https://schema.org",
        "@type": "DataCatalog",
        "name": localized_text(
            "Katalog Data Islamic JSON", "Islamic JSON Data Catalog"
        ),
        "description": localized_text(
            "Indeks dataset Islam bilingual beserta endpoint JSON yang dapat dikonsumsi.",
            "An index of bilingual Islamic datasets and their machine-readable JSON endpoints.",
        ),
        "url": REPOSITORY,
        "dataset": datasets,
    }


def main():
    output_path = ROOT / "catalog.json"
    output_path.write_text(
        json.dumps(build_catalog(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
