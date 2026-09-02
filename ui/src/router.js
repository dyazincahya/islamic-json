import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("./components/pages/home/HomePage.vue"),
    meta: { section: "home" },
  },
  {
    path: "/quran/:surah?",
    name: "quran",
    component: () => import("./components/pages/quran/QuranPage.vue"),
    meta: { section: "quran" },
  },
  {
    path: "/dua",
    name: "dua",
    component: () => import("./components/pages/dua/DuaPage.vue"),
    meta: { section: "dua" },
  },
  {
    path: "/asmaul-husna",
    name: "asmaul",
    component: () =>
      import("./components/pages/asmaul-husna/AsmaulHusnaPage.vue"),
    meta: { section: "asmaul" },
  },
  {
    path: "/pillars-of-islam",
    name: "pillars",
    component: () => import("./components/pages/pillars/PillarsPage.vue"),
    meta: { section: "pillars" },
  },
  {
    path: "/pillars-of-faith",
    name: "faith",
    component: () => import("./components/pages/faith/FaithPage.vue"),
    meta: { section: "faith" },
  },
  {
    path: "/library/:collection?/:file?",
    name: "library",
    component: () =>
      import("./components/pages/library/KnowledgeLibraryPage.vue"),
    meta: { section: "library" },
  },
  {
    path: "/relationships",
    name: "relationships",
    component: () =>
      import("./components/pages/relationships/DataRelationshipsPage.vue"),
    meta: { section: "relationships" },
  },
  {
    path: "/developer",
    name: "developer",
    component: () => import("./components/pages/developer/DeveloperPage.vue"),
    meta: { section: "developer" },
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

export default createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});
