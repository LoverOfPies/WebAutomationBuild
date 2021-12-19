import APIClass from "../../api/ApiUtils.js";
const API = new APIClass();

export default {
    actions: {
        async loadProjects({ state }, { table_name }) {
            await API.getData(table_name).then(projects => {
                state.projects = projects
            });
        },
        async loadWorks({ state }, { table_name }) {
            await API.getData(table_name).then(works => state.works = works);
        },
        async loadStages({state}, { table_name }) {
            await API.getData(table_name).then(stages => state.stages = stages);
        }
    },
    mutations: {
        updateProjectList(state, list) {
            state.projects = list;
        },
        resetProjectList(state) {
            state.projects = [];
        }
    },
    state: {
        projects: [],
        works: [],
        stages: [],
    },
    getters: {
        projectsList(state) {
            return state.projects;
        },
        worksList(state) {
            return state.works;
        },
        baseWorksList(state) {
            return state.works.filter(x => x.work_base == true);
        },
        notBaseWorksList(state) {
            return state.works.filter(x => x.work_base == false);
        },
        stagesList(state) {
            return state.stages;
        },
    }
}