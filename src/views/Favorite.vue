<template>
    <div>
        <h2>
            Favorite List
        </h2>
        <hr>
        <section class="fav">
            <div v-for="favorite in favorites"
            :key="favorite" class="fav-items">
                <img :src="require(`@/assets/${favorite.image}`)"
                :alt="favorite.name">
                <p>{{ favorite.description }}</p>
                <div>
                    <button class="btn btn-primary">
                        remove
                    </button>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import store from "@/store";
export default {
    data() {
    return {
      favorites: store.favorites
    };
  }
}
</script>


<style scoped>
.fav-items{
    display: flex;
    margin: 0 40px;
    padding-bottom: 20px;
}

.fav-items p{
    padding-top: 20px;
    margin: 0 20px;
    text-align: center;
}

.fav-items img {
    max-height: 300px;
    max-width: 250px;
}

button {
    margin-bottom: 20 0px;
}

</style>
