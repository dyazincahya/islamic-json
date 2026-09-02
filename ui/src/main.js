import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBookOpen,
  faBookQuran,
  faCalendarDays,
  faChevronDown,
  faCode,
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
  faMoon,
  faMosque,
  faPersonPraying,
  faScaleBalanced,
  faShieldHeart,
  faStarAndCrescent,
  faUserCheck,
  faUsers,
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
  faMoon,
  faMosque,
  faPersonPraying,
  faScaleBalanced,
  faShieldHeart,
  faStarAndCrescent,
  faUserCheck,
  faUsers,
);

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(router)
  .mount("#app");
