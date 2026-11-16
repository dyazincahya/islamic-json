import asmaulHusna from "../../data/library/asmaul-husna/asmaul-husna.json";
import dua from "../../data/library/dua/data/daily-dua.json";
import pillarsOfFaith from "../../data/library/pillars-of-faith/main.json";
import surahList from "../../data/library/holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah.json";

const pillarModules = import.meta.glob(
  "../../data/library/pillars-of-islam/**/*.json",
  {
    import: "default",
  },
);
const pillarCategoryOrder = ["shahada", "salah", "zakat", "fasting", "hajj"];
const salahOrder = [
  "subuh.json",
  "dhuhr.json",
  "asr.json",
  "maghrib.json",
  "isha.json",
];
const surahModules = import.meta.glob(
  "../../data/library/holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/*.json",
  { import: "default" },
);
const knowledgeModules = import.meta.glob(
  [
    "../../data/library/dhikr/**/*.json",
    "../../data/guides/prayer/**/*.json",
    "../../data/guides/pillars-of-islam/**/*.json",
    "../../data/library/sunnah-prayers/**/*.json",
    "../../data/guides/purification/**/*.json",
    "../../data/library/angels/**/*.json",
    "../../data/library/revealed-books/**/*.json",
    "../../data/library/prophets/**/*.json",
    "../../data/library/islamic-calendar/**/*.json",
    "../../data/library/islamic-places/**/*.json",
    "../../data/library/zakat/**/*.json",
    "../../data/library/fasting/**/*.json",
    "../../data/library/manners/**/*.json",
  ],
  { import: "default" },
);

export const sections = [
  { id: "home", label: { id: "Beranda", en: "Home" }, icon: "house" },
  { id: "quran", label: { id: "Al-Qur’an", en: "Qur’an" }, icon: "book-quran" },
  {
    id: "dua",
    label: { id: "Doa Harian", en: "Daily Dua" },
    icon: "hands-praying",
  },
  {
    id: "asmaul",
    label: { id: "Asmaul Husna", en: "Beautiful Names" },
    icon: "star-and-crescent",
  },
  {
    id: "pillars",
    label: { id: "Rukun Islam", en: "Pillars of Islam" },
    icon: "kaaba",
  },
  {
    id: "faith",
    label: { id: "Rukun Iman", en: "Pillars of Faith" },
    icon: "shield-heart",
  },
  {
    id: "library",
    label: { id: "Pustaka", en: "Library" },
    icon: "layer-group",
  },
  {
    id: "relationships",
    label: { id: "Relasi Data", en: "Data Relations" },
    icon: "diagram-project",
  },
  {
    id: "developer",
    label: { id: "Developer API", en: "Developer API" },
    icon: "code",
  },
];

export const stats = {
  surah: surahList.length,
  ayah: surahList.reduce((sum, surah) => sum + surah.num_ayah, 0),
  dua: dua.length,
  asmaul: asmaulHusna.length,
};

export const getAsmaulHusna = () => asmaulHusna;
export const getDua = () => dua;
export const getPillarsOfFaith = () => pillarsOfFaith;
export const getSurahList = () => surahList;

