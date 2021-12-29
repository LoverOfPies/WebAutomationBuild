<template>
  <div>
    <search-bar @filterChange="onFilterChange" :filter="searchFilter" />

    <b-table
      :fields="fields"
      :items="estimatesList"
      :filter="searchFilter"
      id="table"
      class="text-nowrap"
      head-variant="light"
      bordered
      responsive
      show-empty
    >
      <template #cell(actions)="row">
        <!-- <b-button
          variant="success"
          class="mr-2"
          @click="exportToExcel(row.item.id)"
        >
          Выгрузить в Excel
        </b-button> -->
        <b-button class="mr-2" @click="row.toggleDetails">
          Подробнее {{ row.detailsShowing ? "&#8593;" : "&#8595;" }}
        </b-button>
        <delete-row-btn @deleteRow="onDeleteRow" :rowId="row.item.id" />
      </template>

      <template #table-busy>
        <div class="text-center my-2">
          <b-spinner class="align-middle me-2"></b-spinner>
          <strong>Загрузка...</strong>
        </div>
      </template>

      <template #row-details="row">
        <!-- <b-card> -->
        <b-row class="mb-2">
          <b-col><b>Цена заказчика:</b> {{ row.item.price_client }}</b-col>
          <b-col class="text-right">
            <EstimateModal
              class="mr-2"
              label="Материалы"
              :childId="row.item.id"
              type="materials"
            />
            <EstimateModal
              class="mr-2"
              label="Работы"
              :childId="row.item.id"
              type="works"
            />
            <!-- <b-button variant="info" @click="editEstimate(row.item.id)"
              >Редактировать</b-button
            > -->
          </b-col>
        </b-row>
        <!-- </b-card> -->
      </template>
    </b-table>
  </div>
</template>

<script>
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/
import { mapGetters, mapActions } from "vuex";

import SearchBar from "../tables/SearchBar.vue";
import DeleteRowBtn from "../tables/DeleteRowBtn.vue";
import EstimateModal from "./EstimateModal.vue";

export default {
  components: { SearchBar, DeleteRowBtn, EstimateModal },
  data() {
    return {
      searchFilter: null,
      // TODO: gather fields from DB
      fields: [
        { key: "client_fio", label: "Наименование" },
        { key: "actions", label: "Действия" },
      ],
    };
  },
  computed: {
    ...mapGetters(["estimatesList"]),
  },
  methods: {
    ...mapActions(["loadEstimateInfo", "deleteEstimate"]),
    async init() {
      this.loadEstimateInfo();
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
    onDeleteRow(id) {
      this.deleteEstimate({ table_name: "estimate", id });
    },
    exportToExcel(id) {
      console.log(`TODO: implement exportToExcel(${id})`);
    },
    editEstimate(id) {
      this.$emit("toggleEditingView", true, id);
    },
  },
  mounted() {
    this.init();
  },
};
</script>
