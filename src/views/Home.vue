<template>
  <div class="home">
    <h1>
      All Items
    </h1>
    <div>
      <input type="text" placeholder="Search an item"/>
      <button class="btn btn-primary">
        <router-link :to="{ name: 'notFound' }">Go</router-link>
        </button>
      </div>
    <div class="items">
      <div v-for="item in items"
      :key="item.name">
        <router-link :to="{ name: 'ItemDetails', params: { slug: item.slug } }">
          <h2>{{item.name}}</h2>
        </router-link>
        <figure>
          <router-link :to ="{ name: 'ItemDetails', params: { slug: item.slug } }">
            <img :src="require(`@/assets/${item.image}`)"
            :alt="item.name">
          </router-link>
        </figure>
      </div>
    </div>
    <footer>
      <p>Author: XXX<br>
    <a href="https://rpi.edu">rpi.edu</a></p>
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
import store from "@/store.js";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      items: store.items
    };
  }
};
</script>
<style scoped>
.home {
  max-width: 1400px;
  margin: 0 auto;
}
img {
  max-width: 200px;
}
.items{
  display: flex;
  justify-content: space-between;
}
footer {
  background: lightcoral;
}
</style>