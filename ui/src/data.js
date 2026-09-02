import asmaulHusna from "../../asmaul-husna/asmaul-husna.json";
import dua from "../../dua/data/daily-dua.json";
import pillarsOfFaith from "../../pillars-of-faith/main.json";
import surahList from "../../holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah.json";

const pillarModules = import.meta.glob("../../pillars-of-islam/**/*.json", {
  import: "default",
});
const pillarCategoryOrder = ["shahada", "salah", "zakat", "fasting", "hajj"];
const salahOrder = [
  "subuh.json",
  "dhuhr.json",
  "asr.json",
  "maghrib.json",
  "isha.json",
];
const surahModules = import.meta.glob(
  "../../holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/*.json",
  { import: "default" },
);
const knowledgeModules = import.meta.glob(
  [
    "../../dhikr/**/*.json",
    "../../prayer-guide/**/*.json",
    "../../sunnah-prayers/**/*.json",
    "../../purification/**/*.json",
    "../../angels/**/*.json",
    "../../revealed-books/**/*.json",
    "../../prophets/**/*.json",
    "../../islamic-calendar/**/*.json",
    "../../islamic-places/**/*.json",
    "../../zakat/**/*.json",
    "../../fasting/**/*.json",
    "../../manners/**/*.json",
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
        path: "dhikr/categories.json",
      },
      {
        id: "morning",
        title: { id: "Dzikir Pagi", en: "Morning Dhikr" },
        path: "dhikr/data/morning-dhikr.json",
      },
      {
        id: "evening",
        title: { id: "Dzikir Petang", en: "Evening Dhikr" },
        path: "dhikr/data/evening-dhikr.json",
      },
      {
        id: "after-prayer",
        title: { id: "Setelah Salat", en: "After Prayer" },
        path: "dhikr/data/after-prayer-dhikr.json",
      },
      {
        id: "general",
        title: { id: "Dzikir Umum", en: "General Dhikr" },
        path: "dhikr/data/general-dhikr.json",
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
        path: "prayer-guide/data/obligatory-prayer.json",
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
        path: "sunnah-prayers/data/sunnah-prayers.json",
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
        path: "purification/wudu.json",
      },
      {
        id: "tayammum",
        title: { id: "Tayamum", en: "Tayammum" },
        path: "purification/tayammum.json",
      },
      {
        id: "ghusl",
        title: { id: "Mandi Wajib", en: "Ritual Bath" },
        path: "purification/ghusl.json",
      },
      {
        id: "impurities",
        title: { id: "Najis", en: "Impurities" },
        path: "purification/impurities.json",
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
        path: "angels/angels.json",
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
        path: "revealed-books/revealed-books.json",
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
        path: "prophets/prophets.json",
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
        path: "islamic-calendar/calendar.json",
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
        path: "islamic-places/places.json",
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
        path: "zakat/categories.json",
      },
      {
        id: "recipients",
        title: { id: "Penerima Zakat", en: "Recipients" },
        path: "zakat/recipients.json",
      },
      {
        id: "fitrah",
        title: { id: "Zakat Fitrah", en: "Zakat al-Fitr" },
        path: "zakat/fitrah.json",
      },
      {
        id: "wealth",
        title: { id: "Zakat Harta", en: "Wealth Zakat" },
        path: "zakat/wealth-overview.json",
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
        path: "fasting/types.json",
      },
      {
        id: "invalidators",
        title: { id: "Pembatal Puasa", en: "Invalidators" },
        path: "fasting/invalidators.json",
      },
      {
        id: "exemptions",
        title: { id: "Keringanan", en: "Exemptions" },
        path: "fasting/exemptions.json",
      },
      {
        id: "recommended",
        title: { id: "Amalan Dianjurkan", en: "Recommended Acts" },
        path: "fasting/recommended-actions.json",
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
        path: "manners/eating.json",
      },
      {
        id: "sleeping",
        title: { id: "Tidur", en: "Sleeping" },
        path: "manners/sleeping.json",
      },
      {
        id: "mosque",
        title: { id: "Masjid", en: "Mosque" },
        path: "manners/mosque.json",
      },
      {
        id: "travelling",
        title: { id: "Perjalanan", en: "Travelling" },
        path: "manners/travelling.json",
      },
      {
        id: "visiting",
        title: { id: "Bertamu", en: "Visiting" },
        path: "manners/visiting.json",
      },
      {
        id: "social",
        title: { id: "Sosial", en: "Social" },
        path: "manners/social.json",
      },
    ],
  },
];

export async function getKnowledgeFile(path) {
  const loader = knowledgeModules[`../../${path}`];
  if (!loader) throw new Error(`Knowledge file not found: ${path}`);
  return loader();
}

export async function getSurah(number) {
  const key = `../../holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${number}.json`;
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
      const relativePath = path.replace("../../pillars-of-islam/", "");
      const [category] = relativePath.split("/");
      const records = Array.isArray(data) ? data : [data];
      return records.map((record, index) => ({
        ...record,
        category,
        path: `pillars-of-islam/${relativePath}`,
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
