import app from "../main.js";
import axios from "axios";

export default class {
  constructor() {
    this.api = `http://localhost:${process.env.VUE_APP_API_PORT}/api`;
    this.version = "v0.1";
    this.vm = app;
    this.showErrorToast = (error) => {
      console.log(error);
      this.vm.$bvToast.toast("Произошла ошибка при загрузке данных!", {
        title: "Ошибка",
        autoHideDelay: 5000,
        variant: "danger",
      });
    };
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
      console.info("API Request Params", params);
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
    console.log(collection, fields);
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

  async importTable(collection, file) {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios
      .post(`${this.api}/${this.version}/import/${collection}`, formData, { headers: { 'Content-Type': 'multipart/form-data' } })
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
