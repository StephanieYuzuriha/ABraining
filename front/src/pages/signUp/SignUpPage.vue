<template>
  <div class="signUp">
      <form class="form" @submit.prevent="register">
        <h1>Sign-Up</h1>

        <div class="data">
          <p class="user">Username</p>
          <input autocomplete="new-user" class="user-input" v-model="user" type="text" name="username" placeholder="Type your username">
          <span v-if="isUsernameAlreadyTaken">This username is already taken</span>
        </div>

        <div class="data">
          <p class="name">Name</p>
          <input autocomplete="new-name" class="name-input" v-model="name" type="text" name="name" placeholder="Type your name">
        </div>

        <!-- <div class="data" data-validate = "Username is reauired">
          <p class="email">Email</p>
          <input class="user-input" type="text" name="username" placeholder="Type your username">
        </div> -->

        <div class="data">
          <p class="password">Password</p>
          <input autocomplete="new-password" class="password-input" v-model="password" type="password"  placeholder="Type your password">
        </div>

        <div class="data">
          <p class="password">Please repeat the password</p>
          <input autocomplete="new-password" class="password-input" v-model="rPassword" type="password"  placeholder="Type your password">
          <span v-if="isPasswordNotTheSame">Please verify! Passwords are not the same</span>
        </div>
             
        <button @click="onSignUpButtonClicked" class="login">
          Sign-In
        </button>

        <!-- <div class="signUpMedia">
          <span>
            Or Sign Up Using
          </span>
        </div>

        <div class="socialMedia">
          <a href="#" class="login100-social-item bg1">
            <i class="fa fa-facebook"></i>
          </a>

          <a href="#" class="login100-social-item bg2">
            <i class="fa fa-twitter"></i>
          </a>

          <a href="#" class="login100-social-item bg3">
            <i class="fa fa-google"></i>
          </a>
        </div> -->
      </form>          
  </div>
</template>

<script>
import { useStorage } from "@vueuse/core";
import { signUp } from "@/services/auth.js";

export default {
  name: 'SignUp',
  data() {
    return {
      user: "",
      name: "",
      password: "",
      rPassword: "",
      isUsernameAlreadyTaken: false,
      auth: useStorage("auth", {}),

    }
  },

  computed:{
    isPasswordNotTheSame(){
      if (this.password !== this.rPassword)
      {
        return true
      }

      return false
    }
  },

  mounted() {
    

  },

  methods: {
    validatePassword(){

    },
    
    async onSignUpButtonClicked() {
      console.log("entro")
      //   localStorage.userId = this.selectedUser.id;
      //   localStorage.userName = this.selectedUser.name;
      if (this.isPasswordNotTheSame === false){
        const response = await signUp(this.user, this.name, this.password);
        const loginStatus = response.status;
        console.log(loginStatus)
        console.log("response", response);

        if (loginStatus === 401) {
          this.isUsernameAlreadyTaken = true
        } 
        else{
          
          this.$router.push("/logIn");
        }
      }
      

    }
  }

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins');

/* BASIC */

html {
  background-color: #56baed;
}

body {
  font-family: "Poppins", sans-serif;
  height: 100vh;
}

a {
  color: #92badd;
  display:inline-block;
  text-decoration: none;
  font-weight: 400;
}

h2 {
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
  display:inline-block;
  margin: 40px 8px 10px 8px; 
  color: #cccccc;
}



/* STRUCTURE */

.wrapper {
  display: flex;
  align-items: center;
  flex-direction: column; 
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}

#formContent {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #fff;
  padding: 30px;
  width: 90%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  text-align: center;
}

#formFooter {
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}



/* TABS */

h2.inactive {
  color: #cccccc;
}

h2.active {
  color: #0d0d0d;
  border-bottom: 2px solid #5fbae9;
}

</style>