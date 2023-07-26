
<template>
    <v-card class="width">
        <v-card-title class="text-center justify-center py-6">
      <h1 class="font-weight-bold text-h3">
        RESERVOIRS
      </h1>
    </v-card-title>
      <v-tabs
        v-model="tab"
        color="deep-purple-accent-4"
        align-tabs="center"
      >
        <v-tab :value="1">All</v-tab>
        <v-tab :value="2">Barcelona</v-tab>
        <v-tab :value="3">Girona</v-tab>
        <v-tab :value="4">Lleida</v-tab>
        <v-tab :value="5">Tarragona</v-tab>

      </v-tabs>
      <v-window v-model="tab">
        <v-window-item
          v-for="n in 5"
          :key="n"
          :value="n"
        >
          <v-container fluid>
            <v-row>
                <reservoir-carousel :selectedTab="tabs[n - 1]"></reservoir-carousel>
            </v-row>
          </v-container>
        </v-window-item>
      </v-window>
    </v-card>
  </template>
  
  <script>
    import ReservoirCarousel from './ReservoirCarousel.vue';

    export default {
      components: {
        ReservoirCarousel
      },
      data() {
        return {
          tab: null,
          tabs: ["All", "Barcelona", "Girona", "Lleida", "Tarragona"]
        }
      }
    }
  </script>


<style scoped>
    .width {
        width: 95%;
        margin: auto;
        background-color: rgba(255, 255, 255, 0.781);
    }

</style>