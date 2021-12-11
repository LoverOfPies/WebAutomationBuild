import Vue from "vue";
import VueRouter from "vue-router";
import Estimate from "../views/Estimate.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Расчет",
    component: Estimate,
  },
  {
    path: "/dict/:name",
    name: "dict",
    props: true,
    component: () =>
      import(/* webpackChunkName: "base_units" */ "../views/Dict.vue"),
  },
  {
    path: "/dict/:parent/:name/:id",
    name: "child-dict",
    props: true,
    component: () =>
      import(/* webpackChunkName: "base_units" */ "../views/Dict.vue"),
  },
  {
    path: "/settings",
    name: "settings",
    component: () =>
      import(/* webpackChunkName: "base_units" */ "../views/Settings.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
