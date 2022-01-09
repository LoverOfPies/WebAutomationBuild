<template>
  <div
    class="d-flex flex-column flex-shrink-0 p-3 bg-light vh-100 shadow"
    style="width: 280px; z-index: 1"
  >
    <a
      href="/"
      class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none no-hover"
    >
      <b-iconstack font-scale="2" class="me-3">
        <b-icon stacked icon="gear-wide" scale="1.5"></b-icon>
        <b-icon stacked icon="wrench" scale="0.75" flip-h></b-icon>
        <b-icon stacked icon="hammer" scale="0.75"></b-icon>
      </b-iconstack>
      <span class="fs-4">Automation Build</span>
    </a>
    <hr />
    <ul class="nav nav-pills flex-column">
      <li class="nav-item">
        <router-link
          to="/"
          exact-active-class="active"
          class="nav-link link-dark"
        >
          <b-icon icon="calculator" class="me-1" variant="dark"></b-icon>
          Расчеты
        </router-link>
      </li>
    </ul>

    <hr />
    <!-- Справочники -->
    <ul class="nav nav-pills flex-column mb-auto">
      <li v-for="item in items" :key="item.id">
        <router-link
          :to="{
            name: 'dict',
            params: {
              name: item.name,
            },
          }"
          active-class="active"
          class="nav-link link-dark mb-1"
        >
          <b-icon :icon="item.icon" class="me-1" variant="dark"></b-icon>
          {{ item.title }}
        </router-link>
      </li>
    </ul>

    <hr />
    <ul class="nav nav-pills flex-column">
      <li>
        <router-link
          to="/settings"
          exact-active-class="active"
          class="nav-link link-dark"
        >
          <b-icon icon="gear" class="me-1" variant="dark"></b-icon>
          Настройки
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
// icons: https://bootstrap-vue.org/docs/icons#icons

export default {
  props: ["items"],
};
</script>

<style lang="scss" scoped>
a.active svg {
  color: currentColor !important;
}

.link-dark:not(.no-hover):not(.active) {
  &:hover,
  &:focus {
    background-color: lighten($color: #007bff, $amount: 20%);
  }
}
</style>
