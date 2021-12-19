<template>
  <div>
    <Title :title="title" back="false" />

    <b-container fluid class="p-4">
      <b-row class="my-2">
        <b-col sm="3">
          <label for="name-input">ФИО:</label>
        </b-col>
        <b-col sm="9">
          <b-form-input
            v-model="name"
            id="name-input"
            placeholder="Введите ваше ФИО"
          ></b-form-input>
        </b-col>
      </b-row>

      <b-row class="my-2">
        <b-col sm="3">
          <label for="name-input">Проект:</label>
        </b-col>
        <b-col sm="9">
          <change-field-modal
            ref="project-input"
            :label="'Не выбрано'"
            model="project-input"
            rowId="-1"
            :items="projectsList"
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
          <b-form-checkbox
            v-model="baseEquipment"
            size="lg"
          />
        </b-col>
      </b-row>

      <!-- base table -->
      <BaseTable class="mb-4" v-if="baseEquipment" />
      <!-- stages table -->
      <StagesTable class="mb-4" v-else />

      <b-row class="my-2">
        <b-col cols="2">
          <b-button variant="primary" @click="estimate"> Рассчитать </b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/

import { mapGetters, mapActions } from "vuex";

import Title from "@/components/Title.vue";
import ChangeFieldModal from "../components/tables/ChangeFieldModal.vue";
import BaseTable from "../components/estimate/BaseTable.vue";
import StagesTable from "../components/estimate/StagesTable.vue";


export default {
  components: { Title, ChangeFieldModal, BaseTable, StagesTable },
  data() {
    return {
      title: "Расчет",
      name: null,
      selectedProjectId: null,
      baseEquipment: true,
    };
  },
  computed: {
    ...mapGetters(["projectsList"]),
  },
  methods: {
    ...mapActions(["loadProjects"]),
    async init() {
      this.loadProjects({ table_name: "project" });
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
    estimate() {
      console.log("TODO: estimate() not implemented");
    },
  },
  mounted() {
    this.init();
  },
};
</script>

<style lang="sass" scoped></style>
