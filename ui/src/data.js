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
