<template>
    <div class="page-view-items">
        <div class="columns is-multiline">
            <div class="column is-12">
                <br>
                <br>
                <br>
                <h1 class="title">Products</h1>
            </div>

            <div class="column is-12 box">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Product ID</th>
                            <th>Image</th>
                            <th>Name</th>
                            <th>Price</th>
                            <th>Brand</th>
                            <th>Model</th>
                            <th>Quantity</th>
                            <th>Discount</th>
                            <th>Date Added</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="product in products" v-bind:key="product.product_id">
                            <td>{{ product.product_id }}</td>
                            <td><img v-bind:src="product.image"></td>
                            <td>{{ product.name }}</td>
                            <td>{{ product.price }}</td>
                            <td>{{ product.brand }}</td>
                            <td>{{ product.model }}</td>
                            <td>{{ product.quantiy }}</td>
                            <td>{{ product.discount_amount }}</td>
                            <td>{{ product.date_updated }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
    data() {
        return {
        products: []
        }
    },
    mounted() {
        this.getProducts()
    },
    methods: {
        getProducts() {
        const path = 'http://localhost:5000/home'
        axios
            .get(path)
            .then(response => {
            this.products = response.data
            console.log(this.products)
            })
            .catch(error => {
            console.log(error)
            })
        }
    }
    }
</script>

<style>
img {

    width: 200px;
    height: 150px;
  }
</style>
