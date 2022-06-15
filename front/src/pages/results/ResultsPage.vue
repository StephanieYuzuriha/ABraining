<template>
  <div class="results">
    <h1>Results</h1>
    <section v-if="!userIsNotLogged">
      <table >
        <tr>
          <th>Game number</th>
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
    <section v-else>
      You have to
      <a href="/signUp" class="signUp">
        Sign Up
      </a>
      <p>or</p>
      <a href="/lonIn" class="logIn">
        Log In
      </a>
      to see your results.
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
h1 {
  font-style: italic;
}
</style>