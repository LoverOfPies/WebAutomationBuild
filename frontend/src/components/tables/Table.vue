<template>
  <b-row>
    <b-col>
      <b-table
        id="table"
        class="text-nowrap table-scrollable"
        :style="{ height: tableHeight }"
        :items="itemsData.list"
        :fields="localFields"
        :per-page="perPage"
        :current-page="currentPage"
        :busy="isBusy"
        :filter="filter"
        :sort-desc.sync="SDesc"
        :sticky-header="tableHeight"
        no-border-collapse
        empty-text="Нет записей"
        empty-filtered-text="По вашему запросу не найдено данных"
        sort-by="id"
        head-variant="light"
        bordered
        responsive
        show-empty
        @filtered="onFiltered"
      >
        <!-- TODO: readonly states management -->
        <template
          v-for="field in fieldsData.list"
          v-slot:[`cell(${field.key})`]="data"
        >
          <span :key="field.key">
            <boolean-field
              v-if="data.field.type == 'boolean'"
              :state="data.item[field.key]"
              :field="field.key"
              :rowId="data.item.id"
              :isEditable="true"
              @updateField="onUpdateField"
            />
            <float-field
              v-else-if="data.field.type == 'float'"
              :model="data.item[field.key]"
              :field="field.key"
              :rowId="data.item.id"
              :isEditable="true"
              :currentPopupRef="currentPopupRef"
              @editPopupShown="onEditPopupShown"
              @updateField="onUpdateField"
            />
            <int-field
              v-else-if="data.field.type == 'integer'"
              :model="data.item[field.key]"
              :field="field.key"
              :rowId="data.item.id"
              :isEditable="true"
              :currentPopupRef="currentPopupRef"
              @editPopupShown="onEditPopupShown"
              @updateField="onUpdateField"
            />
            <date-field
              v-else-if="data.field.type == 'date'"
              :value="data.item[field.key]"
              :field="field.key"
              :rowId="data.item.id"
              :isEditable="true"
              :currentPopupRef="currentPopupRef"
              @editPopupShown="onEditPopupShown"
              @updateField="onUpdateField"
            />
            <change-field-modal
              class="mx-2"
              v-else-if="data.field.type == 'selectable'"
              :label="getFieldById(data.item[field.key], field.key, 'name')"
              :model="field.key"
              :rowId="data.item.id"
              :items="fieldsData.models[field.key]"
              @updateField="onUpdateField"
            />
            <span v-else-if="data.field.type === 'caption'">
              <text-field
                :value="data.item[field.key]"
                :isEditable="false"
              />
            </span>
            <text-field
              v-else
              :value="data.item[field.key]"
              :field="field.key"
              :rowId="data.item.id"
              :isEditable="true"
              :currentPopupRef="currentPopupRef"
              @editPopupShown="onEditPopupShown"
              @updateField="onUpdateField"
            />
          </span>
        </template>

        <template #cell(name)="data">
          <text-field
            field="name"
            width="350"
            fieldType="textarea"
            :value="data.item['name']"
            :rowId="data.item.id"
            :isEditable="true"
            :currentPopupRef="currentPopupRef"
            @editPopupShown="onEditPopupShown"
            @updateField="onUpdateField"
          />
        </template>

        <template #cell(actions)="row">
          <div class="mx-2">
            <span v-for="action in itemsData.actions" :key="action.id">
              <router-link
                v-if="action.action == 'route'"
                :to="name + '/' + action.to + '/' + row.item.id"
              >
                <b-button class="mr-2">{{ action.label }}</b-button>
              </router-link>
              <b-button
                v-if="action.action === 'copy'"
                class="mr-2"
                :title="action.label"
                @click="copyWorkGroup({ id: row.item.id })"
              >
                <b-icon icon="back"></b-icon>
              </b-button>
              <router-link
                v-if="action.action === 'versioning'"
                :to="name + '/versioning/' + row.item.id"
              >
                <b-button class="mr-2" :title="action.label"
                  ><b-icon icon="clock-history"></b-icon
                ></b-button>
              </router-link>
              <delete-row-btn
                v-if="action.action == 'delete'"
                :label="action.label"
                :rowId="row.item.id"
                @deleteRow="onDeleteRow"
              />
            </span>
          </div>
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
import BooleanField from "./fields/BooleanField.vue";
import FloatField from "./fields/FloatField.vue";
import IntField from "./fields/IntField.vue";
import DateField from "./fields/DateField.vue";
import TextField from "./fields/TextField.vue";
import DeleteRowBtn from "./DeleteRowBtn.vue";

export default {
  components: {
    BooleanField,
    FloatField,
    IntField,
    DateField,
    TextField,
    ChangeFieldModal,
    DeleteRowBtn,
  },
  props: [
    "parent",
    "itemsData",
    "fieldsData",
    "isBusy",
    "filter",
    "perPage",
    "currentPage",
    "name",
    "tableSpacing",
  ],
  data() {
    return {
      SDesc: false,
      currentPopupRef: null,
    };
  },
  computed: {
    localFields() {
      if (this.parent) {
        return this.fieldsData.list.filter((x) => x.key != this.parent);
      }
      return this.fieldsData.list;
    },
    tableHeight() {
      return `calc(100vh - ${this.tableSpacing}px)`;
    },
  },
  methods: {
    ...mapActions(["deleteRow", "copyWorkGroup"]),
    ...mapMutations(["updateTableItem"]),
    onUpdateField({ id, fields: { field, value } }) {
      console.log("[upd]", this.name, id, field, value);
      this.updateTableItem({ collection: this.name, id, field, value });
    },
    onEditPopupShown(popupRef) {
      this.currentPopupRef = popupRef;
    },
    onDeleteRow(rowId) {
      this.deleteRow({ table_name: this.name, row_id: rowId });
    },
    // FIXME: check if field exists while trying to access it
    getFieldById(id, model, field) {
      if (this.fieldsData.models[model]) {
        return this.fieldsData.models[model].find((x) => x.id == id)[field];
      }
      return "";
    },
    onFiltered(arr, len) {
      this.$emit("filtered", arr, len);
    },
  },
};
</script>
