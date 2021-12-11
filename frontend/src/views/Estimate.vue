<template>
  <div>
    <Title :title="title" back="false" />

    <b-container fluid class="p-4">
      <b-row> hello </b-row>
    </b-container>
  </div>
</template>

<script>
import Title from "@/components/Title.vue";

export default {
  components: { Title },
  data() {
	  return {
		  title: "Расчет",
	  }
  }
};
</script>
