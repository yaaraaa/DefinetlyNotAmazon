<template>
  <div class="page-product">
    <div class="column is-multiline">
        <div class="column is-9">
            <figure class="image mb-6">
                <img v-bind:src="product.get_image">
            </figure>

            <h1 class="title">{{ product.name }}</h1>
            <p>{{ product.descriptions }}</p>
        </div>

        <div class="column is-3">
            <h2 class="subtitle">Information</h2>

            <p><strong>Price: </strong>${{ product.price }}</p>
            
        </div>

    </div>
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
    name: 'ProductView',
    data() {
        return {

        }
    }
}
</script>
