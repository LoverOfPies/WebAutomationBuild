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
        updateRadioSelection(contex, {collection, parent, parent_id, child, child_id, prev, current}) {
            const fields = {
                parent,
                parent_id,
                child,
                prev,
                current,
                mode: "many_to_many",
            }
            console.log(collection, child_id, fields);
            API.updateField(collection, child_id, fields)
        }
    }

}