<template>
  <div>
    <div :class="isEditable ? 'cell-padding' : ''">
      <b-form-checkbox
        v-model="input"
        :value="checked"
        :unchecked-value="unchecked"
        :disabled="readOnly"
        size="lg"
        @change="onUserChange"
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
  methods: {
    onUserChange(newState) {
      this.input = newState;

      let fields = {
        field: this?.field ? this.field : this.model,
        value: newState,
      };
      this.$emit("updateField", {
        id: this?.rowId ? this.rowId : -1,
        fields: fields,
      });
    },
  },
  watch: {
    state: function (newValue) {
      this.input = newValue;
    },
  },
};
</script>
