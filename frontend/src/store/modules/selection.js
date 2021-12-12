import Vue from "vue";
import APIClass from "../../api/ApiUtils.js";
const API = new APIClass(Vue);

export default {

    actions: {
        // work_group: 1, work_technology: 1

        updateSelection(context, { collection, parent, parent_id, child, child_id, value }) {
            const fields = {
                parent,
                parent_id,
                child,
                value,
                mode: "many_to_many"
            };
            API.updateField(collection, child_id, fields);
        }
    }

}