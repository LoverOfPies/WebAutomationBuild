<template>
  <b-pagination
    v-model="currentPageLocal"
    :total-rows="rows"
    :per-page="perPage"
    first-number
    last-number
    aria-controls="table"
  ></b-pagination>
</template>

<script>
export default {
  props: ["rows", "perPage", "currentPage"],
  data() {
    return {
      currentPageLocal: this.currentPage,
    };
  },
  watch: {
    currentPage: function (newCurrentPage) {
      this.currentPageLocal = newCurrentPage;
    },
    currentPageLocal: function (newCurrentPage) {
      this.$emit("pageChange", newCurrentPage);
    },
  },
};
</script>
