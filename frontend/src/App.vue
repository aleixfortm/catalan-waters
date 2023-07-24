<template>
    <main-page></main-page>
</template>

<script>
import MainPage from "./pages/MainPage.vue"

export default {
  components: {
    MainPage
  }
}
</script>

<style>
html {
  margin: 0;
  padding: 0;
  font-family: 'Source Sans Pro', sans-serif;
  background-image: 
  url('data:image/svg+xml;charset=utf8,%3Csvg%20viewBox%3D%220%200%20512%20512%22%20width%3D%22512%22%20height%3D%22512%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%20%3Cfilter%20id%3D%22noise%22%3E%20%3CfeTurbulence%20type%3D%22fractalNoise%22%20baseFrequency%3D%220.875%22%20result%3D%22noise%22%20%2F%3E%20%3CfeColorMatrix%20type%3D%22matrix%22%20values%3D%220.0390625%200%200%200%200%200%200.03515625%200%200%200%200%200%200.03515625%200%200%200%200%200%200.56640625%200%22%20%2F%3E%20%3C%2Ffilter%3E%20%3Crect%20filter%3D%22url%28%23noise%29%22%20x%3D%220%22%20y%3D%220%22%20width%3D%22512%22%20height%3D%22512%22%20fill%3D%22transparent%22%20opacity%3D%221%22%20%2F%3E%3C%2Fsvg%3E'),
  url("./assets/background1.jpg");
  background-color: rgb(32, 32, 32);
  background-repeat: repeat, no-repeat;
  background-position: center, center;
  background-attachment: fixed, fixed;
}

</style>