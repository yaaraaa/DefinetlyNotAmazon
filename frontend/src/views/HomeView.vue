<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <!-- <img src="https://tse1.mm.bing.net/th?id=OIP.L4Ysm20ung681aw6Q0SPxQHaEK&pid=Api&P=0"/> -->
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
      <div class="column is-full">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>     
      <div class="cards">
        <div class="card mb-4"
            v-for="product in latestProducts"
            v-bind:key="product.product_id"
        >
            <div class="box">
              <figure class="image mb--4">
                  <img v-bind:src="product.image">
              </figure>
              <br>
              <h3 class="is-size-10">{{ product.name }}</h3>
              <p class="is-size-5 has-text-grey"> ${{ product.price }}</p>
              <br>
              <router-link v-bind:to="{path:'product/'+product.product_id, params:{'id':product.product_id}}" class="button is-info is-small is-rounded">View details</router-link>
            </div>
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
    }
  },
  mounted() {
    this.getLatestProducts()

    // change tab name
    document.title = 'Home | HighTech'
  },
  methods: {
    getLatestProducts() {
      const path = 'http://localhost:5000/home'
      axios
        .get(path)
        .then(response => {
          this.latestProducts = response.data
          // console.log(response.data)
          console.log(this.latestProducts)
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

<style>
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px,1fr));
    grid-gap: 0.5em;
  }

  .card {
    height: max-content;
  }

  .image {
    object-fit: cover;
    width: 150px;
    height: auto;
    margin-left: 20%;
  }
</style>
