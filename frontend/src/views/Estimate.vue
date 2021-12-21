<template>
  <div>
    <Title :title="title" back="false" />

    <b-container fluid class="p-4">
      <b-row>
        <b-col cols="12" xl="8">
          <!-- all estimates -->
          <EstimatesTable v-if="!isEditing" @toggleEditingView="onToggleView" />
          <!-- adding/editing mode -->
          <EstimateForm
            v-if="isEditing"
            :id="editingId"
            @toggleEditingView="onToggleView"
          />

          <b-button
            v-if="!isEditing"
            variant="primary"
            @click="isEditing = true"
          >
            Добавить
          </b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// import { mapGetters, mapActions } from "vuex";

import Title from "@/components/Title.vue";
import EstimatesTable from "../components/estimate/EstimatesTable.vue";
import EstimateForm from "../components/estimate/EstimateForm.vue";

export default {
  components: { Title, EstimateForm, EstimatesTable },
  data() {
    return {
      title: "Расчеты",
      isEditing: false,
      editingId: null,
      // name: null,
      // selectedProjectId: null,
      // baseEquipment: true,
    };
  },
  computed: {
    // ...mapGetters(["projectsList"]),
  },
  methods: {
    //   ...mapActions(["loadProjects"]),
    onToggleView(boolState) {
      this.isEditing = boolState;
    },
    //   async init() {
    //     this.loadProjects({ table_name: "project" });
    //   },
    //   getFieldById(id, model, field) {
    //     return this.projectsList.find((x) => x.id == id)[field];
    //   },
    //   onProjectLabelChange({ id: itemId, model }) {
    //     this.$refs["project-input"].labelReplacement = this.getFieldById(
    //       itemId,
    //       model,
    //       "name"
    //     );
    //   },
    //   onProjectInputUpdate({ _id, fields }) {
    //     this.selectedProjectId = fields.value;
    //   },
    //   saveEstimate() {
    //     console.log("TODO: estimate() not implemented");
    //   },
    // },
    // mounted() {
    //   this.init();
  },
};
</script>