export const knowledgeCollections = [
  {
    id: "dhikr",
    icon: "hands-praying",
    title: { id: "Dzikir", en: "Dhikr" },
    description: {
      id: "Dzikir pagi, petang, setelah salat, dan umum.",
      en: "Morning, evening, after-prayer, and general remembrance.",
    },
    files: [
      {
        id: "categories",
        title: { id: "Kategori Dzikir", en: "Dhikr Categories" },
        path: "library/dhikr/categories.json",
      },
      {
        id: "morning",
        title: { id: "Dzikir Pagi", en: "Morning Dhikr" },
        path: "library/dhikr/data/morning-dhikr.json",
      },
      {
        id: "evening",
        title: { id: "Dzikir Petang", en: "Evening Dhikr" },
        path: "library/dhikr/data/evening-dhikr.json",
      },
      {
        id: "after-prayer",
        title: { id: "Setelah Salat", en: "After Prayer" },
        path: "library/dhikr/data/after-prayer-dhikr.json",
      },
      {
        id: "general",
        title: { id: "Dzikir Umum", en: "General Dhikr" },
        path: "library/dhikr/data/general-dhikr.json",
      },
    ],
  },
  {
    id: "prayer-guide",
    icon: "person-praying",
    title: { id: "Panduan Salat", en: "Prayer Guide" },
    description: {
      id: "Urutan gerakan dan bacaan salat wajib.",
      en: "Sequence of obligatory prayer movements and recitations.",
    },
    files: [
      {
        id: "obligatory",
        title: { id: "Salat Wajib", en: "Obligatory Prayer" },
        path: "guides/prayer/data/obligatory-prayer.json",
      },
      {
        id: "voluntary",
        title: { id: "Salat Sunah", en: "Voluntary Prayers" },
        path: "guides/prayer/voluntary-prayers.json",
      },
      {
        id: "eid",
        title: { id: "Salat Id", en: "Eid Prayer" },
        path: "guides/prayer/eid-prayer.json",
      },
    ],
  },
  {
    id: "pillars-of-islam-guide",
    icon: "kaaba",
    title: { id: "Panduan Rukun Islam", en: "Pillars of Islam Guides" },
    description: {
      id: "Pengantar makna dan praktik umum lima rukun Islam.",
      en: "An introduction to the meaning and general practice of the five pillars of Islam.",
    },
    files: [
      {
        id: "shahada",
        title: { id: "Syahadat", en: "Shahada" },
        path: "guides/pillars-of-islam/shahada.json",
      },
      {
        id: "salah",
        title: { id: "Salat", en: "Salah" },
        path: "guides/pillars-of-islam/salah.json",
      },
      {
        id: "zakat",
        title: { id: "Zakat", en: "Zakat" },
        path: "guides/pillars-of-islam/zakat.json",
      },
      {
        id: "fasting",
        title: { id: "Puasa", en: "Fasting" },
        path: "guides/pillars-of-islam/fasting.json",
      },
      {
        id: "hajj",
        title: { id: "Haji", en: "Hajj" },
        path: "guides/pillars-of-islam/hajj.json",
      },
    ],
  },
  {
    id: "sunnah-prayers",
    icon: "mosque",
    title: { id: "Salat Sunah", en: "Sunnah Prayers" },
    description: {
      id: "Ringkasan berbagai salat sunah utama.",
      en: "Overview of major voluntary prayers.",
    },
    files: [
      {
        id: "main",
        title: { id: "Salat Sunah", en: "Sunnah Prayers" },
        path: "library/sunnah-prayers/data/sunnah-prayers.json",
      },
    ],
  },
  {
    id: "purification",
    icon: "droplet",
    title: { id: "Bersuci", en: "Purification" },
    description: {
      id: "Wudu, tayamum, mandi wajib, dan najis.",
      en: "Wudu, tayammum, ritual bath, and impurities.",
    },
    files: [
      {
        id: "wudu",
        title: { id: "Wudu", en: "Wudu" },
        path: "guides/purification/wudu.json",
      },
      {
        id: "tayammum",
        title: { id: "Tayamum", en: "Tayammum" },
        path: "guides/purification/tayammum.json",
      },
      {
        id: "ghusl",
        title: { id: "Mandi Wajib", en: "Ritual Bath" },
        path: "guides/purification/ghusl.json",
      },
      {
        id: "impurities",
        title: { id: "Najis", en: "Impurities" },
        path: "guides/purification/impurities.json",
      },
      {
        id: "wudu-procedure",
        title: { id: "Tata Cara Wudu", en: "Wudu Procedure" },
        path: "guides/purification/wudu-procedure.json",
      },
      {
        id: "tayammum-procedure",
        title: { id: "Tata Cara Tayamum", en: "Tayammum Procedure" },
        path: "guides/purification/tayammum-procedure.json",
      },
      {
        id: "ghusl-procedure",
        title: { id: "Tata Cara Mandi Wajib", en: "Ritual Bath Procedure" },
        path: "guides/purification/ghusl-procedure.json",
      },
    ],
  },
  {
    id: "angels",
    icon: "feather",
    title: { id: "Malaikat", en: "Angels" },
    description: {
      id: "Malaikat yang disebut dalam Al-Qur’an.",
      en: "Angels named in the Quran.",
    },
    files: [
      {
        id: "main",
        title: { id: "Malaikat", en: "Angels" },
        path: "library/angels/angels.json",
      },
    ],
  },
  {
    id: "revealed-books",
    icon: "book-open",
    title: { id: "Kitab Allah", en: "Revealed Books" },
    description: {
      id: "Empat kitab wahyu utama.",
      en: "The four principal revealed books.",
    },
    files: [
      {
        id: "main",
        title: { id: "Kitab Allah", en: "Revealed Books" },
        path: "library/revealed-books/revealed-books.json",
      },
    ],
  },
  {
    id: "prophets",
    icon: "users",
    title: { id: "Nabi dan Rasul", en: "Prophets" },
    description: {
      id: "Metadata 25 nabi dan rasul.",
      en: "Metadata for 25 prophets and messengers.",
    },
    files: [
      {
        id: "main",
        title: { id: "Nabi dan Rasul", en: "Prophets" },
        path: "library/prophets/prophets.json",
      },
    ],
  },
  {
    id: "islamic-calendar",
    icon: "calendar-days",
    title: { id: "Kalender Islam", en: "Islamic Calendar" },
    description: {
      id: "Bulan Hijriah dan peristiwa penting.",
      en: "Hijri months and important occasions.",
    },
    files: [
      {
        id: "main",
        title: { id: "Kalender Islam", en: "Islamic Calendar" },
        path: "library/islamic-calendar/calendar.json",
      },
    ],
  },
  {
    id: "islamic-places",
    icon: "location-dot",
    title: { id: "Tempat Islam", en: "Islamic Places" },
    description: {
      id: "Lokasi utama terkait ibadah dan sejarah Islam.",
      en: "Major locations related to worship and Islamic history.",
    },
    files: [
      {
        id: "main",
        title: { id: "Tempat Islam", en: "Islamic Places" },
        path: "library/islamic-places/places.json",
      },
    ],
  },
  {
    id: "zakat",
    icon: "hand-holding-heart",
    title: { id: "Zakat", en: "Zakat" },
    description: {
      id: "Jenis, penerima, fitrah, dan zakat harta.",
      en: "Types, recipients, fitrah, and wealth zakat.",
    },
    files: [
      {
        id: "categories",
        title: { id: "Jenis Zakat", en: "Zakat Types" },
        path: "library/zakat/categories.json",
      },
      {
        id: "recipients",
        title: { id: "Penerima Zakat", en: "Recipients" },
        path: "library/zakat/recipients.json",
      },
      {
        id: "fitrah",
        title: { id: "Zakat Fitrah", en: "Zakat al-Fitr" },
        path: "library/zakat/fitrah.json",
      },
      {
        id: "wealth",
        title: { id: "Zakat Harta", en: "Wealth Zakat" },
        path: "library/zakat/wealth-overview.json",
      },
    ],
  },
  {
    id: "fasting",
    icon: "moon",
    title: { id: "Puasa", en: "Fasting" },
    description: {
      id: "Jenis, pembatal, keringanan, dan amalan puasa.",
      en: "Types, invalidators, exemptions, and recommended acts.",
    },
    files: [
      {
        id: "types",
        title: { id: "Jenis Puasa", en: "Fasting Types" },
        path: "library/fasting/types.json",
      },
      {
        id: "invalidators",
        title: { id: "Pembatal Puasa", en: "Invalidators" },
        path: "library/fasting/invalidators.json",
      },
      {
        id: "exemptions",
        title: { id: "Keringanan", en: "Exemptions" },
        path: "library/fasting/exemptions.json",
      },
      {
        id: "recommended",
        title: { id: "Amalan Dianjurkan", en: "Recommended Acts" },
        path: "library/fasting/recommended-actions.json",
      },
    ],
  },
  {
    id: "pilgrimage-guides",
    icon: "kaaba",
    title: { id: "Haji dan Umrah", en: "Hajj and Umrah" },
    description: {
      id: "Panduan manasik haji dan tata cara umrah.",
      en: "Guides to Hajj rites and Umrah.",
    },
    files: [
      {
        id: "hajj",
        title: { id: "Panduan Haji", en: "Hajj Guide" },
        path: "guides/pilgrimage/hajj.json",
      },
      {
        id: "umrah",
        title: { id: "Panduan Umrah", en: "Umrah Guide" },
        path: "guides/pilgrimage/umrah.json",
      },
    ],
  },
  {
    id: "zakat-guides",
    icon: "hand-holding-heart",
    title: { id: "Panduan Zakat", en: "Zakat Guides" },
    description: {
      id: "Panduan zakat fitrah dan zakat harta.",
      en: "Guides to zakat al-fitr and zakat on wealth.",
    },
    files: [
      {
        id: "fitrah",
        title: { id: "Zakat Fitrah", en: "Zakat al-Fitr" },
        path: "guides/zakat/fitrah.json",
      },
      {
        id: "wealth",
        title: { id: "Zakat Harta", en: "Zakat on Wealth" },
        path: "guides/zakat/wealth.json",
      },
    ],
  },
  {
    id: "daily-worship-guides",
    icon: "hands-praying",
    title: { id: "Ibadah Harian", en: "Daily Worship" },
    description: {
      id: "Panduan menggunakan koleksi dzikir dan doa.",
      en: "Guides for using dhikr and dua collections.",
    },
    files: [
      {
        id: "after-prayer-dhikr",
        title: { id: "Dzikir Setelah Salat", en: "After-Prayer Dhikr" },
        path: "guides/daily-worship/dhikr-after-prayer.json",
      },
    ],
  },
  {
    id: "fasting-guides",
    icon: "moon",
    title: { id: "Panduan Puasa", en: "Fasting Guides" },
    description: {
      id: "Panduan mengganti puasa Ramadan.",
      en: "Guide to making up missed Ramadan fasts.",
    },
    files: [
      {
        id: "make-up-fasts",
        title: { id: "Mengganti Puasa", en: "Make-up Fasts" },
        path: "guides/fasting/make-up-fasts.json",
      },
    ],
  },
  {
    id: "funeral-guides",
    icon: "person-praying",
    title: { id: "Salat Jenazah", en: "Funeral Prayer" },
    description: {
      id: "Panduan umum salat jenazah.",
      en: "General funeral prayer guide.",
    },
    files: [
      {
        id: "janazah",
        title: { id: "Salat Jenazah", en: "Funeral Prayer" },
        path: "guides/funeral/janazah-prayer.json",
      },
    ],
  },
  {
    id: "learning-guides",
    icon: "book-open",
    title: { id: "Belajar Islam", en: "Islamic Learning" },
    description: {
      id: "Panduan belajar dasar Islam dan Asmaul Husna.",
      en: "Guides to Islamic basics and Asma ul Husna.",
    },
    files: [
      {
        id: "new-muslim",
        title: {
          id: "Belajar Dasar bagi Muslim Baru",
          en: "Learning Path for New Muslims",
        },
        path: "guides/learning/new-muslim.json",
      },
      {
        id: "asmaul-husna",
        title: { id: "Belajar Asmaul Husna", en: "Learning Asma ul Husna" },
        path: "guides/learning/asmaul-husna.json",
      },
    ],
  },
  {
    id: "quran-guides",
    icon: "book-quran",
    title: { id: "Belajar Al-Qur'an", en: "Quran Learning" },
    description: {
      id: "Panduan memulai membaca Al-Qur'an.",
      en: "Guide to starting Quran reading.",
    },
    files: [
      {
        id: "reading-quran",
        title: { id: "Membaca Al-Qur'an", en: "Reading the Quran" },
        path: "guides/quran/reading-quran.json",
      },
    ],
  },
  {
    id: "manners",
    icon: "heart",
    title: { id: "Adab", en: "Manners" },
    description: {
      id: "Adab makan, tidur, masjid, perjalanan, bertamu, dan sosial.",
      en: "Manners of eating, sleeping, mosque, travel, visiting, and social life.",
    },
    files: [
      {
        id: "eating",
        title: { id: "Makan", en: "Eating" },
        path: "library/manners/eating.json",
      },
      {
        id: "sleeping",
        title: { id: "Tidur", en: "Sleeping" },
        path: "library/manners/sleeping.json",
      },
      {
        id: "mosque",
        title: { id: "Masjid", en: "Mosque" },
        path: "library/manners/mosque.json",
      },
      {
        id: "travelling",
        title: { id: "Perjalanan", en: "Travelling" },
        path: "library/manners/travelling.json",
      },
      {
        id: "visiting",
        title: { id: "Bertamu", en: "Visiting" },
        path: "library/manners/visiting.json",
      },
      {
        id: "social",
        title: { id: "Sosial", en: "Social" },
        path: "library/manners/social.json",
      },
    ],
  },
];

