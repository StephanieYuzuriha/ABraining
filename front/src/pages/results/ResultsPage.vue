<template>
  <div class="results">
    <h1>Results</h1>
    <table>
      <tr>
        <th>Game number</th>
        <th>Mistakes</th>
        <th>Date</th>
      </tr>
      <tr v-for="round of this.results" :key="round">
        <td>{{round.game_numer}}</td>
        <td>{{round.wrong_matches}}</td>
        <td>{{round.date}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import config from "../../config.js"
export default {
  name: 'Results',
  data() {
    return {
      results: {}
    }
  },

  mounted() {
    this.loadData();

  },

  methods: {
    async loadData(){
      const response = await fetch(`${config.API_PATH}/results`);
      this.results = await response.json();
      console.log(this.results)
    }
  }

}
</script>

<style scoped>
h1 {
  font-style: italic;
}
</style>