<template>
  <div>
    <b-table outlined id="table" class="table-with-checkbox" :fields="fields" :items="stagesList">
      <template #cell(checked)="row">
        <b-form-checkbox
            v-model="selectedStages"
            :value="row.item.id"
        >
        </b-form-checkbox>
      </template>
      <template #cell(actions)="row">
          <b-button v-if="selectedStages.includes(row.item.id)">
              Технологии
          </b-button>
      </template>
    </b-table>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      fields: [
        { key: "checked", label: " " },
        { key: "name", label: "Наименование" },
        { key: "actions", label: " " },
      ],
      selectedStages: [],
    };
  },
  computed: {
    ...mapGetters(["stagesList"]),
  },
  methods: {
    ...mapActions(["loadStages"]),
  },
  mounted() {
    this.loadStages({ table_name: "work_stage" });
  },
};
</script>

