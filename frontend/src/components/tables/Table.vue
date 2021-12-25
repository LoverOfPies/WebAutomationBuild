<template>
  <b-row>
    <b-col>
      <b-table
        id="table"
        class="text-nowrap"
        :items="itemsData.list"
        :fields="localFields"
        :per-page="perPage"
        :current-page="currentPage"
        :busy="isBusy"
        :filter="filter"
        :sort-desc.sync="SDesc"
        head-variant="light"
        bordered
        responsive
        show-empty
      >
        <template #cell(name)="data">
          <name-cell @updateField="onUpdateField" :data="data" />
        </template>

        <!-- TODO: display [ ] float, [ ] int, [x] bool, [ ] date fields -->
        <!-- FIXME: make them editable -->
        <template
          v-for="field in cellTypes"
          v-slot:[`cell(${field.key})`]="data"
        >
          <span :key="field.key">
            <BooleanField
              v-if="data.field.type == 'boolean'"
              :readOnly="true"
              :state="data.item[field.key]"
            />
            <!-- <span v-else-if="data.field.type == 'date'"><DateField  :readOnly="true" :value="data.item[field.key]" />{{data.item[field.key]}}</span> -->
            <change-field-modal
              v-else-if="data.field.type == 'selectable'"
              @updateField="onUpdateField"
              :label="getFieldById(data.item[field.key], field.key, 'name')"
              :model="field.key"
              :rowId="data.item.id"
              :items="fieldsData.models[field.key]"
            />
            <span v-else>
              {{ data.item[field.key] }}
            </span>
          </span>
        </template>

        <template #cell(actions)="row">
          <span v-for="action in itemsData.actions" :key="action.id">
            <router-link
              v-if="action.action == 'route'"
              :to="name + '/' + action.to + '/' + row.item.id"
            >
              <b-button class="mr-2">{{ action.label }}</b-button>
            </router-link>
            <delete-row-btn
              @deleteRow="onDeleteRow"
              v-if="action.action == 'delete'"
              :label="action.label"
              :rowId="row.item.id"
            />
          </span>
        </template>

        <template #table-busy>
          <div class="text-center my-2">
            <b-spinner class="align-middle me-2"></b-spinner>
            <strong>Загрузка...</strong>
          </div>
        </template>
      </b-table>
    </b-col>
  </b-row>
</template>

<script>
import { mapActions, mapMutations } from "vuex";

import ChangeFieldModal from "./ChangeFieldModal.vue";
import NameCell from "./NameCell.vue";
import BooleanField from "./fields/BooleanField.vue";
// import DateField from "./fields/DateField.vue";
import DeleteRowBtn from "./DeleteRowBtn.vue";

export default {
  components: { NameCell, BooleanField, ChangeFieldModal, DeleteRowBtn },
  props: [
    "parent",
    "itemsData",
    "fieldsData",
    "isBusy",
    "filter",
    "perPage",
    "currentPage",
    "name",
  ],
  data() {
    return {
      SDesc: false,
    };
  },
  computed: {
    localFields() {
      if (this.parent) {
        return this.fieldsData.list.filter((x) => x.key != this.parent);
      }
      return this.fieldsData.list;
    },
    cellTypes() {
      return this.fieldsData.list.filter((x) => x?.type);
    },
    // selectableFields() {
    //   return this.fieldsData.list.filter((x) => x.type == "selectable");
    // },
  },
  methods: {
    ...mapActions(["deleteRow"]),
    ...mapMutations(["updateTableItem"]),
    onUpdateField({ id, fields: { field, value } }) {
      console.log("[upd]", this.name, id, field, value);
      this.updateTableItem({ collection: this.name, id, field, value });
    },
    onDeleteRow(rowId) {
      this.deleteRow({ table_name: this.name, row_id: rowId });
    },
    getFieldById(id, model, field) {
      if (this.fieldsData.models[model]) {
        return this.fieldsData.models[model].find((x) => x.id == id)[field];
      }
      return "";
    },
  },
};
</script>
