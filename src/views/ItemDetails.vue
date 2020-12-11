<template>
  <div>
    <GoBack />
    <section class="item">
      <h1>{{item.name}}</h1>
        <div class="item-details">
            <img :src="require(`@/assets/${item.image}`)"
            :alt="item.name">
            <p>{{ item.description }}</p>
        </div>
    </section>
    <div>
      <input type="text" placeholder="Search an item"/>
      <button class="btn btn-primary">
        <router-link :to="{ name: 'notFound' }">Go</router-link>
        </button>
      </div>
    <section class="goods">
      <h2>Top items in {{item.name}} </h2>
      <div class="cards">
        <div v-for="good in item.goods"
          :key="good.slug"
          class="card">
          <router-link
            :to="{
                name: 'goodDetails',
                params: {goodSlug: good.slug}
            }"
          >
            <img 
            :src="require(`@/assets/${good.image}`)" 
            :alt="good.name">
            <span class="card__text">
                {{good.name}}
            </span>
          </router-link>
        </div>
      </div>
      <router-view :key="$route.path" />
    </section>
  </div>
</template>
<script>
import store from "@/store";
import GoBack from "@/components/GoBack";
export default {
    components:{
        GoBack
    },
    data(){
        return{};
    },
    props:{
        slug:{
            type: String,
            required: true
        }
    },
    computed: {
        item() {
            return store.items.find(
                item => item.slug === this.slug
            )
        }
    }
}
</script>
<style scoped>
img {
    max-width: 600px;
    height: auto;
    width: 100%;
    max-height: 400px;
}
.item-details {
    display: flex;
    justify-content: space-between;
}
p {
    margin: 0 40px;
    font-size: 20px;
    text-align: left;
}

.cards {
    display: flex;
}

.cards img {
    max-height: 300px;
    max-width: 250px;
}

.card {
    padding: 0 100px;
    position: relative;
}

.card__text {
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 25px;
    font-weight: bold;
    text-decoration: none;
}
</style>