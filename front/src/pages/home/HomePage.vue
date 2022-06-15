<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />
    <h1>Braining</h1>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/info')
      this.info = await response.json()
    }
  }


}
</script>

<style scoped>
img {
  height: 15rem;
  padding-top: 6rem;
}

.home{
  height: 100vh;
  font-family: 'Skranji', cursive;
}
h1{
  font-size: 7rem;
}
</style>
