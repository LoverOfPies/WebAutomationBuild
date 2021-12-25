<template>
  <div>
    <div v-if="!editing" class="text">
      <span class="me-2">{{ data.value }}</span>
      <b-icon
        icon="pencil-square"
        class="cursor-pointer"
        @click="showChangeInput(true)"
      />
    </div>

    <b-input-group v-else>
      <b-form-input v-model="value"></b-form-input>

      <template #append>
        <b-button @click="changeName" variant="success" class="rounded-0">
          <b-icon icon="check" />
        </b-button>
        <b-button
          @click="showChangeInput(false)"
          variant="danger"
          class="rounded-end"
          ><b-icon icon="x"
        /></b-button>
      </template>
    </b-input-group>
  </div>
</template>

<script>
export default {
  props: ["data"],
  data() {
    return {
      editing: false,
      value: this.data.value,
      id: this.data.item.id,
    };
  },
  methods: {
    showChangeInput(state) {
      this.value = this.data.value;
      this.editing = state;
    },
    changeName() {
      let fields = {
        field: "name",
        value: this.value,
      };
      this.$emit("updateField", {
        id: this.id,
        fields: fields,
      });
      this.editing = false;
    },
  },
};
</script>

<style lang="scss" scoped>
.cursor-pointer {
  cursor: pointer;
}
.text {
  padding: 0.375rem 0.75rem;
  border: 1px solid transparent;
}
</style>
