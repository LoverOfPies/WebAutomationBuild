<template>
  <div>
    <b-button variant="primary" v-if="readOnly"> Импорт </b-button>
    <add-new-row
      v-else
      @addNewRow="onAddNewRow"
      :fields="fields"
      :fieldsModels="fieldsModels"
      title="Добавление записи"
    />
  </div>
</template>

<script>
import AddNewRow from "./AddNewRow.vue";

export default {
  components: { AddNewRow },
  props: ["readOnly", "fields", "fieldsModels"],
  methods: {
    onAddNewRow(fields) {
      this.$emit("addNewRow", fields);
    },
  },
};
</script>

<style></style>
