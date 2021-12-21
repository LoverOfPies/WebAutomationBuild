<template>
  <b-row>
    <b-col>
      <b-table
        id="table"
        class="text-nowrap"
        :items="itemsData.list"
        :fields="fieldsData.list"
        :per-page="perPage"
        :current-page="currentPage"
        :busy="isBusy"
        :filter="filter"
        :sort-desc.sync="SDesc"
        bordered
        responsive
        show-empty
      >
        <template #head(actions)="data" style="width: 1%">
          <span>{{ data.label }}</span>
        </template>

        <!-- FIXME: this accepts only <name> cell -->
        <template #cell(name)="data">
          <name-cell @updateField="onUpdateField" :data="data" />
        </template>

        <!-- Modal Buttons -->
        <template
          v-for="field in selectableFields"
          v-slot:[`cell(${field.key})`]="data"
        >
          <span :key="field.id">
            <change-field-modal
              @updateField="onUpdateField"
              :label="getFieldById(data.item[field.key], field.key, 'name')"
              :model="field.key"
              :rowId="data.item.id"
              :items="fieldsData.models[field.key]"
            />
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
            <!-- <b-button
              v-if="action.action == 'delete'"
              variant="danger"
              @click="deleteRow(row.item.id)"
            >
              {{ action.label ? action.label : "Удалить" }}
            </b-button> -->
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
import DeleteRowBtn from "./DeleteRowBtn.vue";

export default {
  components: { NameCell, ChangeFieldModal, DeleteRowBtn },
  props: [
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
  computed: {
    selectableFields() {
      return this.fieldsData.list.filter((x) => x.type == "selectable");
    },
  },
};
</script>
