<template>
  <div class="page-product">
    <figure class="image mb-6">
            <img v-bind:src="product.image">
    </figure>
    
  </div>
  
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ProductView',
    data() {
        return {
            product: {},
            quantity: 1
        }
    }, 
    mounted() {
    this.getProduct()
    },
    methods: {
        getProduct() {
          
          axios.get('/product/:id')
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
