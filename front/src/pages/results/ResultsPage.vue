<template>
  <div class="resultsPage">
    <h1>Results</h1>
    <section v-if="!userIsNotLogged" class="results">
      <table>
        <tr id="heders">
          <th>Game Name</th>
          <th>Mistakes</th>
          <th>Date</th>
        </tr>
        <tr v-for="round of this.results" :key="round">
          <td>{{round.game_name}}</td>
          <td>{{round.wrong_matches}}</td>
          <td>{{round.date}}</td>
        </tr>
      </table>
    </section>
    <section v-else class="noLogged">
      <div class="noLoggedContent">
        <p>You have to</p>
        <a href="/signUp" class="signUp">
        <p>Sign Up</p>
        </a>
        <p>or</p>
        <a href="/logIn" class="logIn">
        <p>Log In</p>
        </a>
        <p>to see your results.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { getResults } from "@/services/api.js"
export default {
  name: 'Results',
  data() {
    return {
      results: {},
      userIsNotLogged: false,
    }
  },

  mounted() {
    this.loadData();

  },

  methods: {
    async loadData(){
      this.results = await getResults()
      if (this.results === false) {
        this.userIsNotLogged = true
      }
    }
  }

}
</script>

<style scoped>

h1{
  font-weight: bold;
}

table{
  background-color: #177fff44;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.219), 0 6px 20px 0 rgba(0, 0, 0, 0.212);
  width: 70%;
  height: 40vh;
  font-size: 16px;
  
}

th{
  font-weight: bold;
}
#heders{
  border: 1px solid rgb(0, 0, 0);
  color:rgb(108, 30, 182);
}
table  th {
  border-bottom: 2px solid rgba(0, 0, 0, 0.267);
  border-collapse: collapse;
}

.resultsPage{
  padding-top: 10rem;
  height: 100vh;
}
.results{
  display: flex;
  justify-content: center;
  
}
.noLogged{
  display: flex;
  justify-content: center;
  padding: 5rem;
  height: 100vh;
  font-size: 20px;  
}

.noLoggedContent p{
  color:black;
}
.noLoggedContent{
  border: 2px solid yellow;
  
  border-radius: .5rem;
  height: 20rem;
  padding: 1rem;
  background-color: rgba(255, 255, 0, 0.315);
}

@media screen and (max-width: 480px){
  .resultsPage{
    padding-top: 15rem;
  }
}

</style>