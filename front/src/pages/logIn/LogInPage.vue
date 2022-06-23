<template>
  <div class="login">
      <form @submit.prevent="onLogInButtonClicked">
        <h1>Log-In</h1>
        <img class="logo" src="@/assets/img/logo.png" alt="Logo de la web">
        <p class="user">Username</p>
        <div class="data" >
          
          <span><i class="fa fa-user"></i></span>
          <input v-model="user"  autocomplete="current-user" class="user-input" type="text" name="username" placeholder="Type your username" required>
        </div>
        <p class="password">Password</p>
        <div class="data">
          
          <span><i class="fa fa-lock"></i></span>
          <input v-model="password" autocomplete="current-password" class="password-input" type="password" name="pass" placeholder="Type your password" required>
        </div>
        
        <!-- <div class="forgotPassword">
          <a href="#">
            Forgot password?
          </a>
        </div> -->
             
        <button type="submit" class="login-button">
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
  name: "logIn",

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

<style scoped>

@media screen and (max-width: 480px) {
  div{
    display: flex;
  }
}

*{
  font-weight: bold;
}

.login{
  margin-top:2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 6rem;
  background-image: linear-gradient(50deg, rgba(244, 157, 255, 0), #84b6f493);
}

form{
  height: 20rem;
  background-image: linear-gradient(50deg, rgba(244, 157, 255, 0), rgb(146, 30, 255));
  border-radius: 2rem;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.219), 0 6px 20px 0 rgba(0, 0, 0, 0.212);
  padding: 3rem;
  height: auto;;
}

.logo{
  width: 4rem;
}

.login-button{
  margin: 1rem;
  border-radius: .5rem;
  font-size: 15px;
  background-color: violet;
}
.login-button:hover{
  background-color: rgb(194, 160, 221);
}

input{
  border: none;
  height: 1.4rem;
  font-size: 14px;
  outline-color: blue;
  border-radius: .3rem;
  border: none;
  border-bottom: 2px solid white;
  background: none;
}
input :focus{
  outline-color: blue;
}

h1{
  margin-top: 0;
}

span{
  margin: 0.5rem;
}

p{
  font-weight: bold;
}

</style>
