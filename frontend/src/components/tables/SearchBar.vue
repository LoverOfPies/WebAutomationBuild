<template>
  <b-row class="mb-4">
    <b-col>
      <b-form-group class="mb-0">
        <b-input-group>
          <b-form-input
            id="filter-input"
            v-model="filterLocal"
            type="search"
            placeholder="Введите для поиска..."
          ></b-form-input>

          <b-input-group-append>
            <b-button
              class="rounded-end rounded-0"
              :disabled="!filterLocal"
              @click="clearFilter"
            >
              Очистить
            </b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form-group>
    </b-col>
  </b-row>
</template>

<script>
export default {
  props: ["filter"],
  data() {
    return {
      filterLocal: this.filter,
    };
  },
  methods: {
    clearFilter() {
      this.filterLocal = null;
      this.$emit("filterChange", this.filterLocal);
    },
  },
  watch: {
    filterLocal: function (newValue) {
      this.$emit("filterChange", newValue);
    },
  },
};
</script>
