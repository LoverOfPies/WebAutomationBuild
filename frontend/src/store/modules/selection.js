import APIClass from "@/api/ApiUtils.js";
const API = new APIClass();

export default {

    actions: {
        updateSelection(context, { collection, parent, parent_id, child, child_id, value }) {
            const fields = {
                parent,
                parent_id,
                child,
                value,
                mode: "many_to_many"
            };
            API.updateField(collection, child_id, fields);
        },
        // TODO: multiple update
        updateRadioSelection() {}
    }

}