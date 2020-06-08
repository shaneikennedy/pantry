import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./Home.vue";
import Recipes from "./Recipes.vue";
import Login from "./Login.vue";
import RecipeInfo from "./RecipeInfo.vue";
import store from "./store";

const unauthenticatedRoutes = ["login", "home"];

const routes = [
  {
    path: "/",
    component: Home,
    name: "home"
  },
  {
    path: "/recipes",
    component: Recipes,
    name: "recipes"
  },
  {
    path: "/login",
    component: Login,
    name: "login"
  },
  {
    path: "/recipes/:recipe_id",
    component: RecipeInfo,
    name: "recipe-info"
  }
];

Vue.use(VueRouter);
const router = new VueRouter({
  routes,
  mode: "history"
});

function isTokenExpired(tokenExpiration) {
  const today = new Date().toJSON();
  return today > tokenExpiration;
}

router.beforeEach((to, from, next) => {
  const toRequiresAuth = !unauthenticatedRoutes.includes(to.name);
  const user = store.state.user;
  if (toRequiresAuth && !user) {
    next({ path: "/login" });
  } else if (user && isTokenExpired(user.expiry)) {
    next({ path: "/login" });
  } else {
    next();
  }
});

export default router;
