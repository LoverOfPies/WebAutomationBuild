<template>
  <div>
    <b-button
      v-if="label != ''"
      :class="noTruncate ? '' : 'text-truncate'"
      :disabled="disabled"
      :size="size"
      block
      @click="showFieldModal($event.target)"
    >
      {{ displayedLabel }}
    </b-button>

    <b-skeleton v-else type="input"></b-skeleton>

    <b-modal
      :id="fieldModal.id"
      :title="fieldModal.title"
      scrollable
      footer-bg-variant=""
      centered
      @hide="resetFieldModal"
    >
      <SearchBar @filterChange="onFilterChange" :filter="searchFilter" />
      <b-table
        :id="tableId"
        :items="items"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        :filter="searchFilter"
        empty-text="Нет записей"
        empty-filtered-text="По вашему запросу не найдено данных"
        bordered
        show-empty
        responsive
        class="modal-table"
        @filtered="onSearched"
      >
        <template #cell(actions)="row">
          <b-button variant="primary" @click="selectRow(row.item)">
            Выбрать
          </b-button>
        </template>
      </b-table>

      <template #modal-footer>
        <b-row style="width: 100%">
          <b-col class="pl-0">
            <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              :aria-controls="tableId"
              first-number
              last-number
            ></b-pagination>
          </b-col>

          <b-col cols="4">
            <b-button
              v-if="resetBtn"
              variant="danger"
              class="d-block ms-auto"
              @click="resetFilters"
            >
              Сбросить
            </b-button>
          </b-col>
        </b-row>
      </template>

      <!--  -->
      <!-- <template #modal-footer>
        <div class="d-none"></div>
        <b-button variant="danger" @click="cancel()"> Отмена </b-button>
                <b-button variant="success" @click="ok()"> OK </b-button>
      </template> -->
    </b-modal>
  </div>
</template>

<script>
import SearchBar from "@/components/tables/SearchBar.vue";

let uid = 0;

export default {
  components: { SearchBar },
  props: [
    "label",
    "model",
    "rowId",
    "items",
    "disabled",
    "resetBtn",
    "size",
    "no-truncate",
  ],
  data() {
    uid += 1;
    return {
      fieldModal: {
        id: `field-modal-${uid}`,
        title: "Выберите из списка",
      },
      tableId: `table-modal-${uid}`,
      perPage: 150,
      currentPage: 1,
      filter: null,
      labelReplacement: "",
      searchFilter: null,
      searchedRows: 0,
    };
  },
  methods: {
    showFieldModal(button) {
      this.$bvModal.show(this.fieldModal.id, button);
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
      this.currentPage = 1;
    },
    resetFilters() {
      this.$emit("resetFilters", this.rowId);
      this.$bvModal.hide(this.fieldModal.id);
    },
    onSearched(_arr, len) {
      this.searchedRows = len;
    },
    resetFieldModal() {},
    selectRow(item) {
      let fields = {
        field: this.model,
        value: parseInt(item.id),
      };
      this.$emit("updateField", {
        id: this.rowId,
        fields: fields,
      });
      this.$emit("labelChange", {
        id: parseInt(item.id),
        model: this.model,
      });
      this.$bvModal.hide(this.fieldModal.id);
    },
  },
  computed: {
    fields() {
      return [
        { key: "name", sortable: true, label: "Наименование" },
        { key: "actions", label: " " },
      ];
    },
    rows() {
      if (this.searchFilter) {
        return this.searchedRows;
      }
      return this.items ? this.items.length : 0;
    },
    displayedLabel() {
      return this.labelReplacement ? this.labelReplacement : this.label;
    },
  },
};
</script>

<style lang="scss">
.modal-table table td {
  padding: 0.35rem 0.75rem;
}
</style>
>
