import { defineConfig } from "vitepress";

const isCustomDomain = process.env.DOCS_CUSTOM_DOMAIN === "true";

export default defineConfig({
  title: "Islamic JSON",
  description: "Dokumentasi dan penjelajah data Islamic JSON",
  base: isCustomDomain ? "/" : "/islamic-json/",
  cleanUrls: true,
  lastUpdated: true,
  lang: "id-ID",
  head: [["meta", { name: "theme-color", content: "#0d1117" }]],
  themeConfig: {
    search: { provider: "local" },
    nav: [
      { text: "Dokumentasi", link: "/guide/getting-started" },
      { text: "Demo UI", link: "/demo/" },
      { text: "Jelajahi data", link: "/explorer/" },
      { text: "API & CDN", link: "/api/" },
      { text: "Migrasi", link: "/migration/" },
    ],
    sidebar: {
      "/guide/": [
        {
          text: "Panduan",
          items: [
            { text: "Memulai", link: "/guide/getting-started" },
            { text: "Lokalisasi", link: "/guide/localization" },
          ],
        },
      ],
      "/reference/": [
        {
          text: "Referensi",
          items: [
            { text: "Model data", link: "/reference/data-model" },
            { text: "Registry", link: "/reference/registries" },
          ],
        },
      ],
      "/explorer/": [
        {
          text: "Penjelajah",
          items: [
            { text: "Dashboard", link: "/explorer/" },
            { text: "Koleksi", link: "/explorer/collections" },
            { text: "Journey", link: "/explorer/journey" },
          ],
        },
      ],
      "/demo/": [
        {
          text: "Demo UI",
          items: [{ text: "Multi-dataset browser", link: "/demo/" }],
        },
      ],
      "/api/": [
        { text: "API & CDN", items: [{ text: "API explorer", link: "/api/" }] },
      ],
      "/migration/": [
        {
          text: "Migrasi",
          items: [{ text: "Data layout", link: "/migration/" }],
        },
      ],
      "/contributing/": [
        {
          text: "Kontribusi",
          items: [{ text: "Panduan kontribusi", link: "/contributing/" }],
        },
      ],
    },
    socialLinks: [
      { icon: "github", link: "https://github.com/dyazincahya/islamic-json" },
    ],
    footer: {
      message:
        "Data teknis tervalidasi tidak sama dengan persetujuan keilmuan.",
      copyright: "MIT License",
    },
  },
});
