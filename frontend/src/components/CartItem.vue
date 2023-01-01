<template>
    <tr>
        <td><router-link v-bind:to="{path:'/'+item.product.product_id, params:{'id':product.product_id}}">{{ item.product.name }}</router-link></td>
        <td>${{ item.product.price }}</td>
        <td>
            {{ item.quantity }}
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete"></button></td> --> -->
        <td><router-link :to="item.product"></router-link></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    }, 
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        }
    }
}
</script>