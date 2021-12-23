<template>
  <div id="app" class="d-flex" ref="root">
    <side-bar :items="sidebarItems" />
    <div class="d-flex flex-column w-100 overflow-hidden">
      <router-view />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import SideBar from "@/components/SideBar.vue";

export default {
  components: {
    SideBar,
  },
  computed: mapGetters(["sidebarItems"]),
  methods: mapActions(["fetchSidebarItems"]),
  mounted() {
    this.fetchSidebarItems();
  },
};
</script>
