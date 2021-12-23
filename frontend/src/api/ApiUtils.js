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

  async importTable(collection, file) {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios
      .post(`${this.api}/${this.version}/import/${collection}`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      })
      .then(() => this.showSuccessToast())
      .catch((r) => this.showErrorToast(r));

    return res.data;
  }

  exportTable(collection) {
    axios({
      url: `${this.api}/${this.version}/export/${collection}`,
      method: "GET",
      responseType: "blob", // important
    }).then((response) => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute(collection, "file.xlsx");
      link.click();
      window.URL.revokeObjectURL(url);
    });
  }
}
