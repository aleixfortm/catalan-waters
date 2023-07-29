<template>
  <div>
    <h1>This is a test to retrieve data from Flask</h1>
    <ul>
      <li v-for="item in items" :key="item.id">{item.station}</li>
    </ul>

  </div>
</template>

<script>
export default {
  data() {
    return {
      items: []
    };
  },
  mounted() {
    this.fetchItems();
  },
  methods: {
    fetchItems() {
      fetch('http://127.0.0.1:5000/api')
        .then(response => response.json())
        console.log(this.items)
        .then(data => {
          this.items = data;
        })
        
        .catch(error => {
          console.error('Error fetching items:', error);
        });
    }
  }
};

</script>
