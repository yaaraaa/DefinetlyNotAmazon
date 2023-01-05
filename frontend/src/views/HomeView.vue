<template>
 <div class="column is multiline is-centered">
    <br>
    <br>
    <br>
    <center><p class="title mb-6">Seller Panel</p></center>
    <br>
    <center><router-link v-bind:to="{path: '/add-Product'}" class="button is-info is-large is-rounded">Add Product</router-link></center>
    <br>
    <center><router-link v-bind:to="{path: '/update-Product'}" class="button is-info is-large is-rounded">Update Product</router-link></center>
    <br>
    <center><router-link v-bind:to="{path: '/delete-Product'}" class="button is-info is-large is-rounded">delete Product</router-link></center>
    <br>
    <center><router-link v-bind:to="{path: '/view-Products'}" class="button is-info is-large is-rounded">View Products</router-link></center>
 </div>
</template>