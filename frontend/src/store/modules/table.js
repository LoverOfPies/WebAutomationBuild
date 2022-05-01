import APIClass from "@/api/ApiUtils.js";
const API = new APIClass();

export default {
	actions: {
		async getTableInfo({ commit, dispatch }, { name }) {
			commit("updateTableBusyState", true);
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
		async getItems({ commit }, { name, params = {} }) {
			console.log("[getItems()] params:", params);
			await API.getData(name, params).then((data) => {
				commit("updateTableItems", data);
				commit("updateTableBusyState", false);
			});
		},
		getFieldsModels({ commit, getters }) {
			commit("resetFieldsModels");
			getters.selectableFields.forEach((field) => {
				API.getData(field.key).then((data) => {
					commit("updateFieldsModels", {
						key: [field.key],
						data,
					});
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
				commit("addTableItem", data);
			});
		},
		deleteRow({ commit }, { table_name, row_id }) {
			API.deleteRow(table_name, row_id).then(() => {
				commit("deleteTableItem", row_id);
			});
		},
		async getParentNameById({ commit }, { table_name, id }) {
			await API.getData(table_name).then((data) => {
				const name = data.filter((x) => x.id == id)[0]["name"];
				commit("updateTableParentName", name);
			});
		},
		async copyWorkGroup({ commit }, { id }) {
			await API.copyWorkGroup(id).then((data) => {
				commit("addTableItem", data);
			});
		},
		async getHistoryTableData({ commit, dispatch }, { table_name }) {
			commit("updateTableBusyState", true);
			commit("updateTableFilterState", false);

			await API.getHistoryTableData(table_name).then((tableInfo) => {
				commit("updateTableTitle", tableInfo.title);
				commit("updateFieldsList", tableInfo.fields);

				dispatch("getFieldsModels");
			});
		},
		async getHistoryItemsData({ commit }, { table_name, row_id }) {
			await API.getHistoryItemsData(table_name, row_id).then((data) => {
				commit("updateTableItems", data);
				commit("updateTableBusyState", false);
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
		updateTableParentName(state, name) {
			state.table.parent_name = name;
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
			API.updateField(collection, id, {
				field,
				value,
			});
		},
		addTableItem(state, item) {
			console.log("[addTableItem()] pushing new item", item);
			if (item) {
				state.table.items.list.push(item);
			}
		},
		deleteTableItem(state, row_id) {
			let items_list = state.table.items.list;
			items_list.splice(items_list.indexOf(items_list.find((e) => e.id == row_id)), 1);
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
		updateHistoryTableData(state, data) {
			state.history_table.fields = data;
		},
	},
	state: {
		table: {
			title: "",
			parent_name: "",
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
		history_table: {
			fields: [],
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
		parent_name(state) {
			return state.table.parent_name;
		},
		mode(state) {
			return state.table.mode;
		},
		groupField(state) {
			return state.table.group_field;
		},
		itemsData(state, getters) {
			return {
				list: state.table.items.list,
				actions: getters.itemsActions,
			};
		},
		fieldsData(state, getters) {
			return {
				list: getters.fieldsList,
				models: state.table.fields.models,
			};
		},
		fieldsList(state) {
			let fields = state.table.fields.list;

			for (let field of fields) {
				if (field.type === "selectable") {
					field["filterByFormatted"] = true;
					field["formatter"] = (value, key, _item) => {
						return state.table.fields.models[key].find((x) => x.id === value)["name"];
					};
				}
				if (field.type === "date") {
					field["filterByFormatted"] = true;
					field["formatter"] = (value, _key, _item) => {
						return new Date(value).toLocaleDateString("ru-RU");
					};
				}
				if (field.type === "boolean") {
					field["filterByFormatted"] = true;
					field["formatter"] = (value, _key, _item) => {
						return value ? 'A' : 'Z';
					};
				}

				field["sortable"] = true;
			}

			fields.push({
				key: "actions",
				label: "Действия",
			});
			return fields;
		},
		itemsActions(state) {
			let actions = state.table.items.actions;
			actions.push({
				action: "delete",
			});
			return actions;
		},
		selectableFields(state) {
			return state.table.fields.list.filter((x) => x.type == "selectable");
		},
		itemRowsLength(state) {
			return state.table.items.list.length;
		},
		historyTableFieldsData(state) {
			return state.history_table.fields;
		},
	},
};
