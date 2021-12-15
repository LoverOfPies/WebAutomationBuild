<template>
  <b-row class="mb-4">
    <b-col>
      <b-row>
        <b-col
          v-for="item in filtersData.model"
          :key="item.id"
          cols="12"
          class="mb-2"
        >
          <router-link
            :to="{
              name: 'dict',
              params: {
                name: item.key,
                title: item.multiple,
              },
            }"
          >
            <b-button class="w-100">{{ item.multiple }}</b-button>
          </router-link>
        </b-col>
      </b-row>
    </b-col>
    <b-col cols="8" class="text-end">
      <b-row>
        <b-col
          v-for="(item, index) in filtersData.model"
          :key="item.id"
          cols="12"
          class="mb-2"
        >
          <b-row>
            <b-col cols="6" class="position-relative">
              <label class="text-end lh-lg">{{ item.label }}:</label>
            </b-col>
            <b-col>
              <change-field-modal
                :ref="`filter-field-${item.key}`"
                :label="item.text"
                :model="item.key"
                :disabled="item.disabled"
                :resetBtn="true"
                :rowId="index"
                :items="getModelItems(item.key)"
                @updateField="onUpdateField"
                @labelChange="onLabelChange"
                @resetFilters="onResetFilters"
              />
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-col>
  </b-row>
</template>

<script>
import ChangeFieldModal from "./ChangeFieldModal.vue";

export default {
  components: { ChangeFieldModal },
  props: ["filtersData"],
  methods: {
    onUpdateField({ id, fields }) {
      this.$emit("applyFilters", { id, fields });
    },
    onLabelChange({ id: itemId, model }) {
      // this.$refs[`filter-field-${model}`][0].labelLocal = this.getFieldById(
      //     itemId,
      //     model,
      //     "name"
      // );
      this.$emit("filterLabelChange", { itemId, model });
    },
    onResetFilters(id) {
      this.$emit("resetFilters", id);
    },
    getFieldById(id, model, field) {
      return this.filtersData.list[model].find((x) => x.id == id)[field];
    },
    getModelItems(key) {
      let items = this.filtersData.list[key];
      const index = this.filtersData.model.findIndex((x) => x.key == key);
      if (index != 0) {
        const parent = this.filtersData.model[index - 1].key;
        if (
          this.filtersData.state[parent] &&
          this.filtersData.state[parent] != ""
        ) {
          items = this.filtersData.list[key].filter(
            (item) => item[parent] == this.filtersData.state[parent]
          );
        }
      }
      return items;
    },
  },
};
</script>
