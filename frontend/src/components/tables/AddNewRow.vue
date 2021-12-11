<template>
  <div>
    <b-button variant="primary" @click="showAddModal($event.target)">
      Добавить
    </b-button>

    <b-modal
      :id="addModal.id"
      :title="addModal.title"
      @hide="resetAddModal"
      centered
    >
      <b-row v-for="field in fields" :key="field.id" class="py-2">
        <b-col class="position-relative" v-if="field.key != 'actions'">
          <label
            class="position-absolute top-50 start-50 translate-middle"
            for="input-default"
            >{{ field.label }}:</label
          >
        </b-col>
        <b-col cols="8" v-if="field.key != 'actions'">
          <change-field-modal
            :ref="`change-field-${field.key}`"
            v-if="field.type && field.type == 'selectable'"
            :label="'Не выбранно'"
            :model="field.key"
            rowId="-1"
            :items="fieldsModels[field.key]"
            @updateField="onUpdateField"
            @labelChange="onLabelChange"
          ></change-field-modal>
          <float-field
            v-else-if="field.type && field.type == 'float'"
            :model="field.key"
            @updateField="onUpdateField"
          />
          <int-field
            v-else-if="field.type && field.type == 'integer'"
            :model="field.key"
            @updateField="onUpdateField"
          />
          <boolean-field
            v-else-if="field.type && field.type == 'boolean'"
            :model="field.key"
            @updateField="onUpdateField"
          />
          <b-form-input
            v-else
            v-model="addModal.fields[field.key]"
            id="input-default"
            placeholder="Введите текст"
          ></b-form-input>
        </b-col>
      </b-row>

      <template #modal-footer="{ ok, cancel }">
        <b-button variant="danger" @click="cancel()"> Отмена </b-button>
        <b-button variant="success" @click="addNewRow(ok)"> OK </b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/
import API from "../../api/ApiUtils.js";

import ChangeFieldModal from "./ChangeFieldModal.vue";
import FloatField from "./fields/FloatField.vue";
import IntField from "./fields/IntField.vue";
import BooleanField from "./fields/BooleanField.vue";

export default {
  components: { ChangeFieldModal, FloatField, IntField, BooleanField },
  props: ["title", "fields", "fieldsModels"],
  data() {
    return {
      API: new API(this),
      addModal: {
        id: "add-row-modal",
        title: this.title,
        fields: {},
      },
    };
  },
  methods: {
    showAddModal(button) {
      this.$bvModal.show(this.addModal.id, button);
    },
    resetAddModal() {
      for (let field in this.addModal.fields) {
        this.addModal.fields[field] = "";
        delete this.addModal.fields[field];
      }
    },
    onLabelChange({ id: itemId, model }) {
      this.$refs[`change-field-${model}`][0].labelReplacement =
        this.getFieldById(itemId, model, "name");
    },
    onUpdateField({ _id, fields }) {
      this.$set(this.addModal.fields, fields.field, fields.value);
    },
    addNewRow(ok) {
      let fields = {};

      Object.keys(this.addModal.fields).forEach((key) => {
        fields[key] = this.addModal.fields[key];
      });

      this.$emit("addNewRow", fields);
      ok();
    },
    getFieldById(id, model, field) {
      return this.fieldsModels[model].find((x) => x.id == id)[field];
    },
  },
};
</script>
