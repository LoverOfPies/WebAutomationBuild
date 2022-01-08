<template>
  <div>
    <div v-if="isEditable" class="position-relative">
      <div class="text d-flex align-items-center">
        <span class="me-2">{{ value }}</span>
        <b-icon
          icon="pencil-square"
          class="cursor-pointer"
          @click="showChangeInput(true)"
        />
      </div>

      <!--  -->
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

        <b-form-textarea
          v-if="fieldType == 'textarea'"
          v-model="input"
          type="text"
          class="border-white"
          rows="3"
          max-rows="6"
          :value="input"
          :style="width ? 'min-width:' + width + 'px' : ''"
        />
        <b-form-input
          v-else
          v-model="input"
          type="text"
          class="border-white"
          placeholder="Введите текст"
          :value="input"
          :style="width ? 'min-width:' + width + 'px' : ''"
        />
      </b-card>
      <!--  -->
    </div>
    <span v-else>
      {{ value }}
    </span>
  </div>
</template>

<script>
export default {
  props: [
    "value",
    "isEditable",
    "field",
    "rowId",
    "readOnly",
    "width",
    "fieldType",
  ],
  data() {
    return {
      input: "",
      editing: false,
    };
  },
  methods: {
    showChangeInput(state) {
      this.input = this.value;
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
