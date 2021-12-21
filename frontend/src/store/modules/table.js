import APIClass from "@/api/ApiUtils.js";
const API = new APIClass();

export default {
  actions: {
    async getTableInfo({ commit, dispatch }, { name }) {
      commit("updateTableFilterState", false);
      await API.getTableInfo(name).then((tableInfo) => {
        commit("updateTableTitle", tableInfo.title);
        commit("updateFieldsList", tableInfo.fields);

        commit("resetTableMode");
        if (tableInfo.mode) {
          commit("updateTableMode", tableInfo.mode);
        }

        commit("resetGroupField");
        if (tableInfo.group_field) {
          commit("updateGroupField", tableInfo.group_field);
        }

        commit("resetFilters");
        if (tableInfo.filters.length > 0) {
          commit("updateFiltersModel", tableInfo.filters);
          dispatch("extendFilters", tableInfo.filters);
        }

        commit("resetItemsActions");
        if (tableInfo.actions.length > 0) {
          commit("updateItemsActions", tableInfo.actions);
        }

        dispatch("getFieldsModels");
        dispatch("getFiltersItems");
      });
    },
    getItems({ commit }, { name, params = {} }) {
      commit("updateTableBusyState", true);
      API.getData(name, params).then((data) => {
        commit("updateTableItems", data);
        commit("updateTableBusyState", false);
      });
    },
    getFieldsModels({ commit, getters }) {
      commit("resetFieldsModels");
      getters.selectableFields.forEach((field) => {
        API.getData(field.key).then((data) => {
          commit("updateFieldsModels", { key: [field.key], data });
        });
      });
    },
    addNewRow({ commit, dispatch, getters, state }, { table_name, row }) {
      API.addRow(table_name, row).then((data) => {
        if (state.table.isFiltered) {
          console.log("[getItems()] filtered update");
          dispatch("getItems", {
            name: table_name,
            params: getters.filterParams,
          });
        }
        console.log(data);
        commit("addTableItem", data);
      });
    },
    deleteRow({ commit }, { table_name, row_id }) {
      API.deleteRow(table_name, row_id).then(() => {
        commit("deleteTableItem", row_id);
      });
    },
  },
  mutations: {
    updateTableBusyState(state, isBusy) {
      state.table.isBusy = isBusy;
    },
    updateTableFilterState(state, isFiltered) {
      state.table.isFiltered = isFiltered;
    },
    updateTableTitle(state, title) {
      state.table.title = title;
    },
    updateTableMode(state, mode) {
      state.table.mode = mode;
    },
    resetTableMode(state) {
      state.table.mode = null;
    },
    updateGroupField(state, field) {
      state.table.group_field = field;
    },
    resetGroupField(state) {
      state.table.group_field = null;
    },
    updateTableItems(state, items) {
      state.table.items.list = items;
    },
    updateTableItem(state, { collection, id, field, value }) {
      let changedField = state.table.items.list.find((e) => e.id == id);
      changedField[field] = value;
      API.updateField(collection, id, { field, value });
    },
    addTableItem(state, item) {
      console.log("[addTableItem()] pushing new item", item);
      state.table.items.list.push(item);
    },
    deleteTableItem(state, row_id) {
      let items_list = state.table.items.list;
      items_list.splice(
        items_list.indexOf(items_list.find((e) => e.id == row_id)),
        1
      );
    },
    resetItemsActions(state) {
      state.table.items.actions = [];
    },
    updateItemsActions(state, data) {
      state.table.items.actions = data;
    },
    resetFieldsModels(state) {
      state.table.fields.models = {};
    },
    updateFieldsModels(state, { key, data }) {
      this.$app.$set(state.table.fields.models, key, data);
    },
    updateFieldsList(state, data) {
      state.table.fields.list = data;
    },
  },
  state: {
    table: {
      title: "",
      mode: null,
      group_field: null,
      isBusy: false,
      isReadOnly: false,
      isFiltered: false,
      fields: {
        list: [],
        models: [],
      },
      items: {
        list: [],
        actions: [],
      },
    },
  },
  getters: {
    isBusy(state) {
      return state.table.isBusy;
    },
    isFiltered(state) {
      return state.table.isFiltered;
    },
    isReadOnly(state) {
      return state.table.isReadOnly;
    },
    title(state) {
      return state.table.title;
    },
    mode(state) {
      return state.table.mode;
    },
    groupField(state) {
      return state.table.group_field;
    },
    itemsData(state, getters) {
      return { list: state.table.items.list, actions: getters.itemsActions };
    },
    fieldsData(state, getters) {
      return { list: getters.fieldsList, models: state.table.fields.models };
    },
    fieldsList(state) {
      let fields = state.table.fields.list;
      fields.push({ key: "actions", label: "Действия" });
      return fields;
    },
    itemsActions(state) {
      let actions = state.table.items.actions;
      actions.push({ action: "delete" });
      return actions;
    },
    selectableFields(state) {
      return state.table.fields.list.filter((x) => x.type == "selectable");
    },
    itemRowsLength(state) {
      return state.table.items.list.length;
    },
  },
};
