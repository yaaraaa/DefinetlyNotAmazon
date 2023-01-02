<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-info">Log in</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/sign-up">click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            email: '',
            password: '',
            status: '',
            errors: []
        }
    },
    mounted() {
        document.title ='Login | HighTech'
    },
    methods: {
        submitForm() {
            this.error = []

            if (this.email === '') {
                this.errors.push('the email is missing')
            }
            if (this.password === '') {
                this.errors.push('the password is missing')
            }

            if (!this.errors.length) {
                const formData = {
                   email: this.email,
                   password: this.password, 
                }

                axios
                    .post("http://localhost:5000/login", formData)
                    .then(response => {
                        this.status = response.data.status
                        console.log(response.data)
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

                if (this.status === 1) {
                    toast({
                            message: 'successfully logged in',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/home')
                }
                else {
                    this.errors.push('incorrect login information')
                }
                

            }
        }
    }
}
</script>
