<template>
  <div id="app">
      <background-image>
          <div class="main-container">
            <div>
              <div class="pollancre" :class="{ 'is-loading': isLoading }">EVOLUTION OF CATALAN WATER LEVELS</div>
              <br>
              <div class="pollancre-secondary" :class="{ 'is-loading': isLoading }">Even in highly developed regions, extended periods of drought can severely deplete water resources, leading to acute scarcity and posing significant challenges to water availability.</div>
            </div>
            <div>
              <img src="./assets/image2.jpg" alt="catwaters-logo" class="main-container__img" :class="{ 'is-loading': isLoading }">
            </div>
          </div>
      </background-image>
  </div>
</template>

<script>
import BackgroundImage from "./components/BackgroundImage.vue"

export default {
  components: {
    BackgroundImage
  },
  data() {
    return {
      isLoading: false
    }
  },
  mounted() {
      setTimeout(() => {
        this.isLoading = true;
      }, 150); // Set the delay time in milliseconds
    },
  }
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
  font-family: 'Source Sans Pro', sans-serif;
}

.pollancre {
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.863);
    letter-spacing: 0.225rem;
    font-size: 20px;
    line-height: 1.5;
    font-weight: 300;
    opacity: 0;
    margin-top: 30px;
    transition: opacity 0.4s ease-in-out 0s, visibility 1.5s 0s, margin-top ease-in 1s;
}

.pollancre.is-loading {
  opacity: 1;
  margin-top: 0px;
}

.pollancre-secondary {
    color: rgba(255, 255, 255, 0.527);
    letter-spacing: 0.225rem;
    font-size: 16px;
    line-height: 1.5;
    font-weight: 300;
    opacity: 0;
    transition: 1.2s ease-in-out all;
}

.pollancre-secondary.is-loading {
  opacity: 1;
}

.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 1300px;
}

.main-container__img {
  width: 550px;
  height: auto;
  border-radius: 15px;
  margin: 0 0 0 200px;
  opacity: 0;
  transition: 1s ease-in all;
}

.main-container__img.is-loading {
  opacity: 1;
}

</style>