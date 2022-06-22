<template>
  <div id="nav">
    <div>
    <router-link class="iconHome" to="/"><img src="logo.png" alt="Logo Braining"></router-link>
    </div>
    <div class="center">
      <router-link to="/">Home  |</router-link>
      <router-link to="/match">  Match</router-link>
    </div>
    <div class="log">
      <!-- <router-link class="singUp" to="/signUp"> Sign Up </router-link> -->
      <router-link  to="/logIn"> Log In </router-link>
    </div>
    <button @click="onClickedLogOut"><i class="fa fa-sign-out"></i> LogOut </button>

 </div>
  <router-view />
  
  <footer>
    <compFooter></compFooter>
  </footer>
</template>

<script>

import { useStorage } from "@vueuse/core";
import compFooter from "@/pages/components/footer.vue"

export default {
  components:{
    compFooter
  },

  data() {
    return {
      localUser: useStorage("auth", {}),
    };
  },
  computed: {
    loggedUser() {
      return this.localUser.name
    },        
  },

  methods: {
    onClickedLogOut(){
      this.localUser = {}
      this.$router.push("/logIn")
      console.log(this.localUser)

    }, 
    
    
  }
};
</script>

<style scoped>
  #nav{
    display: grid;
    grid-template-columns: 10% auto 20%;
    
  }

  .center{
    padding-left: 15%;
  }

  img{
    width:2rem;
    height: 2rem;
  }

  button {
    grid-column: 3 / 3;
    background-color: lightblue;
  }

  .singUp{
      border-right: 2px solid black;
      margin: 3px;

  }

  .log{
    display:block;
  }

@media screen and (max-width: 620px){

  .singUp{
      border-right: none;
  }
  #nav{
    display: flex; 
    
  }
  

}
</style>