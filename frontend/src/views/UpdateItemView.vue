<template>
    <div class="page-update-item">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <br>
                <br>
                <br>
                <br>
                <h1 class="title">Update Product</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">

                        <label> Product ID </label>
                        <div class="control">
                            <input type="text" class="input" v-model="productID">
                        </div>

                        <label> Product Name </label>
                        <div class="control">
                            <input type="text" class="input" v-model="productName">
                        </div>

                        <label> Price </label>
                        <div class="control">
                            <input type="number" class="input" v-model="price">
                        </div>

                        <label> Image </label>
                        <div class="control">
                            <input type="url" class="input" v-model="image">
                        </div>

                        <label> Brand </label>
                        <div class="control">
                            <input type="text" class="input" v-model="brand">
                        </div>

                        <label> Model </label>
                        <div class="control">
                            <input type="text" class="input" v-model="model">
                        </div>

                        <label> Quantity </label>
                        <div class="control">
                            <input type="number" class="input" v-model="quantity">
                        </div>

                        <label> Discount </label>
                        <div class="control">
                            <input type="number" class="input" v-model="discount">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-info">Update Product</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data() {
        return {
            productID:'',
            productName: '',
            price: '',
            image: '',
            brand: '',
            model: '',
            quantity: '',
            discount: ''
        }
    },
    methods: {
        submitForm() {

                const formData = {
                   productID: this.productID,
                   productName: this.productName,
                   price: this.price,
                   image: this.image,
                   brand: this.brand,
                   model: this.model,
                   quantity: this.quantity,
                   discount: this.discount
                }

                axios
                    .post("http://localhost:5000/update", formData)
                    .then(response => {
                        toast({
                            message: 'Product Updated successfully',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
        }

    }
}

</script>