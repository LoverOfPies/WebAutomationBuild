<template>
  <div>
    <div v-if="isEditable" class="position-relative">
      <div class="text d-flex justify-content-between align-items-center">
        <span class="me-2">{{ simplifyDate(value) }}</span>
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
              :disabled="!isSelectedDate"
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

        <!--  -->
        <b-input-group>
          <b-form-input
            v-model="dateEditInput"
            type="text"
            class="border-white"
            placeholder="ДД.ММ.ГГГГ"
            autocomplete="off"
          />
          <b-input-group-append>
            <b-form-datepicker
              v-model="convertedDate"
              button-only
              right
              locale="ru-RU"
              @context="onContext"
            />
          </b-input-group-append>
        </b-input-group>
        <!--  -->
      </b-card>
    </div>
    <div v-else>
      <b-form-datepicker
        v-model="input"
        placeholder="Выберите дату"
        locale="ru-RU"
        :hide-header="true"
        :readonly="readOnly"
      />
    </div>
  </div>
</template>

<script>
let uid = 0;

export default {
  props: [
    "model",
    "readOnly",
    "value",
    "isEditable",
    "field",
    "rowId",
    "currentPopupRef",
  ],
  data() {
    uid += 1;

    return {
      input: "",
      editing: false,
      selected: "",
      dateEditInput: "",
      popupRef: `date-popup-${uid}`,
    };
  },
  methods: {
    showChangeInput(state) {        
      this.input = this.value;
      this.dateEditInput = this.simplifiedDate;
      this.editing = state;

      if (state) {
        this.$emit("editPopupShown", this.popupRef);
      }
    },
    onContext(ctx) {
      this.selected = ctx.selectedYMD;
      this.dateEditInput = this.simplifyDate(ctx.selectedYMD);
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
    simplifyDate(dateString) {
      return new Date(dateString).toLocaleDateString("ru-RU");
    },
  },
  computed: {
    isSelectedDate() {
      return !!this.selected;
    },
    simplifiedDate() {
      const dateString = this.input ? this.input : "12.12.1999";
      return this.simplifyDate(dateString);
    },
    convertedDate: {
      get: function () {
        return this.simplifiedDate.split(".").reverse().join("-");
      },
      set: function (newValue) {
        this.input = newValue;
      },
    },
  },
  mounted() {
    if (this.value) {
      this.input = this.value;
    }
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
    dateEditInput: function (newValue) {
      const dateString = newValue.split(".").reverse().join("-");
      const date = new Date(dateString);

      if (date instanceof Date && !isNaN(date.valueOf())) {
        this.input = dateString;
      } else {
        console.log("NOT OK:", dateString);
        this.selected = "";
      }
    },
  },
};
</script>
