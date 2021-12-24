import APIClass from "../../api/ApiUtils.js";
const API = new APIClass();

export default {
  actions: {
    async loadEstimateInfo({ state }) {
      await API.getEstimateInfo().then(
        (estimates) => (state.estimates = estimates)
      );
    },
    async loadProjects({ state }, { table_name }) {
      await API.getData(table_name).then((projects) => {
        state.projects = projects;
      });
    },
    async loadWorks({ state }, { table_name }) {
      await API.getData(table_name).then((works) => (state.works = works));
    },
    async loadStages({ state }, { table_name }) {
      await API.getData(table_name).then((stages) => (state.stages = stages));
    },
    async addEstimate(ctx, { fields }) {
      await API.addEstimate(fields).then(console.log("Success"));
    },
    async loadTechList({ state }, { table_name }) {
      await API.getData(table_name).then(
        (tech_list) => (state.tech_list = tech_list)
      );
    },
    async loadEstimateMaterials({ state }, { id }) {
      await API.getEstimateMaterials(id).then(mat_list => state.estimate_modal_list = mat_list);
    },
    async loadEstimateWorks({ state }, { id }) {
      await API.getEstimateWorks(id).then(work_list => state.estimate_modal_list = work_list);
    }
  },
  mutations: {
    updateProjectList(state, list) {
      state.projects = list;
    },
    resetProjectList(state) {
      state.projects = [];
    },
    resetEstimateModalList(state) {
      state.estimate_modal_list = [];
    }
  },
  state: {
    estimates: [],
    projects: [],
    works: [],
    stages: [],
    tech_list: [],
    estimate_modal_list: [],
  },
  getters: {
    estimatesList(state) {
      return state.estimates;
    },
    projectsList(state) {
      return state.projects;
    },
    worksList(state) {
      return state.works;
    },
    baseWorksList(state) {
      return state.works.filter((x) => x.work_base == true);
    },
    notBaseWorksList(state) {
      return state.works.filter((x) => x.work_base == false);
    },
    stagesList(state) {
      return state.stages;
    },
    techList(state) {
      return state.tech_list;
    },
    estimateModalList(state) {
      return state.estimate_modal_list;
    },
  },
};
