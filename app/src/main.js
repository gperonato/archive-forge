import Vue from "vue";
import VueConfetti from "vue-confetti";
import Buefy from "buefy";
import "buefy/dist/buefy.css";
import uploader from "vue-simple-uploader";
import datapackage from "datapackage";

import App from "./App.vue";

Vue.config.productionTip = false;

Vue.use(Buefy);
Vue.use(VueConfetti);
Vue.use(uploader);
Vue.use(datapackage);

new Vue({
  render: (h) => h(App)
}).$mount("#app");
