<template>
    <div class="page-delete-product">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <br>
                <br>
                <br>
                <br>
                <h1 class="title">Delete Product</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>product ID</label>
                        <div class="control">
                            <input type="number" class="input" v-model="productID">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-info">Delete Product</button>
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
    name: 'LogIn',
    data() {
        return {
            email: '',
            password: '',
            idExists: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.error = []

            if (this.productID === '') {
                this.errors.push('the ID is missing')
            }

            if (!this.errors.length) {
                const formData = {
                   productID: this.productID,
                }

                axios
                    .post("http://localhost:5000/delete", formData)
                    .then(response => {
                        this.idExists = response.data.idExists
                        console.log(this.idExists)
                        if (this.idExists.length) {
                            toast({
                                    message: 'Product Deleted successfully',
                                    type: 'is-success',
                                    dismissible: true,
                                    pauseOnHover: true,
                                    duration: 2000,
                                    position: 'bottom-right',
                                })
                        }
                        else{
                            this.errors.push('there are no products with this ID value')
                        }
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
}
</script>
