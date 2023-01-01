<template>
    <div class="page-search">
        <div class="column is-multiline">
            <div class="column is-full">
                <h1 class="title">Search</h1>

                <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
            </div>     

            <div class="cards">
                <div class="card mb-4"
                    v-for="product in products"
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
    name: 'SearchView',
    
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | HighTech'

        let url = window.location.search.substring(1)
        let params = new URLSearchParams(url)

        if(params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
        performSearch() {
            axios
            .post(`http://localhost:5000/search/${this.query}`, {'query': this.query})
            .then(response => {
                this.products = response.data      
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
