import axios from "axios";
import Vue from "vue";
import { ToastPlugin } from "bootstrap-vue";

Vue.use(ToastPlugin);

export default class {
  constructor() {
    this.api = `http://localhost:${process.env.VUE_APP_API_PORT}/api`;
    this.version = "v0.1";

    const vm = new Vue();

    this.showErrorToast = (error) => {
      console.log(error);
      vm.$bvToast.toast("Произошла ошибка при загрузке данных!", {
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
    }
  }

  getSidebarItems() {
    const promise = axios.get(`${this.api}/${this.version}/sidebar`);
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  getData(collection, params = {}) {
    if (Object.keys(params).length != 0) {
      console.info("[getData() params]", params);
    }

    const promise = axios.get(`${this.api}/${this.version}/get/${collection}`, {
      params,
    });
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  async getTableInfo(collection) {
    const res = await axios
      .get(`${this.api}/${this.version}/get_dict/${collection}`)
      .catch((r) => this.showErrorToast(r));
    // const data = promise.then((res) => res.data).catch((r) => this.showErrorToast(r));

    return res.data;
  }

  getTablesInfo() {
    const promise = axios.get(`${this.api}/${this.version}/get_dict`);
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  updateField(collection, id, fields) {
    const promise = axios.put(
      `${this.api}/${this.version}/update/${collection}/${id}`,
      fields
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  addRow(collection, fields) {
    console.log("[addRow() params]", collection, fields);
    const promise = axios.post(
      `${this.api}/${this.version}/add/${collection}`,
      fields
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  deleteRow(collection, id) {
    const promise = axios.delete(
      `${this.api}/${this.version}/delete/${collection}/${id}`
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  // estimate section

  getEstimateInfo() {
    const promise = axios.get(
      `${this.api}/${this.version}/get_estimate_records`
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  addEstimate(fields) {
    const promise = axios.post(
      `${this.api}/${this.version}/calculate_estimate`,
      fields
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  deleteEstimate(id) {
    const promise = axios.delete(`${this.api}/${this.version}/delete_estimate/${id}`)
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  getEstimateMaterials(id) {
    const promise = axios.get(
      `${this.api}/${this.version}/get_estimate_materials/${id}`
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

    return data;
  }

  getEstimateWorks(id) {
    const promise = axios.get(
      `${this.api}/${this.version}/get_estimate_works/${id}`
    );
    const data = promise
      .then((res) => res.data)
      .catch((r) => this.showErrorToast(r));

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
}
