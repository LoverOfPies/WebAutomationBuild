<template>
  <span>
    <b-button variant="danger" :id="popId">
      {{ label ? label : "Удалить" }}
    </b-button>

    <b-popover :target="popId" title="Вы уверенны?">
      <b-button @click="deleteRow" variant="success" class="mr-2" size="sm">
        <b-icon icon="check" variant="light"></b-icon>
      </b-button>
      <b-button @click="closePopover" size="sm"> Отмена </b-button>
    </b-popover>
  </span>
</template>

<script>
let uid = 0;

export default {
  props: ["label", "rowId"],
  data() {
    uid += 1;
    return {
      popId: `delete-popover-${uid}`,
    };
  },
  methods: {
    deleteRow() {
      this.closePopover();
      this.$emit("deleteRow", this.rowId);
    },
    closePopover() {
      this.$root.$emit("bv::hide::popover", this.popId);
    },
  },
};
</script>
