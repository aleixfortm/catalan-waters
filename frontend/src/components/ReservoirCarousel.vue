<template>
  <v-container>
    <v-row>
      <v-col
        v-for="(reservoir, index) in data"
        :key="index"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
      <reservoir-card
        :reservoirName="reservoir.name"
        :reservoirPicture="reservoir.picture"
        :reservoirProvince="reservoir.province">
      </reservoir-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ReservoirCard from './ReservoirCard.vue';

export default {
  components: {
    ReservoirCard
  },
  data() {
    return {
      data: [
        {
          name: "Riudecanyes",
          picture: "riudecanyes.png",
          province: "Girona"
        },
        {
          name: "Llosa del Cavall",
          picture: "llosa-del-cavall.jpg",
          province: "Barcelona"
        },
        {
          name: "Baells",
          picture: "baells3.jpg",
          province: "Girona"
        },
        {
          name: "Boadella",
          picture: "boadella.jpg",
          province: "Lleida"
        },
        {
          name: "Foix",
          picture: "foix.jpg",
          province: "Lleida"
        },
        {
          name: "Sau",
          picture: "sau2.jpg",
          province: "Lleida"
        },
        {
          name: "Siurana",
          picture: "siurana.jpg",
          province: "Tarragona"
        },
        {
          name: "Susqueda (Girona)",
          picture: "susqueda(girona).jpeg",
          province: "Girona"
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>