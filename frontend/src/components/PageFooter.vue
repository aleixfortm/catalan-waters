<template>
    <v-footer
      class="bg-indigo-lighten-5 text-center d-flex flex-column margin"
    >
      <div>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-1"
          :icon="icon"
          variant="text"
        ></v-btn>
      </div>
  
      <div class="pt-0">
        This is a hobby project made by a team of 3 ambitious students. All data has been acquired from official sources at <span>gencat.cat</span>. We warmly welcome feedback or any other questions, do not hesitate to reach out to us through ourno social media above.
      </div>
  
      <v-divider></v-divider>
  
      <div>
        {{ new Date().getFullYear() }} — <strong>Guillem, Pau & Aleix</strong>
      </div>
    </v-footer>
  </template>

<script>
export default {
  data: () => ({
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram',
    ],
  }),
}
</script>

<style scoped>
    .margin {
        margin-top: 100px;
    }

    span {
      text-decoration: underline;
    }
</style>