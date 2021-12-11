<template>
  <div>
    <b-form-checkbox
      v-model="input"
      :value="checked"
      :unchecked-value="unchecked"
      size="lg"
    />
  </div>
</template>

<script>
export default {
  props: ["model"],
  data() {
    return {
      input: false,
      checked: true,
      unchecked: false,
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
