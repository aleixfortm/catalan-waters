<template>
      <background-image>
          <div class="main-container">

            <div class="svg-container">
              <svg-map class="main-container__img" :class="{ 'is-loading': isLoading }"></svg-map>
            </div>
          </div>

      </background-image>

</template>


<script>
import BackgroundImage from "../components/BackgroundImage.vue";
import SvgMap from "../components/SvgMap.vue";

export default {
  components: {
    BackgroundImage,
    SvgMap
  },
  data() {
    return {
      isLoading: false,
    }
  },
  methods: {
    handleMouseOver(event) {
      // Handle hover over a region
      const regionId = event.target.getAttribute('id'); // Get the ID of the region
      console.log(`Hovered over region with ID: ${regionId}`);
    },
    handleMouseOut(event) {
      // Handle leaving a region
      const regionId = event.target.getAttribute('id'); // Get the ID of the region
      console.log(`Left region with ID: ${regionId}`);
    },
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

.svg-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px; /* Add padding as needed */
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
  position: absolute;
  top: 50%; /* Center the content vertically */
  left: 50%; /* Center the content horizontally */
  transform: translate(-50%, -50%); /* Adjust for centering */
  text-align: center; /* Center the text inside the div */
  color: #ffffff; /* Set the text color */
}

.text {
  flex: 1;
  padding: 20px; /* Add padding as needed */
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

</style>