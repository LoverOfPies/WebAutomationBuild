<template>
  <div>
    <Title :title="title" back="false" exim="false" />

    <b-container fluid class="p-4">
      <b-row>
        <b-col cols="12" xl="6" class="p-2">
          <b-form @submit.prevent="importTable" class="d-flex flex-wrap">
            <div class="mb-2 fs-5 w-100">Системный импорт</div>
            <b-form-select
              id="settings-import"
              v-model="importForm.selected"
              :options="importForm.options"
              class="me-2"
            ></b-form-select>
            <b-form-file
              v-model="importForm.file"
              :state="Boolean(importForm.file)"
              placeholder="Выберите файл или перетащите сюда..."
              drop-placeholder="Перетащите файл сюда..."
              class="me-2 flex-grow-1"
            ></b-form-file>
            <b-button type="submit" :disabled="importForm.disabled" variant="primary">Импорт</b-button>
          </b-form>
        </b-col>
        <b-col cols="12" xl="5" offset-xl="1" class="p-2">
          <b-form @submit.prevent="exportTable">
            <div class="mb-2 fs-5">Системный экспорт</div>
            <b-form-select
              id="settings-export"
              v-model="exportForm.selected"
              :options="exportForm.options"
              class="me-2"
            ></b-form-select>
            <b-button
              type="submit"
              :disabled="exportForm.disabled"
              variant="primary"
              >Экспорт</b-button
            >
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import API from "../api/ApiUtils.js";
import Title from "@/components/Title.vue";

export default {
  components: { Title },
  data() {
    return {
      API: new API(this),
      title: "Настройки",
      importForm: {
        selected: null,
        options: [{ value: null, text: "Выберите из списка" }],
        disabled: true,
        file: null,
      },
      exportForm: {
        selected: null,
        options: [{ value: null, text: "Выберите из списка" }],
        disabled: true,
      },
    };
  },
  methods: {
    getTablesInfo() {
      this.API.getTablesInfo().then((data) => {
        data.forEach((table) => {
          this.importForm.options.push({
            value: table.name,
            text: table.title,
          });
          this.exportForm.options.push({
            value: table.name,
            text: table.title,
          });
        });
      });
    },
    importTable() {
      console.log(this.importForm);
      this.API.importTable(this.importForm.selected, this.importForm.file);
    },
    exportTable() {
      console.log(this.exportForm);
    },
  },
  watch: {
    "importForm.selected": function () {
      this.importForm.disabled = (this.importForm.selected && !this.importForm.file) ? true : false
    },
    "importForm.file": function () {
      this.importForm.disabled = (this.importForm.selected && !this.importForm.file) ? true : false
    },
    "exportForm.selected": function (selected) {
      this.exportForm.disabled = !selected;
    },
  },
  mounted() {
    this.getTablesInfo();
  },
};
</script>
