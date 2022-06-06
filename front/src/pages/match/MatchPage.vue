<template>
  <div id="container">
    <h1>Match Game</h1>
    <h2>Instructions</h2>
    <article>Connect the image with the correct color</article>
    <!-- <p>tittle</p> -->
    <!-- {{id_img}} -->
    <section v-for="item of this.randomQuestions" :key="item">
      <transition name="fade">
        <img :id="item.id" v-show="item.show"  :class="{selected: item.id === id_img, correct: !item.show }" @click="onClickImg(item.id)" :src="item.img_id" alt="img">
      </transition>
      {{item.id_img}}
      <transition name="fade">
      <p :id="item.id" v-show="item.show"  :class="{selected: item.id === id_desc, correct: !item.show }" @click="onClickDesc(item.id)">{{item.description}}</p>
      </transition>
    </section>
    
    <button v-if="totQuestionsAnswered == this.randomQuestions.length" @click="resultsButton()">See my results</button>
    <button v-else @click.prevent="checkMatch">Check Match</button>

  </div>
</template>

<script>
import config from "../../config.js"
// import {autoAnimate} from "@formkit/auto-animate"
// import { onMounted } from "vue"
// onMounted(() => {
//   autoAnimate(.value) // thats it!
// }) 

export default {
  
  name: "Match",
  data() {
    return {
      tittle: "Prueba",
      questions:[],
      randomQuestions:[],
      id_img: "",
      id_desc:"",
      wrongMatchs:"",
      correct:false,
      showResultsButton: false,
      totQuestionsAnswered: 0,
    }
  },

  computed: {

  },

  mounted() {
    this.loadData();

  },

  methods: {
    async loadData() {
      //this.randomQuestions = [{"show": "true", "id":"0", "id_img": "apple.png", "description":"Leaf"}, {"id":"1","id_img": "leafTree.png", "description":"Apple", "show":"true"}]
      const response = await fetch(`${config.API_PATH}/asocia`);
      this.randomQuestions = await response.json();

    },

    onClickImg(id){
      this.id_img = id

    },

    onClickDesc(id){
      this.id_desc = id
    },

    idIsNotEmpty(){
      if (this.id_img != "" && this.id_desc !=""){
        return true
      }      
    },
    
    ansIsCorrect(){
      
      if (this.id_img === this.id_desc){
        
        this.randomQuestions[this.id_img -1].show = false

        return true
      }
    },

    checkMatch(){
      if (this.idIsNotEmpty()){
        if (this.ansIsCorrect()){
          this.id_img = ""
          this.id_desc = ""
          this.totQuestionsAnswered++
          
        }
        else{
          this.wrongMatchs ++
        }
      }
      
    },
    
    resultsButton(){
      console.log("RESULT BUTTON")
      let results = {"game_name": "Match Game", "id_user": "1" ,"wrong_matches": this.wrongMatchs}
      console.log("results>: " , results.game_name)
      
      
      const settings = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(results),
      };

      fetch(`${config.API_PATH}/results`, settings);
      this.$router.push("/results/ResultsPage.vue");
    }
    

    
  }
}
</script>

<style>
  #container {
    
    height: 100vh;
  }
  img{
    width: 7rem;
    height: 7rem;
  }
  section{
    display: flex;
    justify-content: space-around;
    
  }
  p{
    display: flex;
    align-items: center;
  }
  
  .selected {
    border: 2px yellow solid;
  }
  .unselected{
    border: none;
  }
  .correct{
    border: green 2px solid;
  }

  
  .uncorrect{
    border: red 2px solid;
  }

  
  .fade-leave-active {
    opacity: 0;
    transition:  2s ease;   
  }

  

  
</style>