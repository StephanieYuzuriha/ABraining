<template>
  <div id="container">
    <h1 id="title">Match Game</h1>
    <h4>Connect the image with the correct color</h4>
    <section v-for="item of this.randomQuestions" :key="item">
      <transition name="fade">
        <img :id="item.id" v-show="item.show"  :class="{selected: item.id === id_img, correct: !item.show }" @click="onClickImg(item.id)" :src="item.img_id" alt="img">
      </transition>
      {{item.id_img}}
      <transition name="fade">
        <div class="description-container" :id="item.id" v-show="item.show"  :class="{selected: item.id === id_desc, correct: !item.show }" @click="onClickDesc(item.id)">
          <p>{{item.description}}</p>
        </div>
      </transition>
    </section>
    <section>
      <p class="isWrong" v-if="wrong">Wrong Match!</p>
    </section>
    
    <button class="check-button"  v-if="totQuestionsAnswered == this.randomQuestions.length" @click="resultsButton()">See my results</button>
    <button class="check-button" v-else @click.prevent="checkMatch">Check Match</button>
    

  </div>
</template>

<script>
import config from "../../config.js"
import { addResults } from "@/services/api.js";

export default {
  
  name: "Match",
  data() {
    return {
      wrong: false,
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
          this.wrong = false
        }
        else{
          this.wrong = true
          this.wrongMatchs ++
        }
      }
      
    },
    
    async resultsButton(){
      let results = {"game_name": "Match Game", "id_user": "1" ,"wrong_matches": this.wrongMatchs}
      await addResults(results)
      
      this.$router.push("/results");
    }
    

    
  }
}
</script>

<style scoped>
  *{
    font-weight: bold;
  }
  p{
    font-size: 16px;
    color: black;
  }
  h4{
    padding-bottom: 2rem;
  }
  #container {
    height: 80%;
  }

  .check-button {
    padding: 1rem 2rem;
    border: none;
    border-radius: 10px;
    background-color: var(--secund);
    font-size: 16px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  .check-button:hover{
    background-color: plum;
  }

  .description-container {
    width: 12rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 4px solid rgb(121, 0, 235);
    border-radius: 5px;
  }

  #title {
    font-family: 'Skranji', cursive;
    font-size: 70px;
    padding-top: 6rem;
  }

  img {
    width: 12rem;
    height: 12rem;
    border: 4px solid rgb(121, 0, 235);
    border-radius: 5px;
  }

  section {
    display: flex;
    justify-content: space-around;
    margin: 10px 15rem 10px 15rem;
  }

  .isWrong{
    margin: 1rem 1rem;
    font-size: 16px;
    border: 2px solid rgb(255, 0, 0);
    text-align: center;
    width: 100vh;
    background-color: yellow;
    border-radius: 4px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  .selected {
    border: 4px yellow solid;
  }
  .unselected {
    border: none;
  }
  .correct {
    border: green 4px solid;
  }

  .uncorrect {
    border: red 4px solid;
  }

  .fade-leave-active {
    opacity: 0;
    transition:  2s ease;   
  }
  @media screen and (max-width: 800px) {
    img {
      width: 10rem;
      height: 10rem;
      border: 2px solid rgb(121, 0, 235);
    }

    .description-container {
    width: 10rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid rgb(121, 0, 235);
    }

    section {
    display: flex;
    justify-content: space-around;
    margin: 10px 2rem 10px 2rem;
    }

    #title {
    font-family: 'Skranji', cursive;
    font-size: 40px;
    padding-top: 5rem;
    }

  }
  
  @media screen and (max-width: 480px) {
    #container{
      padding-top: 20px;
      padding-bottom: 10px;
    }

    img {
      width: 8rem;
      height: 8rem;
      border: 2px solid rgb(121, 0, 235);
    }

    .description-container {
    width: 8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid rgb(121, 0, 235);
    }

    section {
    display: flex;
    justify-content: space-around;
    margin: 10px 2rem 10px 2rem;
    }

    #title {
    font-family: 'Skranji', cursive;
    font-size: 40px;
    padding-top: 5rem;
  }
  .selected {
    border: 4px yellow solid;
  }
  .unselected {
    border: none;
  }
  .correct {
    border: green 4px solid;
  }

  .uncorrect {
    border: red 4px solid;
  }

  .fade-leave-active {
    opacity: 0;
    transition:  2s ease;   
  }
}


  
</style>