<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light ps-2">
      <div class="container-fluid">
        <div v-if="showBackBtn">
          <button @click="$router.go(-1)" class="btn btn-primary">Назад</button>
        </div>
        <span
          class="navbar-brand mb-0 me-auto"
          :class="{ 'ms-4': showBackBtn }"
        >
          {{ title }}
        </span>
        <!-- <div v-if="exim == 'true'" class="d-flex">
                    <button class="btn btn-primary me-2" type="button">Импорт</button>
                    <button class="btn btn-primary" type="button">Экспорт</button>
                </div> -->
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  props: ["title", "exim", "back"],
  computed: {
    showBackBtn() {
      if (this.back == "true") {
        return this.$store.getters.sidebarItems.find(
          (x) => x.title == this.title
        )
          ? false
          : true;
      }
      return false;
    },
  },
};
</script>
