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
  

}
</script>

<style scoped>

img {
  height: 15rem;
  padding-top: 8rem;
  border: none;
}

.home{
  height: 100vh;
}
h1{
  font-size: 7rem;
  font-family: 'Skranji', cursive;
}
</style>
