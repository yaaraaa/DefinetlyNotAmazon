<template>
  <div class="page-product">
        <div class="column is-multiline">
        <div class="column is-9">
            <figure class="image mb-6" v-for="product in product" v-bind:key="product.product_id">
                <img v-bind:src="product.image">
            </figure>
            <h1 class="subtitle" v-for="product in product" v-bind:key="product.product_id">{{ product.name }}</h1>
            <div class="details" v-for="product in product" v-bind:key="product.product_id">
              <p>Brand: {{ product.brand }}</p>
              <p>Model: {{ product.model }}</p>
            </div>
        </div>
        <div class="column is-3">
            <p v-for="product in product" v-bind:key="product.product_id"><strong>Price: </strong>${{ product.price }}</p>
            
            <div class="field has-addons mt-6">
                <div class="control">
                    <input type="number" class="input" min="1" v-model="quantity">
                </div>
                <div class="control">
                    <a class="button is-info" @click="addToCart">Add to cart</a>
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
    name: 'ProductView',
    data() {
        return {
            product: [],
            quantity: 1
        }
    }, 
    mounted() {
    this.getProduct()
    },
    methods: {
        getProduct() {
          const id_slug = this.$route.params.id
          console.log(id_slug)
          axios.get(`http://localhost:5000/product/${id_slug}`)
          .then(response => {
            this.product = response.data
            console.log(response.data)
          })
          .catch(error => {
            console.log(error)
          })

          // changing tab name
          document.title = this.product.name + ' | HighTech'

        },
        addToCart() {
            // correct quantity value if any changes happen to it
            if (isNaN(this.quantity || this.quantity < 1)) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast ({
                message: 'The product was added to cart',
                type: 'is-info',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right'
            })
        },
       
    }
}

</script>
