<template>
  <b-form-input
    v-model="input"
    type="number"
    step="any"
    :no-wheel="true"
    placeholder="Введите число"
  />
</template>

<script>
export default {
  props: ["model"],
  data() {
    return {
      input: "",
    };
  },
  watch: {
    input: function (newValue) {
      let fields = {
        field: this.model,
        value: newValue,
      };
      this.$emit("updateField", {
        id: -1,
        fields: fields,
      });
    },
  },
};
</script>

<style></style>
