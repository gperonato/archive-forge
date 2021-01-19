import Vue from "vue";
import App from "./App.vue";

import Buefy from "buefy";
import "buefy/dist/buefy.css";

import VueConfetti from "vue-confetti";

import uploader from "vue-simple-uploader";

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueConfetti);
Vue.use(uploader);

new Vue({
  render: (h) => h(App)
}).$mount("#app");
