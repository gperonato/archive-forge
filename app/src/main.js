import Vue from "vue";
import App from "./App.vue";

import Buefy from "buefy";
import "buefy/dist/buefy.css";

import VueConfetti from "vue-confetti";

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueConfetti);

new Vue({
  render: (h) => h(App)
}).$mount("#app");
