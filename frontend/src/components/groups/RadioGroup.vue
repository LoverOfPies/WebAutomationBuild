<template>
  <div>
    <b-form-group
      v-for="(group, index) in radioGroups"
      :key="index"
      label="radio group placeholder"
    >
      <RadioGroupElement :id="id" :name="name" :group="group" :index="index" :selection="groupSelections[index]" :parent="parent_table" :child="child_table" />
    </b-form-group>
  </div>
</template>

<script>
import RadioGroupElement from "./RadioGroupElement.vue";

export default {
  props: ["items", "groupField", "fields", "id", "name"],
  components: { RadioGroupElement },
  data() {
    return {
      parent_id: this.id,
      parent_table: this.fields.list[0].key,
      child_table: this.fields.list[1].key,
    };
  },
  computed: {
    radioGroups() {
      let groups = [];

      this.items.list.forEach((e) => {
        if (!groups[e.work_stage]) {
          groups[e.work_stage] = [
            {
              id: -1,
              name: "Не выбрано",
              work_stage: e.work_stage,
            },
          ];
        }
        groups[e.work_stage].push(e);
      });

      return groups.filter(Boolean);
    },
    groupSelections() {
      const selections = [];

      for (let i = 0; i < this.radioGroups.length; i++) {
        const current_selection = this.radioGroups[i].filter(
          (item) => item.checked == true
        );
        const selection_id =
          current_selection.length == 0 ? -1 : current_selection[0].id;
        selections[i] = selection_id;
      }

      return selections;
    },
  },
};
</script>
