<template>
  <b-form-datepicker
    v-model="input"
    placeholder="Выберите дату"
    locale="ru-RU"
    :hide-header="true"
    :readonly="readOnly"
  ></b-form-datepicker>
</template>

<script>
export default {
  props: ["model", "readOnly", "value"],
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
