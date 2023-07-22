<template>
  <div id="app">
      <background-image>
          <div class="main-container">
            <div class="pollancre">EVOLUTION OF CATALAN WATER LEVELS</div>
            <div>
              <img src="./assets/image.jpg" alt="catwaters-logo" class="main-container__img">
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
  }
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
    color: rgba(255,255,255,0.839);
    letter-spacing: 0.225rem;
    width: calc(100% + 0.225rem);
    font-size: 1em;
    line-height: 1.5;
    font-weight: 300;
}

.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 1080px;
}

.main-container__img {
  width: 500px;
  height: auto;
  border-radius: 15px;
}
</style>