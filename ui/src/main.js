import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBookOpen,
  faBookQuran,
  faChevronDown,
  faCode,
  faFeather,
  faHandsPraying,
  faHourglassHalf,
  faHouse,
  faKaaba,
  faScaleBalanced,
  faShieldHeart,
  faStarAndCrescent,
  faUserCheck,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./style.css";

library.add(
  faBookOpen,
  faBookQuran,
  faChevronDown,
  faCode,
  faFeather,
  faHandsPraying,
  faHourglassHalf,
  faHouse,
  faKaaba,
  faScaleBalanced,
  faShieldHeart,
  faStarAndCrescent,
  faUserCheck,
);

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(router)
  .mount("#app");
