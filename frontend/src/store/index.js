import Vue from "vue";
import Vuex from "vuex";
import filters from "./modules/filter";
import table from "./modules/table";
import selection from "./modules/selection";
import common from "./modules/common";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    common,
    filters,
    table,
    selection,
  },
});
