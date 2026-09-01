import asmaulHusna from "../../asmaul-husna/asmaul-husna.json";
import dua from "../../dua/data/daily-dua.json";
import surahList from "../../holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah.json";

const pillarModules = import.meta.glob("../../pillars-of-islam/**/*.json");
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
);

export const sections = [
  { id: "home", label: { id: "Beranda", en: "Home" }, icon: "⌂" },
  { id: "quran", label: { id: "Al-Qur’an", en: "Qur’an" }, icon: "۞" },
  { id: "dua", label: { id: "Doa Harian", en: "Daily Dua" }, icon: "☾" },
  {
    id: "asmaul",
    label: { id: "Asmaul Husna", en: "Beautiful Names" },
    icon: "◈",
  },
  {
    id: "pillars",
    label: { id: "Rukun Islam", en: "Pillars of Islam" },
    icon: "◆",
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
export const getSurahList = () => surahList;

export async function getSurah(number) {
  const key = `../../holy-quran/ministry-of-religion-of-the-republic-of-indonesia/surah/${number}.json`;
  const module = await surahModules[key]();
  return module.default[String(number)];
}

export async function getPillars() {
  const entries = await Promise.all(
    Object.entries(pillarModules).map(async ([path, loader]) => {
      const module = await loader();
      const relativePath = path.replace("../../pillars-of-islam/", "");
      const [category] = relativePath.split("/");
      const records = Array.isArray(module.default)
        ? module.default
        : [module.default];
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
