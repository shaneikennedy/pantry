import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./Home.vue";
import Recipes from "./Recipes.vue";
import Register from "./Register.vue";
import Login from "./Login.vue";
import RecipeInfo from "./RecipeInfo.vue";
import RecipeCreate from "./RecipeCreate.vue";
import Profile from "./Profile.vue";
import store from "./store";

const unauthenticatedRoutes = ["login", "home", "register"];

const routes = [
  {
    path: "/",
    component: Home,
    name: "home",
    meta: {
      title: "Pantry | Home",
    }
  },
  {
    path: "/recipes",
    component: Recipes,
    name: "recipes",
    meta: {
      title: "Pantry | Recipes",
    }
  },
  {
    path: "/login",
    component: Login,
    name: "login",
    meta: {
      title: "Pantry | Login",
    }
  },
  {
    path: "/recipes/:recipe_id",
    component: RecipeInfo,
    name: "recipe-info",
    meta: {
      title: "Pantry | Recipe",
    }
  },
  {
    path: "/recipes/create",
    component: RecipeCreate,
    name: "recipe-create",
    meta: {
      title: "Pantry | Create recipe",
    }
  },
  {
    path: "/register",
    component: Register,
    name: "register",
    meta: {
      title: "Pantry | Register",
    }
  },
  {
    path: "/profile",
    component: Profile,
    name: "profile",
    meta: {
      title: "Pantry | Profile",
    }
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

router.afterEach((to) => {
  document.title = to.meta.title;
});

export default router;
