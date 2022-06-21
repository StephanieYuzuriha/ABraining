<template>
  <div class="signUp">
      <form @submit.prevent="onSignUpButtonClicked">
        <h1>Sign-Up</h1>
        <img class="logo" src="@/assets/img/logo.png" alt="Logo de la web">
        <div class="data">
          <p class="user">Username</p>
          <input required autocomplete="new-user" class="user-input" v-model="user" type="text" name="username" placeholder="Type your username">
          <p class="warning" v-if="isUsernameAlreadyTaken">This username is already taken</p>
        </div>

        <div class="data">
          <p class="name">Name</p>
          <input required autocomplete="new-name" class="name-input" v-model="name" type="text" name="name" placeholder="Type your name">
        </div>

        <div class="data">
          <p class="password">Password</p>
          <input required autocomplete="new-password" class="password-input" v-model="password" type="password"  placeholder="Type your password">
        </div>

        <div class="data">
          <p class="password">Please repeat the password</p>
          <input required autocomplete="new-password" class="password-input" v-model="rPassword" type="password"  placeholder="Type your password">
          <p class="warning" v-if="isPasswordNotTheSame">Please verify! Passwords are not the same</p>
        </div>
             
        <button type="submit" class="sing-up">
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
      isRegister: false,

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
      if (this.isPasswordNotTheSame === false){
        const response = await signUp(this.user, this.name, this.password);
        const loginStatus = response.status;
        console.log(loginStatus)
        console.log("response", response);

        if (loginStatus === 401) {
          this.isUsernameAlreadyTaken = true
        } 
        else{
          this.$router.push("/logIn", );
        }
      }
      

    }
  }

}
</script>

<style scoped>
@media screen and (max-width: 480px) {
  .signUp{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 100vh;

  }
}

*{
  font-weight: bold;
}
.signUp{
  
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding-bottom: 2rem;

}

form{
  background-image: linear-gradient(50deg, rgba(244, 157, 255, 0), rgb(146, 30, 255));
  border-radius: 2rem;
  margin-top: 8rem;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.219), 0 6px 20px 0 rgba(0, 0, 0, 0.212);
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
  height: 1.4rem;
  font-size: 14px;
  outline-color: blue;
  border: none;
  border-bottom: 2px solid white;
  background: none;
  border-radius: .3rem;
}

input :focus{
  outline-color: blue;
}

span{
  margin: 0.5rem;
}

p{
  margin: 1rem 2rem;
  width: 17rem;
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