<template>
  <div>
    <b-card v-if="showBase" class="mb-4" :no-body="baseWorksList.length != 0" header="Базовые работы">
      <div v-if="baseWorksList.length == 0">
        Базовые работы отсутствуют!
      </div>
      <b-list-group v-else flush>
        <b-list-group-item
          v-for="baseWork in baseWorksList"
          :key="baseWork.id"
          >{{ baseWork.name }}</b-list-group-item
        >
      </b-list-group>
    </b-card>

    <b-card class="mb-2" :no-body="notBaseWorksList.length != 0" header="Дополнительные работы">
      <div v-if="notBaseWorksList.length == 0">
        Дополнительные работы отсутствуют!
      </div>
      <b-list-group v-else flush>
        <b-list-group-item
          v-for="additionalWork in notBaseWorksList"
          :key="additionalWork.id"
        >
          <b-form-checkbox
            v-model="selectedAdditionalWorks"
            :value="additionalWork.id"
            >{{ additionalWork.name }}</b-form-checkbox
          >
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  props: ["showBase"],
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
  watch: {
    selectedAdditionalWorks(newList) {
      this.$emit("updateAdditionalWorks", newList);
    },
  },
  mounted() {
    this.init();
  },
};
</script>
