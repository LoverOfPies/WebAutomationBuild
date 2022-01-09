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
          step="any"
          placeholder="Введите число"
          class="border-white"
          :value="input"
          :no-wheel="true"
        />
      </b-card>
    </div>
    <span v-else>
      <b-form-input
        v-model="input"
        type="number"
        step="any"
        placeholder="Введите число"
        :no-wheel="true"
      />
    </span>
  </div>
</template>

<script>
let uid = 0;

export default {
  props: [
    "model",
    "isEditable",
    "field",
    "rowId",
    "readOnly",
    "currentPopupRef",
  ],
  data() {
    uid += 1;
    return {
      editing: false,
      input: "",
      popupRef: `float-popup-${uid}`,
    };
  },
  methods: {
    showChangeInput(state) {
      this.input = this.model;
      this.editing = state;
      if (state) {
        this.$emit("editPopupShown", this.popupRef);
      }
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
    currentPopupRef: function (newValue) {
      if (this.popupRef != newValue) {
        this.showChangeInput(false);
      }
    },
  },
};
</script>
