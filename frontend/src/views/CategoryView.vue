<template>
    <div class="page-category">
        <div class="column is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>
            <div class="cards">
                <div class="card mb-4"
                    v-for="product in category.products"
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
import { toast } from 'bulma-toast'

export default {
    data() {
        return { 
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    // track changes to route then calls the function again
    // function in mounted is called only once but switches between categories happen so watch fixes this problem
    watch: {
        $route(to, from) {
            if(to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        getCategory() {

            // some code similar for the one in ProductView
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
