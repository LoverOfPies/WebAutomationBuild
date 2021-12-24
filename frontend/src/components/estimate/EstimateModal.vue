<template>
  <span>
    <b-button @click="showFieldModal($event.target)">
      {{ label }}
    </b-button>

    <b-modal :id="modalId" :title="label" size="lg" centered>
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
      />

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
    },
    onFilterChange(newValue) {
      this.searchFilter = newValue;
    },
  },
  mounted() {
    if (this.type == "materials") {
      this.loadEstimateMaterials({ id: this.childId });
    } else {
      this.loadEstimateWorks({ id: this.childId });
    }
  },
};
</script>
