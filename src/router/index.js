import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "@/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Login",
    props: true,
    component: () =>
      import(/* webpackChunkName: "/" */
      "../views/Login")
  },
  {
    path: "/home",
    name: "Home",
    component: Home,
    props: true
  },
  {
    path: "/user-account",
    name: "UserAccount",
    props: true,
    component: () =>
      import(/* webpackChunkName: "UserAccount" */
      "../views/UserAccount")
  },
  {
    path: "/favorite",
    name: "Favorite",
    props: true,
    component: () =>
      import(/* webpackChunkName: "Favorite" */
      "../views/Favorite")
  },
  {
    path: "/transaction",
    name: "Transaction",
    props: true,
    component: () =>
      import(/* webpackChunkName: "Transaction" */
      "../views/Transaction")
  },
  {
    path:"/item/:slug",
    name:"ItemDetails",
    props: true,
    component: () => 
      import(/*webpackChunkName: "details"*/ "../views/ItemDetails"),
    children: [
      {
        path: ":goodSlug",
        name: "goodDetails",
        props: true,
        component: () =>
          import(/*webpackChunkName: "goodDetails"*/ "../views/goodDetails")
      }
    ],
    beforeEnter: (to, from, next) => {
      const exists = store.items.find(
        item => item.slug === to.params.slug
      );
      if (exists) {
        next();
      } else {
        next({ name: "notFound" });
      }
    }
  },
  {
    path: "/404",
    alias: "*",
    name: "notFound",
    component: () =>
      import(/* webpackChunkName: "NotFound" */
      "../views/NotFound")
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
