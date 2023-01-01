<template>
  <div id="wrapper">
    <nav class="navbar is-light">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>HighTech</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="what are you looking for?" name="query">
                </div>
                
                <div class="control">
                  <button class="button is-info">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>

              </div>
            </form>
            
          </div>
        </div>

        <div class="navbar-end">
           <!-- <router-link to="/item1" class="navbar-item">item1</router-link>
           <router-link to="/item2" class="navbar-item">item2</router-link> -->

           <div class="navbar-item ">
            <div class="buttons">
              <router-link to="/log-in" class="button is-dark">Login</router-link>
              <router-link to="/cart" class="button is-info">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
           </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>
    
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  // initialize store
  beforeCreate() {
    // commit is used to call the mutations in the store
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }

}

</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
