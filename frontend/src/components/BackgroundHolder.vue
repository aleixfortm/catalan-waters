
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
          v-for="n in 3"
          :key="n"
          :value="n"
        >
          <v-container fluid class="color">
            <v-row>
                <slot></slot>
            </v-row>
          </v-container>
        </v-window-item>
      </v-window>
    </v-card>
  </template>
  
  <script>
    export default {
      data: () => ({
        tab: null,
      }),
    }
  </script>


<style scoped>
    .width {
        width: 95%;
        margin: auto;
        background-color: rgba(255, 255, 255, 0.781);
    }

</style>