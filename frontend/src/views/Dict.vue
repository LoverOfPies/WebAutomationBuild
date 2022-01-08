<template>
  <div>
    <Title :title="localTitle" back="true" />

    <b-container fluid class="p-4">
      <b-row>
        <b-col cols="12">
          <!-- search bar -->
          <search-bar
            v-if="mode == null"
            @filterChange="onFilterChange"
            :filter="searchFilter"
          />
          <!-- filters -->
          <Filters
            v-if="filtersData.model.length != 0"
            :filtersData="filtersData"
            @applyFilters="onApplyFilters"
            @resetFilters="onResetFilters"
            @filterLabelChange="onFilterLabelChange"
            ref="filters"
          />
          <!-- table -->
          <Table
            v-if="mode == null"
            :parent="parent"
            :itemsData="itemsData"
            :fieldsData="fieldsData"
            :filter="searchFilter"
            :isBusy="isBusy"
            :perPage="perPage"
            :currentPage="currentPage"
            :name="name"
          />
          <!-- select group -->
          <b-row>
            <b-col cols="12" lg="10" xl="8">
              <SelectGroup
                v-if="mode != null && groupField == null"
                :items="itemsData"
                :fields="fieldsData"
                :id="id"
                :name="name"
              />
              <RadioGroup
                v-if="mode != null && groupField != null"
                :items="itemsData"
                :groupField="groupField"
                :fields="fieldsData"
                :id="id"
                :name="name"
              />
            </b-col>
          </b-row>
          <!-- bottom navigation -->
          <b-row v-if="mode == null">
            <b-col cols="8">
              <!-- pagination -->
              <Pagination
                :rows="itemRowsLength"
                :perPage="perPage"
                :currentPage="currentPage"
                @pageChange="onPageChange"
              />
            </b-col>
            <b-col cols="4">
              <add-data-btn
                class="text-end"
                :parent="parent"
                :parentId="id"
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

import Title from "@/components/Title.vue";
import SearchBar from "../components/tables/SearchBar.vue";
import Filters from "../components/tables/Filters.vue";
import Table from "../components/tables/Table.vue";
import Pagination from "../components/tables/Pagination.vue";
import AddDataBtn from "../components/tables/AddDataBtn.vue";
import SelectGroup from "../components/groups/SelectGroup.vue";
import RadioGroup from "../components/groups/RadioGroup.vue";

export default {
  components: {
    Title,
    SearchBar,
    Filters,
    Table,
    Pagination,
    AddDataBtn,
    SelectGroup,
    RadioGroup,
  },
  props: ["name", "id", "parent"],
  data() {
    return {
      searchFilter: null,
      perPage: 10,
      currentPage: 1,
      isReadOnly: false,
    };
  },
  computed: {
    ...mapGetters([
      "title",
      "parent_name",
      "mode",
      "groupField",
      "isBusy",
      "isFiltered",
      "itemsData",
      "fieldsData",
      "selectableFields",
      "itemRowsLength",
      "filtersData",
      "filterParams",
    ]),
    localTitle() {
      if (this.mode === "many_to_many" && this.parent) {
        this.getParentNameById({ table_name: this.parent, id: this.id });
        return `${this.title.substring(0, this.title.lastIndexOf(" "))} ${
          this.parent_name
        }`;
      }
      return this.title;
    },
    compiledParams() {
      let initialParams = {};
      if (this?.parent) {
        initialParams = {
          [this.parent]: this.id,
        };
      }
      if (this.mode != null) {
        initialParams["mode"] = this.mode;
        initialParams["child"] = this.fieldsData.list[0].key;
      }
      if (this.groupField != null) {
        initialParams["child"] = this.fieldsData.list[1].key;
      }
      return initialParams;
    },
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
      "getParentNameById",
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
      let params = this.compiledParams;
      if (id != 0) {
        params = { ...params, ...this.filterParams };
      }
      this.getItems({ name: [this.name], params });
    },
    onResetFilters(id) {
      this.resetFilters(id);
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
    onFilterLabelChange({ itemId, model }) {
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
      this.searchFilter = null;
      await this.getTableInfo({ name: this.name });
      this.getItems({ name: this.name, params: this.compiledParams });

      /*
        Sticky table fix
        FIXME: rewrite using https://bootstrap-vue.org/docs/directives/visible 
      */
      function isElementInViewport(el) {
        var rect = el.getBoundingClientRect();
        return (
          rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <=
            (window.innerHeight || document.documentElement.clientHeight) &&
          rect.right <=
            (window.innerWidth || document.documentElement.clientWidth)
        );
      }
      const table = document.querySelector(".table-responsive");
      if (table != null) {
        setTimeout(function () {
          if (!isElementInViewport(table)) {
            table.classList.add("b-table-sticky-header");
            table.style.maxHeight = "500px";
          } else {
            table.classList.remove("b-table-sticky-header");
            table.style.maxHeight = "unset";
          }
        }, 500);
      }
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
