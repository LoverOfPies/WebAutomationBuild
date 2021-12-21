<template>
  <div>
    <search-bar @filterChange="onFilterChange" :filter="searchFilter" />

    <b-table
      bordered
      responsive
      show-empty
      id="table"
      class="text-nowrap"
      :fields="fields"
      :items="items"
      :filter="searchFilter"
    >
      <template #cell(actions)="row">
        <b-button
          variant="success"
          class="mr-2"
          @click="exportToExcel(row.item.id)"
        >
          Выгрузить в Excel
        </b-button>
        <b-button @click="row.toggleDetails">
          Подробнее {{ row.detailsShowing ? "&#8593;" : "&#8595;" }}
        </b-button>
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
          <b-col><b>Цена заказчика:</b> {{ row.item.id }}</b-col>
          <b-col class="text-right">
            <b-button class="mr-2">Материалы</b-button>
            <b-button class="mr-2">Работы</b-button>
            <b-button variant="info">Редактировать</b-button>
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

export default {
  components: { SearchBar },
  data() {
    return {
      searchFilter: null,
      fields: [
        { key: "name", label: "Наименование" },
        { key: "actions", label: "Действия" },
      ],
      items: [
        {
          id: -1,
          name: "ХАРДКОД",
        },
      ],
    };
  },
  computed: {
    ...mapGetters(["estimatesList"]),
  },
  methods: {
    ...mapActions(["loadEstimateInfo"]),
    async init() {
      this.loadEstimateInfo();
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
    exportToExcel(id) {
      console.log(`TODO: implement exportToExcel(${id})`);
    },
    // toggleEditingView() {
    //   this.$emit("toggleEditingView", true);
    // },
  },
  mounted() {
    this.init();
  },
};
</script>
