<template>
  <div class="project-title">PROJECT 1</div>
  <div class="project-desc">Create a component that shows the name of 3 friends. The names cannot be written in the HTML code, and must be passed from the script section to the template section.
  Hints: variables that are sharable across the component are written within the "data" section of the script. Variables in the template are written inside double curly braces.</div>
  <project-one></project-one>
  <div class="project-desc">Create a component variable that is set to false or true. Make one of your friends render depending on the value of that variable. Hint: use v-if</div>
  <br>
  <div class="project-title">PROJECT 2</div><br>

  <div class="project-title">PROJECT 3</div><br>

  <div class="project-title">PROJECT 4</div><br>

  <div class="project-title">PROJECT 5</div><br>

  <div class="project-title">PROJECT 6</div><br>

</template>

<script>
import ProjectOne from "./components/ProjectOne.vue";

export default {
  components: {
    ProjectOne
  }
}

</script>

<style>
* {
  font-family:'Gill Sans', Calibri;
}

.project-title {
  margin: auto;
  font-size: 30px;
  text-align: center;
}

.project-desc {
  width: 1080px;
  font-size: 18px;
  margin: auto;
  text-align: center;
  text-justify: center;
}
</style>