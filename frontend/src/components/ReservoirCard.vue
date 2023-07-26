<template>
    <v-card
      class="mx-auto"
      max-width="400"
    >
      <v-img
        class="align-end text-white"
        height="200"
        :src="imageSource"
        cover
      >
        <v-card-title><b>{{ reservoirName }}</b></v-card-title>
      </v-img>
  
      <v-card-subtitle class="pt-3">
        {{ reservoirProvince }}
      </v-card-subtitle>
  
      <v-card-text>
        <div>+5% water volume</div>
  
      </v-card-text>
  
      <v-card-actions>
  
        <v-btn 
        variant="tonal"
        color="teal-accent-4">
            EXPLORE
        </v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>

export default {
    props: ["reservoirName", "reservoirPicture", "reservoirProvince"],
    computed: {
        imageSource() {
            return require(`@/assets/${this.reservoirPicture}`);
        }
    }
}
</script>

<style scoped>
</style>