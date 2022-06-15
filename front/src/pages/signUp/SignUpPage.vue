<template>
  <div class="signUp">
    <h1>Sign-Up</h1>
    <img class="logo" src="@/assets/img/logo.png" alt="Logo de la web">

      <form class="form" @submit.prevent="register">
        <div class="data">
          <p class="user">Username</p>
          <input autocomplete="new-user" class="user-input" v-model="user" type="text" name="username" placeholder="Type your username">
          <p class="warning" v-if="isUsernameAlreadyTaken">This username is already taken</p>
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
          <p class="warning" v-if="isPasswordNotTheSame">Please verify! Passwords are not the same</p>
        </div>
             
        <button @click="onSignUpButtonClicked" class="sing-up">
          Sign-In
        </button>
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
.signUp{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: blueviolet;
  border-radius: .8rem;
  margin: 5rem 15rem;
}

.logo{
  width: 4rem;
}

.warning{
  border: 2px solid yellow;
  border-radius: .5rem;
  padding: 1rem;
}

input{
  border: none;
  height: 1.4rem;
  font-size: 14px;
  outline-color: blue;
  border-radius: .3rem;
}

input :focus{
  outline-color: blue;
}

span{
  margin: 0.5rem;
}

p{
  font-weight: bold;
  margin: 1rem 2rem;
}

.sing-up{
  margin: 1rem;
  border-radius: .5rem;
  font-size: 15px;
  background-color: violet;

}

.sing-up:hover{
  background-color: plum;
}



</style>