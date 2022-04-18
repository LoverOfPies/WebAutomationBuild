<template>
  <span>
    <b-button @click="showFieldModal($event.target)">
      {{ label }}
    </b-button>

    <b-modal
      :id="modalId"
      :title="label"
      size="lg"
      footer-bg-variant="secondary"
      centered
    >
      <SearchBar @filterChange="onFilterChange" :filter="searchFilter" />

      <b-table
        :id="tableId"
        :items="estimateModalList"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        :filter="searchFilter"
        bordered
        show-empty
        responsive
      >
        <template v-for="field in fields" v-slot:[`cell(${field.key})`]="row">
          <div class="text" :key="field.key">
            {{ row.item[field.key] }}
          </div>
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
      </b-row>

      <!--  -->
      <template #modal-footer>
        <div class="d-none"></div>
      </template>
    </b-modal>
  </span>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import SearchBar from "@/components/tables/SearchBar.vue";

export default {
  components: { SearchBar },
  props: ["label", "childId", "type"],
  data() {
    return {
      modalId: `estimate-${this.childId}-modal-${this.type}`,
      tableId: `estimate-${this.childId}-modal-${this.type}-table`,
      searchFilter: null,
      perPage: 8,
      currentPage: 1,
      fields: [{ key: "name", label: "Наименование" }],
    };
  },
  computed: {
    ...mapGetters(["estimateModalList"]),
    rows() {
      return this.items ? this.items.length : 0;
    },
  },
  methods: {
    ...mapActions(["loadEstimateMaterials", "loadEstimateWorks"]),
    showFieldModal(button) {
      this.$bvModal.show(this.modalId, button);

      if (this.type == "materials") {
        this.loadEstimateMaterials({ id: this.childId });
        this.fields = [
          { key: "material_name", label: "Наименование" },
          { key: "amount", label: "Кол-во" },
          { key: "price", label: "Цена" },
        ];
      } else {
        this.loadEstimateWorks({ id: this.childId });
        this.fields = [
          { key: "work_name", label: "Наименование" },
          { key: "client_price", label: "Цена клиента" },
          { key: "base_price", label: "Цена себестоимости" },
        ];
      }
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
  },
  mounted() {
    // if (this.type == "materials") {
    //   this.loadEstimateMaterials({ id: this.childId });
    // } else {
    //   this.loadEstimateWorks({ id: this.childId });
    // }
  },
};
</script>

<style>
.modal-footer.bg-secondary {
  display: none;
}
</style>
