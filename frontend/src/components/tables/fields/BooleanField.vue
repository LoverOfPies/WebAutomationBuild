<template>
  <div>
    <div :class="isEditable ? 'cell-padding' : ''">
      <b-form-checkbox
        v-model="input"
        :value="checked"
        :unchecked-value="unchecked"
        :disabled="readOnly"
        size="lg"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: ["model", "readOnly", "state", "isEditable", "field", "rowId"],
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
        field: this?.field ? this.field : this.model,
        value: newValue,
      };
      this.$emit("updateField", {
        id: this?.rowId ? this.rowId : -1,
        fields: fields,
      });
    },
  },
};
</script>
