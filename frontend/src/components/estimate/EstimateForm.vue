<template>
  <div>
    <b-row class="my-2">
      <b-col sm="3" class="position-relative d-flex align-items-center">
        <label for="name-input" class="mb-0">ФИО:</label>
      </b-col>
      <b-col sm="9">
        <b-form-input
          v-model="name"
          id="name-input"
          placeholder="Введите ФИО"
        />
      </b-col>
    </b-row>

    <b-row class="my-2">
      <b-col sm="3" class="position-relative d-flex align-items-center">
        <label for="name-input" class="mb-0">Проект:</label>
      </b-col>
      <b-col sm="9">
        <change-field-modal
          ref="project-input"
          model="project-input"
          rowId="-1"
          :label="'Не выбрано'"
          :items="projectsList"
          :no-truncate="true"
          @updateField="onProjectInputUpdate"
          @labelChange="onProjectLabelChange"
        />
      </b-col>
    </b-row>

    <b-row class="my-2">
      <b-col sm="3">
        <label for="name-input">Базовая комплектация:</label>
      </b-col>
      <b-col sm="9">
        <b-form-checkbox v-model="isBaseEquipment" size="lg" />
      </b-col>
    </b-row>

    <!-- base table -->
    <BaseTable
      class="mb-4"
      :showBase="isBaseEquipment"
      :projectId="selectedProjectId"
      @updateAdditionalWorks="onUpdateAdditionalWorks"
    />
    <!-- stages table -->
    <StagesTable
      class="mb-4"
      v-if="!isBaseEquipment"
      @updateWorkTechnologies="onUpdateWorkTechnologies"
    />

    <b-row class="my-2">
      <b-col cols="2">
        <b-button variant="primary" @click="saveEstimate"> Сохранить </b-button>
      </b-col>
      <b-col class="text-end">
        <b-button variant="danger" @click="$emit('toggleEditingView', false)">
          Отмена
        </b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/

import { mapGetters, mapActions } from "vuex";

import ChangeFieldModal from "../tables/ChangeFieldModal.vue";
import BaseTable from "./BaseTable.vue";
import StagesTable from "./StagesTable.vue";

export default {
  components: { ChangeFieldModal, BaseTable, StagesTable },
  props: ["id"],
  data() {
    return {
      name: null,
      selectedProjectId: null,
      selectedAdditionalWorks: [],
      selectedWorkTechnologies: [],
      isBaseEquipment: true,
      isEditing: false,
    };
  },
  computed: {
    ...mapGetters(["projectsList"]),
  },
  methods: {
    ...mapActions(["loadProjects", "addEstimate"]),
    async init() {
      this.loadProjects({ table_name: "project" });
      if (this.id != null && this.id != -1) {
        console.log("editing estiamte with id " + this.id);
      }
    },
    getFieldById(id, model, field) {
      return this.projectsList.find((x) => x.id == id)[field];
    },
    onProjectLabelChange({ id: itemId, model }) {
      this.$refs["project-input"].labelReplacement = this.getFieldById(
        itemId,
        model,
        "name"
      );
    },
    onProjectInputUpdate({ _id, fields }) {
      this.selectedProjectId = fields.value;
    },
    onUpdateAdditionalWorks(newList) {
      this.selectedAdditionalWorks = newList;
    },
    onUpdateWorkTechnologies(newList) {
      this.selectedWorkTechnologies = newList;
    },
    async saveEstimate() {
      /* 
      {
        client_fio,
        use_base,
        project_id,
        additional_works: [1, 2, ...] (optional),
        work_technologies: [1, 2, ...] (optional)
      } 
      */
      const fields = {
        client_info: this.name,
        use_base: this.isBaseEquipment,
        project_id: this.selectedProjectId,
        ...(this.selectedAdditionalWorks.length && {
          additional_works: this.selectedAdditionalWorks,
        }),
        ...(this.selectedWorkTechnologies.length && {
          work_technologies: this.selectedWorkTechnologies,
        }),
      };
      console.table(fields);
      await this.addEstimate({ fields }).then((data) => {
        console.log(data);
        this.$emit("toggleEditingView", false);
      });
    },
  },
  mounted() {
    this.init();
  },
};
</script>
