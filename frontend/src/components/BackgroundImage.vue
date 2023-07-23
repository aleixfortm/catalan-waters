<template>
    <div class="background-container " :class="{ 'is-loading': isLoading }">
      <!-- Background Image -->
      <div class="background-image" :class="{ 'is-loading': isLoading }"></div>

      <!-- Noise Pattern -->
      <div class="background-noise"></div>

      <slot></slot>

    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isLoading: false, // Add a isLoading data property
      };
    },
    mounted() {
      setTimeout(() => {
        this.isLoading = true;
      }, 10); // Set the delay time in milliseconds
    },
  };
  </script>

  <style>
  .background-container {
    position: relative;
    width: 100vw;
    background-color: black;
    height: 100vh;
    transition: opacity 1s ease-in 0s;
  }

  .background-container.is-loading {
      opacity: 1;
      visibility: visible;
  }
  
  .background-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('../assets/background2.jpg');
    background-size: cover;
    opacity: 0.05;
    transition: opacity 1s ease-in 0.5s, visibility 1.5s 0s;
  }

  .background-image.is-loading {
    opacity: 1;
  }

  .background-noise {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('data:image/svg+xml;charset=utf8,%3Csvg%20viewBox%3D%220%200%20512%20512%22%20width%3D%22512%22%20height%3D%22512%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%20%3Cfilter%20id%3D%22noise%22%3E%20%3CfeTurbulence%20type%3D%22fractalNoise%22%20baseFrequency%3D%220.875%22%20result%3D%22noise%22%20%2F%3E%20%3CfeColorMatrix%20type%3D%22matrix%22%20values%3D%220.0390625%200%200%200%200%200%200.03515625%200%200%200%200%200%200.03515625%200%200%200%200%200%200.56640625%200%22%20%2F%3E%20%3C%2Ffilter%3E%20%3Crect%20filter%3D%22url%28%23noise%29%22%20x%3D%220%22%20y%3D%220%22%20width%3D%22512%22%20height%3D%22512%22%20fill%3D%22transparent%22%20opacity%3D%221%22%20%2F%3E%3C%2Fsvg%3E');
    opacity: 1;
    transition: opacity 1.5s ease-in-out 0s, visibility 1.5s 0s;
  }
  
  .content {
    position: absolute;
    top: 50%; /* Center the content vertically */
    left: 50%; /* Center the content horizontally */
    transform: translate(-50%, -50%); /* Adjust for centering */
    text-align: center; /* Center the text inside the div */
    color: #ffffff; /* Set the text color */

  }
  </style>