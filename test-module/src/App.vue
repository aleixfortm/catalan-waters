<template>
  <div id="app">
    <h1>TESTING VUE APP</h1>
    <apiChart />
  </div>
</template>

<script>

import apiChart from './components/apiChart.vue';

export default {
  name: 'App',
  components: { 
    apiChart 
  }
}

</script>





<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
