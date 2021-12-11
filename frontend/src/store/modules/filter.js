import Vue from "vue";
import APIClass from "../../api/ApiUtils.js";
const API = new APIClass(Vue);

export default {
  actions: {
    getFiltersItems({ commit, state }) {
      commit("resetFilterList");
      state.filters.model.forEach((filter) => {
        API.getData(filter.key).then((data) => {
          commit("updateFilterList", {
            key: [filter.key],
            data,
          });
        });
      });
    },
    extendFilters({ commit, state }, data) {
      data.forEach((filter, i) => {
        commit("updateObj", {
          obj: state.filters.model[i],
          key: "disabled",
          data: i == 0 ? false : true,
        });
        commit("updateObj", {
          obj: state.filters.model[i],
          key: "text",
          data: "Не выбрано",
        });
        commit("updateObj", {
          obj: state.filters.state,
          key: [filter.key],
          data: "",
        });
      });
    },
    resetFiltersFromId({ commit, state }, id = 0) {
      for (let i = id; i < state.filters.model.length; i++) {
        commit("resetFilterLabel", { model: state.filters.model[i].key });

        commit("updateObj", {
          obj: state.filters.model[i],
          key: "disabled",
          data: i == id ? false : true,
        });
        commit("updateObj", {
          obj: state.filters.state,
          key: state.filters.model[i].key,
          data: "",
        });
      }
      if (id == 0) commit("updateTableFilterState", false);
    },
    applyFilters({ commit, state }, fields) {
      let current = state.filters.model.findIndex((x) => x.key == fields.field);
      if (current != state.filters.model.length - 1) {
        commit("updateObj", {
          obj: state.filters.model[current + 1],
          key: "disabled",
          data: false,
        });
      }

      commit("updateTableFilterState", true);
      commit("updateObj", {
        obj: state.filters.state,
        key: fields.field,
        data: fields.value,
      });
    },
  },
  mutations: {
    resetFilterList(state) {
      state.filters.list = {};
    },
    // resetFiltersModel(state) {
    //     state.filters.model = [];
    // },
    // resetFilterState(state) {
    //     state.filters.state = {};
    // },
    resetFilters(state) {
      state.filters.list = {};
      state.filters.model = [];
      state.filters.state = {};
    },
    resetFilterLabel(state, { model }) {
      state.filters.model.find((x) => x.key == model).text = "Не выбрано";
    },
    updateFiltersModel(state, data) {
      state.filters.model = data;
    },
    updateFilterList(state, { key, data }) {
      this.$app.$set(state.filters.list, key, data);
    },
    updateFilterLabel(state, { itemId, model }) {
      state.filters.model.find((x) => x.key == model).text = state.filters.list[
        model
      ].find((x) => x.id == itemId)["name"];
    },
  },
  state: {
    filters: {
      model: [],
      list: {},
      state: {},
    },
  },
  getters: {
    filtersData(state) {
      return state.filters;
    },
    filterParams(state) {
      return { ...state.filters.state, ...{ mode: "advanced_filters" } };
    },
  },
};
