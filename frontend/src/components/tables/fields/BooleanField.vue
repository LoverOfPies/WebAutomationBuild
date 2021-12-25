<template>
  <div>
    <b-form-checkbox
      v-model="input"
      :value="checked"
      :unchecked-value="unchecked"
      :disabled="readOnly"
      size="lg"
    />
  </div>
</template>

<script>
export default {
  props: ["model", "readOnly", "state"],
  data() {
    return {
      input: this?.state ? this.state : false,
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
