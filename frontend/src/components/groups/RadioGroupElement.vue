<template>
  <b-form-radio-group
    v-model="localSelection"
    @change="changeSelection($event, group[index].work_stage)"
    stacked
  >
    <b-form-radio v-for="item in group" :key="item.id" :value="item.id">
      {{ item.name }}
    </b-form-radio>
  </b-form-radio-group>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: ["id", "name", "group", "index", "selection", "parent", "child"],
  data() {
    return {
      localSelection: this.selection,
      prev: null,
      current: null,
    };
  },
  methods: {
    ...mapActions(["updateRadioSelection"]),
    changeSelection(checked, work_stage_id) {
      console.log("[changeSelection() radio update]", checked, work_stage_id);

      this.updateRadioSelection({
        collection: this.name,
        parent: this.parent,
        parent_id: this.id,
        child: this.child,
        child_id: this.id,
        prev: this.prev,
        current: this.current,
      });
    },
  },
  watch: {
    localSelection(after, before) {
      this.prev = before;
      this.current = after;
    },
  },
};
</script>
