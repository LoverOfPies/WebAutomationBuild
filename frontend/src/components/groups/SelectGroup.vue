<template>
  <div>
    <!-- TODO: get tech group name -->
    <b-form-group label="tech group placeholder" v-slot="{ ariaDescribedby }">
      <b-form-checkbox
        v-for="item in items.list"
        :key="item.id"
        :checked="item.checked"
        :aria-describedby="ariaDescribedby"
        @change="changeSelection($event, item.id)"
      >
        {{ item.name }}
      </b-form-checkbox>
    </b-form-group>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: ["items", "fields", "id", "name"],
  data() {
    return {
      child_table: this.fields.list[0].key,
      parent_table: this.fields.list[1].key,
      parent_id: this.id,
    };
  },
  computed: {
    //   options() {
    //     return this.items.list.map(function (item) {
    //       return { text: item.name, value: item.id };
    //     });
    //   },
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
