import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBookOpen,
  faBookQuran,
  faCalendarDays,
  faChevronDown,
  faCode,
  faDiagramProject,
  faDroplet,
  faFeather,
  faHandHoldingHeart,
  faHandsPraying,
  faHeart,
  faHourglassHalf,
  faHouse,
  faKaaba,
  faLayerGroup,
  faLocationDot,
  faMagnifyingGlassMinus,
  faMagnifyingGlassPlus,
  faMoon,
  faMosque,
  faPersonPraying,
  faRotateLeft,
  faScaleBalanced,
  faShieldHeart,
  faStarAndCrescent,
  faUserCheck,
  faUsers,
  faExpand,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./style.css";

library.add(
  faBookOpen,
  faBookQuran,
  faCalendarDays,
  faChevronDown,
  faCode,
  faDiagramProject,
  faDroplet,
  faFeather,
  faHandHoldingHeart,
  faHandsPraying,
  faHeart,
  faHourglassHalf,
  faHouse,
  faKaaba,
  faLayerGroup,
  faLocationDot,
  faMagnifyingGlassMinus,
  faMagnifyingGlassPlus,
  faMoon,
  faMosque,
  faPersonPraying,
  faRotateLeft,
  faScaleBalanced,
  faShieldHeart,
  faStarAndCrescent,
  faUserCheck,
  faUsers,
  faExpand,
);

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(router)
  .mount("#app");
