import { createStore } from 'vuex'

export default createStore({
  state: {
    product: [],
    cart: {
        items: [],
    },
    isAuthenticated: false,
    token: '',
  },
  mutations: {
    initializeStore(state) {
      // checks if local storage is accessed with an item called cart
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } 
      // else creates it
      else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
  addToCart(state, item) {    
    // const exists = state.cart.items.filter(i => i.product.product_id === item.product.product_id)


    // // length is not zero then we know item already exists in cart
    // if (exists.length) {
    //   // increments quantity of already existing item
    //   exists[0].quantity = parseInt(exists[0].quanity) + parseInt(item.quanity)
    // } 
    // // if item not in cart, it is added to cart
    // else {
      state.cart.items.push(item)
    // }
    localStorage.setItem('cart', JSON.stringify(state.cart))
  }
},

  actions: {
  },
  modules: {
  }
})


