<template>
  <div class="login">
      <form class="login-form" @submit.prevent="onLogInButtonClicked" >
        <h1>Log-In</h1>

        <div class="data" >
          <span class="user">Username</span>
          <input v-model="user"  autocomplete="current-user" class="user-input" type="text" name="username" placeholder="Type your username">
        </div>

        <div class="data">
          <span class="password">Password</span>
          <input v-model="password" autocomplete="current-password" class="password-input" type="password" name="pass" placeholder="Type your password">
        </div>
        
        <!-- <div class="forgotPassword">
          <a href="#">
            Forgot password?
          </a>
        </div> -->
             
        <button type="submit" class="login">
          Login
        </button>

        <div>
          <spam>Or you can </spam>
          <a href="/signUp" class="signUp">
            Sign Up
          </a>
        </div>

      </form>          
  </div>
</template>

<script>
import { useStorage } from "@vueuse/core";
import { login } from "@/services/auth.js";

export default {
  data() {
    return {
      user: "",
      password: "",
      auth: useStorage("auth", {}),
    };
  },

  methods: {
    async onLogInButtonClicked() {
      console.log("entro")
      const response = await login(this.user, this.password);
      console.log("response", response);
      
      const loginStatus = response.status;
      console.log(loginStatus)
      
      if (loginStatus === 401) {
        alert("User or password are incorrect");
      } else {
        const auth = await response.json();
        console.log("auth", auth);

        this.auth = auth;
        this.$router.push("/match");
      }
    },
  },
};
</script>

<style>
</style>
