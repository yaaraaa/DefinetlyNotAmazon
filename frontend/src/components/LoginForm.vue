<template>
  <form @submit.prevent="handleSubmit">
    <h1> HighTech </h1>
    <br>
    <h2> Login </h2>

    <label>Email:</label>
    <input type="email" v-model="email" required>

    <label>Password:</label>
    <input type="password" v-model="password" required>

    <div class="submit">
      <button>Login</button>
    </div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: ""
    }
  },

  methods: {
    handleSubmit() {  
      console.log('Email: ', this.email)
      console.log('Password: ', this.password)

      const path = 'http://localhost:5000/login'
      axios
        .get(path)
        .then(response => {
          this.latestProducts = response.data
          // console.log(response.data)
          console.log(this.latestProducts)
          //this.latestProducts = response.data
          //console.log(this.latestProducts)
        })
        .catch(error => {
          console.log(error)
        })
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