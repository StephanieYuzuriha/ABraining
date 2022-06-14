<template>
  <div id="nav">
    <router-link to="/">Home</router-link> | 
    <router-link to="/match">Match</router-link> | 
    <router-link to="/results">Results</router-link> | 
    <router-link to="/signUp">Sign Up</router-link>  | 
    <router-link to="/logIn">Log In</router-link>
  </div>
  <router-view />
</template>

<script>
import { useStorage } from "@vueuse/core";

export default {
  data() {
    return {
      localUser: useStorage("user", {}),
    };
  },
  computed: {
    loggedUser() {
      return this.localUser.name;
    },
  },
};
</script>