export async function getKnowledgeFile(path) {
  const loader = knowledgeModules[`../../data/${path}`];
  if (!loader) throw new Error(`Knowledge file not found: ${path}`);
  return loader();
}

export async function getSurah(number) {
  const key = `../../data/library/holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${number}.json`;
  const loader = surahModules[key];
  if (!loader) throw new Error(`Surah module not found: ${number}`);
  const data = await loader();
  const surah = data[String(number)];
  if (!surah) throw new Error(`Invalid surah data: ${number}`);
  return surah;
}

export async function getPillars() {
  const entries = await Promise.all(
    Object.entries(pillarModules).map(async ([path, loader]) => {
      const data = await loader();
      const relativePath = path.replace(
        "../../data/library/pillars-of-islam/",
        "",
      );
      const [category] = relativePath.split("/");
      const records = Array.isArray(data) ? data : [data];
      return records.map((record, index) => ({
        ...record,
        category,
        path: `library/pillars-of-islam/${relativePath}`,
        key: `${relativePath}-${index}`,
      }));
    }),
  );
  return entries.flat().sort((first, second) => {
    const categoryDifference =
      pillarCategoryOrder.indexOf(first.category) -
      pillarCategoryOrder.indexOf(second.category);
    if (categoryDifference !== 0) return categoryDifference;
    if (first.category === "salah") {
      const firstFile = first.path.split("/").at(-1);
      const secondFile = second.path.split("/").at(-1);
      return salahOrder.indexOf(firstFile) - salahOrder.indexOf(secondFile);
    }
    return first.path.localeCompare(second.path);
  });
}

export function localized(value, locale = "id") {
  if (value == null) return "";
  if (typeof value === "object")
    return value[locale] ?? value.id ?? value.en ?? "";
  return value;
}

export const repositoryUrl = "https://github.com/dyazincahya/islamic-json";
export const rawUrl = (path) => `${repositoryUrl}/blob/main/${path}`;
export const apiUrl = (source) => {
  const githubFileUrl = source.startsWith("http") ? source : rawUrl(source);
  return `https://gitcdn-generator.vercel.app?q=${githubFileUrl}`;
};
