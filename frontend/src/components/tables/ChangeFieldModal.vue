<template>
  <div>
    <b-button
      @click="showFieldModal($event.target)"
      :disabled="disabled"
      block
      :size="size"
      v-if="label != ''"
    >
      {{ displayedLabel }}
    </b-button>

    <b-skeleton v-else type="input"></b-skeleton>

    <b-modal
      :id="fieldModal.id"
      :title="fieldModal.title"
      footer-bg-variant="secondary"
      @hide="resetFieldModal"
      centered
    >
      <SearchBar @filterChange="onFilterChange" :filter="searchFilter" />
      <b-table
        :id="tableId"
        :items="items"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        :filter="searchFilter"
        bordered
        show-empty
        responsive
      >
        <template #cell(actions)="row">
          <b-button variant="primary" @click="selectRow(row.item)">
            Выбрать
          </b-button>
        </template>
      </b-table>

      <b-row>
        <b-col>
          <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            first-number
            last-number
            :aria-controls="tableId"
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

      <!--  -->
      <template #modal-footer>
        <div class="d-none"></div>
        <!-- <b-button variant="danger" @click="cancel()"> Отмена </b-button>
                <b-button variant="success" @click="ok()"> OK </b-button> -->
      </template>
    </b-modal>
  </div>
</template>

<script>
import SearchBar from "@/components/tables/SearchBar.vue";

let uid = 0;

export default {
  components: { SearchBar },
  props: ["label", "model", "rowId", "items", "disabled", "resetBtn", "size"],
  data() {
    uid += 1;
    return {
      fieldModal: {
        id: `field-modal-${uid}`,
        title: "Выберите из списка",
      },
      tableId: `table-modal-${uid}`,
      perPage: 8,
      currentPage: 1,
      filter: null,
      labelReplacement: "",
      searchFilter: null,
    };
  },
  methods: {
    showFieldModal(button) {
      this.$bvModal.show(this.fieldModal.id, button);
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
    resetFilters() {
      this.$emit("resetFilters", this.rowId);
      this.$bvModal.hide(this.fieldModal.id);
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
        { key: "name", sortable: false },
        { key: "actions", label: " " },
      ];
    },
    rows() {
      return this.items ? this.items.length : 0;
    },
    displayedLabel() {
      return this.labelReplacement ? this.labelReplacement : this.label;
    },
  },
};
</script>

<style>
.modal-footer.bg-secondary {
  display: none;
}
</style>
