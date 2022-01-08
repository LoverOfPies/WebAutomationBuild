<template>
  <div>
    <div v-if="isEditable" class="position-relative">
      <div class="text d-flex align-items-center">
        <span class="me-2">{{ model }}</span>
        <b-icon
          icon="pencil-square"
          class="cursor-pointer"
          @click="showChangeInput(true)"
        />
      </div>

      <b-card v-if="editing" no-body class="edit-popup shadow">
        <b-card-header
          class="d-flex justify-content-between align-items-center"
        >
          <div class="me-4">Редактирование</div>
          <div>
            <b-button
              @click="updateField"
              variant="success"
              class="pill-equal-padding me-2"
              pill
            >
              <b-icon icon="check" />
            </b-button>
            <b-button
              @click="showChangeInput(false)"
              variant="danger"
              class="pill-equal-padding"
              pill
              ><b-icon icon="x"
            /></b-button>
          </div>
        </b-card-header>

        <b-form-input
          v-model="input"
          type="number"
          step="1"
          placeholder="Введите целое число"
          class="border-white"
          :no-wheel="true"
          :value="input"
        />
      </b-card>
    </div>
    <span v-else>
      <b-form-input
        v-model="input"
        placeholder="Введите целое число"
        type="number"
        step="1"
        :no-wheel="true"
      />
    </span>
  </div>
</template>

<script>
export default {
  props: ["model", "isEditable", "field", "rowId", "readOnly"],
  data() {
    return {
      editing: false,
      input: "",
    };
  },
  methods: {
    showChangeInput(state) {
      this.input = this.model;
      this.editing = state;
    },
    updateField() {
      const fields = {
        field: this.field,
        value: this.input,
      };
      this.$emit("updateField", {
        id: this.rowId,
        fields: fields,
      });
      this.showChangeInput(false);
    },
  },
  watch: {
    input: function (newValue) {
      if (this?.isEditable) return;
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
