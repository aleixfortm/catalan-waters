<template>
  <div>
    <h1>This is a test to retrieve data from Flask</h1>
    <ul>
      <li v-for="item in filteredData" :key="item.id">
        {{item.day}} : {{ item.absolut_volume }} {{ "L" }}</li>
    </ul>
    <h1>This is a chart test using the data above</h1>

  </div>
</template>

<script>

export default {
  data() {
    return {
      items: [],
      maxItems: 100
    };
  },
  mounted() {
    this.fetchItems();
  },
  methods: {
    fetchItems() {
      fetch('http://127.0.0.1:5000/api')
        .then(response => response.json())
        .then(data => {
          this.items = data;
        })
    }
  },
  
  computed: {
    filteredData() {
      const limitedItems = this.items.slice(0, this.maxItems);
      return limitedItems.filter(item => item.station == "Embassament de Susqueda (Osor)");
    }
  }
};

</script>
