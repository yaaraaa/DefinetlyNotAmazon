<template>
  <form @submit.prevent="handleSubmit">
    <h1> HighTech </h1>
    <br>
    <h2> Create an Account </h2>

    <label>Firstname:</label>
    <input type="text" v-model="firstname" required>

    <label>Lastname:</label>
    <input type="text" v-model="lastname" required>

    <label>Email:</label>
    <input type="email" v-model="email" required>

    <label>Phone Number:</label>
    <input type="number" v-model="phoneNumber" required>

    <label>Password:</label>
    <input type="password" v-model="password" required>

    <label>Password Confirmation:</label>
    <input type="password" v-model="passwordConfirmation" required>

    <label>Date of Birth:</label>
    <input type="date" v-model="dateOfBirth" required>

    <div class="submit">
      <button>Register</button>
    </div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      firstname: "",
      lastname: "",
      email: "",
      phoneNumber: "",
      password: "",
      passwordConfirmation: "",
      dateOfBirth: ""
    }
  },

  methods: {
    handleSubmit() {  
      console.log('Firstname: ', this.firstname)
      console.log('Lastname: ', this.lastname)
      console.log('Email: ', this.email)
      console.log('Phone Number: ', this.phoneNumber)
      console.log('Password: ', this.password)
      console.log('Password Confirmation: ', this.passwordConfirmation)
      console.log('Date of Birth: ', this.dateOfBirth)
    }
  }
}
</script>

<style scoped>
    form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
  }
  label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
  }
  input {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  button {
    background: #0b6dff;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;
  }
  .submit {
    text-align: center;
  }

  h1, h2 {
    text-align: center;
  }
</style>