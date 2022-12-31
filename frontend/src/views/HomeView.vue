<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
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
              <div class="button is-info is-small is-rounded">Vew details</div>
              <!-- <router-link v-bind:to="product.get_absolute_url" class="button is-info is-small is-rounded4">View details</router-link> -->
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
      // {
      //   product_id:self.product_id,
      //   date_added:self.date_added,
      //   image:self.image,
      //   brand:self.brand,
      //   model:self.model,
      //   price:self.price,
      //   name:self.name,
      //   discount_amount:self.discount_amount,
      //   date_updated:self.date_updated
      // }
      //'https://images-na.ssl-images-amazon.com/images/I/71oVh2UO8xL._SL1500_.jpg', 'https://i5.walmartimages.com/asr/67bd3300-5231-4fe7-8dbe-37562aafb8f4_1.17f76f8ffae7f60409efa7dfc601dc7f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF'
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
