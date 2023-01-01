<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">

                        <label> FirstName </label>
                        <div class="control">
                            <input type="text" class="input" v-model="firstname">
                        </div>

                        <label> LastName </label>
                        <div class="control">
                            <input type="text" class="input" v-model="lastname">
                        </div>

                        <label> Email </label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>

                        <label> Password </label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>

                        <label> Password Confirmation </label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>

                        <label> Birth Date </label>
                        <div class="control">
                            <input type="date" class="input" v-model="birthdate">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error"> {{ error }} </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-info">Sign Up</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/log-in">click here</router-link> to log in!
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
            firstname: '',
            lastname: '',
            email: '',
            password: '',
            password2: '',
            birthdate: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.error = []

            if (this.firstname === '') {
                this.errors.push('the first name is missing')
            }
            if (this.lastname === '') {
                this.errors.push('the last name is missing')
            }
            if (this.email === '') {
                this.errors.push('the email is missing')
            }
            if (this.password === '') {
                this.errors.push('password is too short')
            }
            if (this.password != this.password2) {
                this.errors.push('passwords do not match')
            }
            if (this.birthdate === '') {
                this.errors.push('birth date is missing')
            }

            if (!this.errors.length) {
                const formData = {
                   firstname: this.firstname,
                   lastname: this.lastname,
                   email: this.email,
                   password: this.password,
                   birthdate: this.birthdate 
                }

                axios
                    .post("http://localhost:5000/register", formData)
                    .then(response => {
                        toast({
                            message: 'Account created, please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/log-in')
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