<template>
    <nav id="nav">
      <p class="logo">Rensselaer Trade Platform</p>
      <ul class="nav-links">
        <li class="links">
          <router-link to="/home">
            Home
          </router-link>
        </li>
        <li class="links">
          <router-link to="/user-account">
            Account
          </router-link>
        </li>
        <li class="links">
          <router-link to="/favorite">
            Favorite
          </router-link>
        </li>
        <li class="links">
          <router-link to="/transaction">
            Transaction
          </router-link>
        </li>
        <li class='img'>
          <a href="https://rpi.edu/">
            <img src="../assets/rpi.png" alt="Rensselaer logo">
          </a>
        </li>
      </ul>
    </nav>
</template>

<script>
import store from "@/store";
export default {
  data() {
    return {
      itemId: this.$route.params.id,
      items: store.items
    };
  }
};
</script>


<style scoped>
#nav {
    padding: 20px;
    display: flex;
    background-color:white;
}

#nav a {
  font-weight: bold;
  color: rgb(226, 163, 26);
  text-decoration: none;
  padding: 0 40px
}

#nav a.router-link-exact-active {
  color: hsl(0, 100%, 50%);
}

.nav-links {
  display: flex;
}

.links {
  padding-right: 0px;
  list-style: none;
}

.img {
  list-style: none;
  max-height: 100px;
  max-width: 100px;
}

.links:hover {
  text-decoration: underline;
}

.logo {
  font-size: 20px;
  color: #ab26ab;
  font-weight: bold;
}
</style>