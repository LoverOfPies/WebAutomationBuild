<template>
  <div>
    <Title :title="title" back="true" />

    <b-container fluid class="p-4">
      <b-row>
        <b-col cols="12" xl="8">
          <!-- search bar -->
          <search-bar v-if="mode == null" @filterChange="onFilterChange" :filter="searchFilter" />
          <!-- filters -->
          <Filters
            v-if="filtersData.model.length != 0"
            :filtersData="filtersData"
            @applyFilters="onApplyFilters"
            @resetFilters="onResetFilters"
            @filterLableChange="onFilterLableChange"
            ref="filters"
          />
          <!-- table -->
          <Table
            v-if="mode == null"
            :itemsData="itemsData"
            :fieldsData="fieldsData"
            :filter="searchFilter"
            :isBusy="isBusy"
            :perPage="perPage"
            :currentPage="currentPage"
            :name="name"
          />
          <!-- select group -->
          <select-group v-else :items="itemsData" :fields="fieldsData" :id="id" :name="name">
          </select-group>
          <!-- bottom navigation  v-if="mode == null"-->
          <b-row >
            <b-col cols="10">
              <!-- pagination -->
              <Pagination
                :rows="itemRowsLength"
                :perPage="perPage"
                :currentPage="currentPage"
                @pageChange="onPageChange"
              />
            </b-col>
            <b-col cols="2">
              <add-data-btn
                class="text-end"
                :readOnly="isReadOnly"
                :fields="fieldsData.list"
                :fieldsModels="fieldsData.models"
                @addNewRow="onAddNewRow"
              />
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
/*eslint no-unused-vars: ["error", { "argsIgnorePattern": "^_" }]*/
import { mapGetters, mapActions, mapMutations } from "vuex";

import API from "../api/ApiUtils.js";

import Title from "@/components/Title.vue";
import SearchBar from "../components/tables/SearchBar.vue";
import Filters from "../components/tables/Filters.vue";
import Table from "../components/tables/Table.vue";
import Pagination from "../components/tables/Pagination.vue";
import AddDataBtn from "../components/tables/AddDataBtn.vue";
import SelectGroup from "../components/groups/SelectGroup.vue";

export default {
  components: { Title, SearchBar, Filters, Table, Pagination, AddDataBtn, SelectGroup },
  props: ["name", "id", "parent"],
  data() {
    return {
      API: new API(this),
      searchFilter: null,
      perPage: 10,
      currentPage: 1,
      isReadOnly: false,
    };
  },
  computed: {
    ...mapGetters([
      "title",
      "mode",
      "isBusy",
      "isFiltered",
      "itemsData",
      "fieldsData",
      "selectableFields",
      "itemRowsLength",
      "filtersData",
      "filterParams",
    ]),
  },
  methods: {
    ...mapActions([
      "getItems",
      "getFieldsModels",
      "getFiltersItems",
      "resetFiltersFromId",
      "getTableInfo",
      "applyFilters",
      "addNewRow",
    ]),
    ...mapMutations([
      "updateFieldsList",
      "resetItemsActions",
      "updateItemsActions",
      "resetFiltersModel",
      "updateFiltersModel",
      "resetFilterState",
      "addTableItem",
      "updateObj",
      "updateFilterLabel",
    ]),
    onApplyFilters({ _id, fields }) {
      this.applyFilters(fields);
      this.getItems({ name: [this.name], params: this.filterParams });
    },
    resetFilters(id = 0) {
      this.resetFiltersFromId(id);
      let params = {};
      if (id != 0) {
        params = this.filterParams;
      }
      this.getItems({ name: [this.name], params });
    },
    onResetFilters(id) {
      this.resetFilters(id);
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
    onFilterLableChange({ itemId, model }) {
      this.updateFilterLabel({ itemId, model });
    },
    onPageChange(newCurrentPage) {
      this.currentPage = newCurrentPage;
    },
    onAddNewRow(item) {
      this.resetFilters(0);
      this.addNewRow({ table_name: this.name, row: item });
    },
    async init() {
      await this.getTableInfo({ name: this.name });
      let params = {};
      if (this?.parent) {
        params = {
          [this.parent]: this.id,
        };
      }
      if (this.mode != null) {
        params["mode"] = this.mode;
        params["child"] = this.fieldsData.list[0].key;
      }
      // console.log(this.mode, params);
      this.getItems({ name: this.name, params });
    },
  },
  mounted() {
    this.init();
  },
  watch: {
    name: function () {
      this.init();
    },
  },
};
</script>
