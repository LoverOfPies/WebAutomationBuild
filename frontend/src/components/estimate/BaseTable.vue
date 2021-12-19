<template>
  <div>
    <b-card class="mb-2" no-body header="Базовые работы">
      <b-list-group flush>
        <b-list-group-item
          v-for="baseWork in baseWorksList"
          :key="baseWork.id"
          >{{ baseWork.name }}</b-list-group-item
        >
      </b-list-group>
    </b-card>

    <b-card class="mb-2" header="Дополнительные работы">
      <b-form-checkbox-group v-model="selectedAdditionalWorks">
        <b-form-checkbox
          v-for="additionalWork in notBaseWorksList"
          :key="additionalWork.id"
          :value="additionalWork.id"
          >{{ additionalWork.name }}</b-form-checkbox
        >
      </b-form-checkbox-group>
    </b-card>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  data() {
    return {
      selectedAdditionalWorks: [],
    };
  },
  computed: {
    ...mapGetters(["worksList", "baseWorksList", "notBaseWorksList"]),
  },
  methods: {
    ...mapActions(["loadWorks"]),
    async init() {
      this.loadWorks({ table_name: "work" });
    },
  },
  mounted() {
    this.init();
  },
};
</script>
