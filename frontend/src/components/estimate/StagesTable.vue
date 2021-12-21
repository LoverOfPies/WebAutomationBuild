<template>
  <div>
    <b-card class="mb-2" no-body header="Стадии работ">
      <b-list-group flush>
        <b-list-group-item v-for="stage in stagesList" :key="stage.id">
          <b-row>
            <b-col>
              <b-form-checkbox v-model="selectedStages" :value="stage.id">{{
                stage.name
              }}</b-form-checkbox>
            </b-col>
            <b-col class="text-end">
              <!-- TODO: модалка со всеми технологиями для этой стадии -->
              <change-field-modal
                v-if="selectedStages.includes(stage.id)"
                label="Выберите технологию"
                :model="techModel"
                :rowId="stage.id"
                :items="techList"
                :ref="`tech-field-${stage.id}`"
                size="sm"
                class="negative-margin"
                @updateField="onUpdateField"
              />
            </b-col>
          </b-row>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/
import { mapActions, mapGetters } from "vuex";

import ChangeFieldModal from "../tables/ChangeFieldModal.vue";

export default {
  components: { ChangeFieldModal },
  data() {
    return {
      fields: [
        { key: "checked", label: " " },
        { key: "name", label: "Наименование" },
        { key: "actions", label: " " },
      ],
      stageModel: "work_stage",
      selectedStages: [],
      techModel: "work_technology",
      selectedWorkTech: [],
    };
  },
  computed: {
    ...mapGetters(["stagesList", "techList"]),
  },
  methods: {
    ...mapActions(["loadStages", "loadTechList"]),
    onUpdateField({ id, fields }) {
      this.$set(this.selectedWorkTech, id, fields.value);
      this.$refs[`tech-field-${id}`][0].labelReplacement = this.getFieldById(
        fields.value,
        this.techModel,
        "name"
      );
    },
    getFieldById(id, _model, field) {
      return this.techList.find((x) => x.id == id)[field];
    },
  },
  watch: {
    selectedWorkTech(newList) {
      this.$emit("updateWorkTechnologies", newList.filter(Boolean));
    },
    selectedStages(newList, oldList) {
      const diff = oldList.filter((x) => !newList.includes(x));
      if (diff[0]) {
        this.selectedWorkTech.splice(diff, 1);
      }
    },
  },
  mounted() {
    this.loadStages({ table_name: this.stageModel });
    this.loadTechList({ table_name: this.techModel });
  },
};
</script>

<style lang="scss" scoped>
.negative-margin {
  margin: -4px 0;
}
</style>
