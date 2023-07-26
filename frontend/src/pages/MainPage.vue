<template>
      <div class="main-title" :class="{ 'is-loading': isLoading }">catalan waters</div>
      <div class="subtitle" :class="{ 'is-loading': isLoading }">Explore real-time data from the catalan water reservoirs</div>
      
      <div class="svg-container" :class="{ 'is-loading': isLoading }">
        <svg-map class="main-container__img"></svg-map>
      </div>
      <background-holder></background-holder>

      <div class="chart"><canvas id="volumes"></canvas></div>
</template>


<script>
import SvgMap from "../components/SvgMap.vue";
import Chart from 'chart.js/auto';
import BackgroundHolder from "@/components/BackgroundHolder.vue";

export default {
  components: {
    SvgMap,
    BackgroundHolder
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


(async function() {
  const data = [

    { year: 2001, count: 72 },

    { year: 2003, count: 82 },

    { year: 2005, count: 83 },

    { year: 2007, count: 90 },

    { year: 2009, count: 81 },

    { year: 2011, count: 83 },

    { year: 2013, count: 70 },

    { year: 2015, count: 65 },

    { year: 2017, count: 63 },

    { year: 2019, count: 80 },

    { year: 2021, count: 72 },

    { year: 2023, count: 49 },
  ];

  new Chart(
    document.getElementById('volumes'),
    {
      type: 'line',
      data: {
        labels: data.map(row => row.year),
        datasets: [
          {
            label: 'Total reservoir water volume (%)',
            data: data.map(row => row.count)
          }
        ]
      }
    }
  );
})();
    },
  }
</script>


<style scoped>

#volumes {
  padding: 10px;
  margin: 50px 0 0 0;
}

.main-title {
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.863);
    letter-spacing: 8px;
    font-size: 30px;
    line-height: 1.5;
    font-weight: 300;
    opacity: 1;
    font-weight: bold;
    margin: 0 auto;
    align-self: center;
    width: fit-content;
    text-align: center;
    transition: opacity 0.4s ease-in-out 0s, visibility 1.5s 0s, margin-top ease-in 1s;
    padding: 10px 0 0 0;
    border-radius: 5px;
}

.subtitle {
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.466);
  letter-spacing: 3px;
  font-size: 18px;
  line-height: 1.5;
  font-weight: 300;
  opacity: 1;
  margin: auto;
  align-self: center;
  width: fit-content;
  text-align: center;
  transition: opacity 0.4s ease-in-out 0s, visibility 1.5s 0s, margin-top ease-in 1s;
  padding: 10px;

  border-radius: 5px;
}


.svg-container {
  display: flex;
  justify-content: center;
  margin: 5px auto;
  opacity: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  width: 45%;
  transition: all 0.8s ease-in;
}

.svg-container.is-loading {
  opacity: 1;
}

.main-container__img {
  border-radius: 15px;
  opacity: 0;
  transition: 1s ease-in all;
}

.main-container__img.is-loading {
  opacity: 1;
}


</style>