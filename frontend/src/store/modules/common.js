import APIClass from "../../api/ApiUtils.js";
const API = new APIClass();

export default {
  actions: {
    fetchSidebarItems(ctx) {
      console.log("[API info]", API);
      API.getSidebarItems().then((data) => {
        ctx.commit("updateSidebarItems", data);
      });
    },
  },
  mutations: {
    updateSidebarItems(state, items) {
      state.sidebar.items = items;
    },
    updateObj(state, { obj, key, data }) {
      this.$app.$set(obj, key, data);
    },
  },
  state: {
    sidebar: {
      items: [],
    },
  },
  getters: {
    sidebarItems(state) {
      return state.sidebar.items;
    },
  },
};
