<template>
  <span>
    <span v-if="this.$slots.default[0].text == ''" class="shimmer"></span>
    <slot></slot>
  </span>
</template>

<script>
export default {};
</script>

<style lang="scss">
$gray700: var(--bs-gray-700);
$gray600: var(--bs-gray-600);

.shimmer {
  background: $gray700;
  background-image: linear-gradient(
    to right,
    $gray700 0%,
    $gray700 10%,
    $gray600 20%,
    $gray700 30%,
    $gray700 50%,
    $gray700 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 200px;
  display: inline-block;
  position: relative;

  border-radius: 3px;
  width: 70%;
  height: 70%;
  height: 22px;
  bottom: -3px;

  animation-fill-mode: forwards;
  animation-iteration-count: infinite;
  animation-name: placeholderShimmer;
  animation-timing-function: linear;
  animation-duration: 1s;
}

@keyframes placeholderShimmer {
  0% {
    background-position: -468px 0;
  }

  100% {
    background-position: 468px 0;
  }
}
</style>
