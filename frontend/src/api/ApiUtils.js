import axios from "axios";
import Vue from "vue";
import { ToastPlugin } from "bootstrap-vue";

axios.interceptors.response.use(undefined, function (error) {
	error.originalMessage = error.message;
	Object.defineProperty(error, "message", {
		get: function () {
			if (!error.response) {
				return error.originalMessage;
			}
			return error.response.data.error;
		},
	});
	return Promise.reject(error);
});

Vue.use(ToastPlugin);

export default class {
	constructor() {
		if (process.env.VUE_APP_API_PORT != null) {
			this.api = `http://${window.location.hostname}:${process.env.VUE_APP_API_PORT}/api`;
		} else {
			this.api = `http://${window.location.host}/api`;
		}
		this.version = "v0.1";

		const vm = new Vue();

		this.showErrorToast = (error) => {
			vm.$bvToast.toast(error.toJSON().message, {
				title: "Ошибка",
				autoHideDelay: 5000,
				variant: "danger",
			});
		};

		this.showSuccessToast = () => {
			vm.$bvToast.toast("Запрос выполнен успешно!", {
				title: "Успех",
				autoHideDelay: 3000,
				variant: "success",
			});
		};
	}

	getSidebarItems() {
		const promise = axios.get(`${this.api}/${this.version}/sidebar`);
		const data = promise
			.then((res) => res.data)
			.catch((r) => {
				this.showErrorToast(r);
			});

		return data;
	}

	getData(collection, params = {}) {
		const promise = axios.get(`${this.api}/${this.version}/get/${collection}`, {
			params,
		});
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	async getTableInfo(collection) {
		const res = await axios
			.get(`${this.api}/${this.version}/get_dict/${collection}`)
			.catch((r) => this.showErrorToast(r));

		return res.data;
	}

	getTablesInfo() {
		const promise = axios.get(`${this.api}/${this.version}/get_dict`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	updateField(collection, id, fields) {
		const promise = axios.put(`${this.api}/${this.version}/update/${collection}/${id}`, fields);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	addRow(collection, fields) {
		console.log("[addRow() params]", collection, fields);
		const promise = axios.post(`${this.api}/${this.version}/add/${collection}`, fields);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	deleteRow(collection, id) {
		const promise = axios.delete(`${this.api}/${this.version}/delete/${collection}/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	// estimate section

	getEstimateInfo() {
		const promise = axios.get(`${this.api}/${this.version}/get_estimate_records`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	addEstimate(fields) {
		const promise = axios.post(`${this.api}/${this.version}/calculate_estimate`, fields);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	deleteEstimate(id) {
		const promise = axios.delete(`${this.api}/${this.version}/delete_estimate/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	getEstimateMaterials(id) {
		const promise = axios.get(`${this.api}/${this.version}/get_estimate_materials/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	getEstimateWorks(id) {
		const promise = axios.get(`${this.api}/${this.version}/get_estimate_works/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	getProjectTechnoloies(id) {
		const promise = axios.get(`${this.api}/${this.version}/get_project_technologies/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	// import/export

	async importTable(collection) {
		await axios
			.post(`${this.api}/${this.version}/import/${collection}`)
			.then(() => this.showSuccessToast())
			.catch((r) => this.showErrorToast(r));
	}

	async exportTable(collection) {
		await axios
			.get(`${this.api}/${this.version}/export/${collection}`)
			.then(() => this.showSuccessToast())
			.catch((r) => this.showErrorToast(r));
	}

	// copy

	copyWorkGroup(id) {
		const promise = axios.get(`${this.api}/${this.version}/copy_work_group/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	// history control

	getHistoryTableData(collection) {
		const promise = axios.get(`${this.api}/${this.version}/get_history_dict/${collection}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}

	getHistoryItemsData(collection, id) {
		const promise = axios.get(`${this.api}/${this.version}/get_history/${collection}/${id}`);
		const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

		return data;
	}
}
