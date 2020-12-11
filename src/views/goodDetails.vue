<template>
    <section>
        <h1>goods</h1>
        <h2>{{good.name}}</h2>
        <div class="good-details">
            <img 
            :src="require(`@/assets/${good.image}`)" 
            :alt="good.name">
            <ul>
                <p>{{good.description}}</p>
                <li class="user">User Available:</li>
                <li v-for="name in good.sellers"
                :key="name" class="seller">{{name}}</li>
            </ul>
            
        </div>
        <div>
            <button class="btn btn-primary">
                add to favorite
            </button>
        </div>
    </section>
</template>
<script>
import store from "@/store.js"
export default {
    props: {
        slug: {
            type: String,
            required: true
        },
        goodSlug: {
            type: String,
            required: true
        }
    },
    computed:{
        item() {
            return store.items.find(
                item => item.slug === this.slug
            );
        },
        good() {
            return this.item.goods.find(
                good => good.slug === this.goodSlug
            );
        }
    }
};
</script>

<style scoped>
img {
  max-width: 600px;
  height: auto;
  width: 100%;
  max-height: 400px;
}
.good-details {
  display: flex;
  justify-content: space-between;
}
p {
  color: black;
  margin: 40 0px;
  font-size: 40px;
  text-align: left;
}

.user{
  display: flex;
  font-size: 25px;
  color: black;
  justify-content: space-between;
  text-align: left;
}

.seller {
  display: flex;
  font-size: 20px;
  margin: 0 20px;
  color: grey;
  justify-content: space-between;
  text-align: left;
  text-decoration: underline;
}
</style>