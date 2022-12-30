<template>
  <div class="home">
    <section class="hero is-medium is-ligh mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
            Welcome to HighTech
        </p>
        <p class="subtitle">
            The best tech store online
        </p>
      </div>
    </section>

    <div class="column is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered"> Latest products</h2>
      </div>
    <div 
          class="column is-3"
          v-for="product in latestProducts"
          v-bind:key="product"
        >
          <div class="box">
            <figure class="image mb--4">
              <img v-bind:src="product">
            </figure>

            <!-- <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey"> ${{ product.price }}</p> -->
          </div>
        </div>
       

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
      //'https://images-na.ssl-images-amazon.com/images/I/71oVh2UO8xL._SL1500_.jpg', 'https://i5.walmartimages.com/asr/67bd3300-5231-4fe7-8dbe-37562aafb8f4_1.17f76f8ffae7f60409efa7dfc601dc7f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF'
    }
  },
  components: {
    
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      const path = 'http://localhost:5000/home'
      axios
        .get(path)
        .then(response => {
          this.latestProducts.push(response.data)
          console.log(response.data)
          //this.latestProducts = response.data
          //console.log(this.latestProducts)
        })
        .catch(error => {
          console.log(error)
        })

    }
  }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
