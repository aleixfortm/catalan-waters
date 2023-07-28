<template>
  <v-hover v-slot="{ isHovering }">
    <v-card
      @mouseover="handleMouseOver"
      @mouseout="handleMouseOut"
      :elevation="isHovering ? 24 : 6" 
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
  </v-hover>
</template>

<script>

export default {
    props: ["reservoirName", "reservoirPicture", "reservoirProvince"],
    data() {
      return {
        isHovering: false
      }
    },
    computed: {
        imageSource() {
            return require(`@/assets/${this.reservoirPicture}`);
        }
    },
    methods: {
      handleMouseOver() {
        this.isHovering = true;
      },
      handleMouseOut() {
        this.isHovering = false;
      }
    }
}
</script>

<style scoped>
</style>