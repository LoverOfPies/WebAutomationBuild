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
      <b-row v-for="field in localFields" :key="field.id" class="py-2">
        <b-col
          class="position-relative d-flex align-items-center"
          v-if="field.key != 'actions'"
        >
          <label class="mb-0">{{ field.label }}:</label>
        </b-col>
        <b-col cols="8" v-if="field.key != 'actions'">
          <change-field-modal
            v-if="field.type && field.type == 'selectable'"
            rowId="-1"
            :ref="`change-field-${field.key}`"
            :label="'Не выбрано'"
            :model="field.key"
            :items="fieldsModels[field.key]"
            :no-truncate="true"
            @updateField="onUpdateField"
            @labelChange="onLabelChange"
          />
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
          <date-field
            v-else-if="field.type && field.type == 'date'"
            :model="field.key"
            @updateField="onUpdateField"
          >
          </date-field>
          <b-form-input
            v-else
            v-model="addModal.fields[field.key]"
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
import DateField from "./fields/DateField.vue";

export default {
  components: {
    ChangeFieldModal,
    FloatField,
    IntField,
    BooleanField,
    DateField,
  },
  props: ["title", "fields", "fieldsModels", "parent", "parentId"],
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
  computed: {
    localFields() {
      if (this.parent) {
        return this.fields.filter((x) => x.key != this.parent);
      }
      return this.fields;
    },
  },
  methods: {
    showAddModal(button) {
      this.$bvModal.show(this.addModal.id, button);
      // keys listener
      window.addEventListener("keypress", this.keyAction);
    },
    resetAddModal() {
      for (let field in this.addModal.fields) {
        this.addModal.fields[field] = "";
        delete this.addModal.fields[field];
      }
      window.removeEventListener("keypress", this.keyAction);
    },
    onLabelChange({ id: itemId, model }) {
      this.$refs[`change-field-${model}`][0].labelReplacement =
        this.getFieldById(itemId, model, "name");
    },
    onUpdateField({ _id, fields }) {
      this.$set(this.addModal.fields, fields.field, fields.value);
    },
    addNewRow(ok) {
      console.log(ok);
      const fields = {};

      Object.keys(this.addModal.fields).forEach((key) => {
        fields[key] = this.addModal.fields[key];
      });

      if (this.parent) {
        fields[this.parent] = this.parentId;
      }

      this.$emit("addNewRow", fields);
      ok();
    },
    getFieldById(id, model, field) {
      return this.fieldsModels[model].find((x) => x.id == id)[field];
    },
    keyAction(e) {
      if (e.key === "Enter" && e.target.classList.contains("modal-content")) {
        this.addNewRow(() => {
          this.$bvModal.hide(this.addModal.id);
        });
      }
    },
  },
  destroyed() {
    window.removeEventListener("keypress", this.keyAction);
  },
};
</script>
