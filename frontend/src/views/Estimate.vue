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
            @click="onToggleView(true, -1)"
          >
            Добавить
          </b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
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
    };
  },
  methods: {
    onToggleView(boolState, editId = -1) {
      this.isEditing = boolState;
      this.editingId = editId;
    },
  },
};
</script>
