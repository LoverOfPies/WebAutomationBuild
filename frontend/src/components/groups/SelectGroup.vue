<template>
  <div>
    <!-- TODO: подтягивать заголовок группы -->
    <h5 v-if="items.list.length == 0">Нет доступных записей!</h5>
    <b-card v-else header="Выберите из списка" class="mb-4">
      <b-form-checkbox
        v-for="item in items.list"
        :key="item.id"
        :checked="item.checked"
        @change="changeSelection($event, item.id)"
      >
        {{ item.name }}
      </b-form-checkbox>
    </b-card>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: ["items", "fields", "id", "name"],
  data() {
    return {
      parent_id: this.id,
      child_table: this.fields.list[0].key,
      parent_table: this.fields.list[1].key,
    };
  },
  methods: {
    ...mapActions(["updateSelection"]),
    changeSelection(checked, item_id) {
      this.updateSelection({
        collection: this.name,
        parent: this.parent_table,
        parent_id: this.parent_id,
        child: this.child_table,
        child_id: item_id,
        value: checked,
      });
    },
  },
};
</script>
