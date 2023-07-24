<template>
  <div class="main-container">
    <div class="pollancre">POLLANCRE AAHHAHAH</div>
    <div class="svg-container" :class="{ 'is-loading': isLoading }">
      <svg-map></svg-map>
    </div>
  </div>
</template>


<script>
import SvgMap from "../components/SvgMap.vue";


export default {
  components: {
    SvgMap
  },
  data() {
    return {
      isLoading: false,
    }
  },
  mounted() {
      setTimeout(() => {
        this.isLoading = true;
      }, 350); // Set the delay time in milliseconds
    },
  }
</script>


<style>
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

.text-container {
  flex: 1;

  padding: 10px;
}

.svg-container {
  display: flex;
  justify-content: center;
  margin: auto;
  opacity: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  width: 50%;
  transition: all 0.8s ease-in;
}

.svg-container.is-loading {
  opacity: 1;
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
  text-align: center; 
  color: #ffffff;
  width: 90%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  flex: 1;
  padding: 20px;
}

.main-container__img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 15px;
  opacity: 0;
  flex: 1;
  padding: 20px; /* Add padding as needed */
  transition: 1s ease-in all;
}

.main-container__img.is-loading {
  opacity: 1;
}

@media (max-width: 1080px) {
  .main-container {
    flex-direction: column;
    height: 75%;
  }
}

</style>