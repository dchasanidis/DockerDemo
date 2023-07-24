<template>
  <div>
    <h1>GET Request Response:</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <div v-for="(product, index) in response" :key="index">
        <p>Name: {{ product.name }}</p>
        <p>Price: {{ product.price }}</p>
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      response: null,
      loading: true,
      error: null,
    };
  },
  mounted() {
    this.makeGetRequest();
  },
  methods: {
    makeGetRequest() {
      fetch('http://localhost:5001/products')
        .then((response) => response.json())
        .then((data) => {
          this.response = data;
          this.loading = false;
        })
        .catch((error) => {
          this.error = 'Error fetching data';
          this.loading = false;
        });
    },
  },
};
</script>
