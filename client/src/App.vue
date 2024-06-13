<template>
  
  <div class="nav-container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">A Website</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <RouterLink class="nav-item nav-link active" to="/">Ping <span class="sr-only">(current)</span></RouterLink>
                    <RouterLink class="nav-item nav-link" to="/books">Books</RouterLink>
                    <a class="nav-item nav-link" href="#">Pricing</a>
                    <a class="nav-item nav-link disabled" href="#">Disabled</a>
                </div>
            </div>
        </nav>
    </div>
    <RouterView />
</template>

<script lang="ts">
import { RouterView } from 'vue-router'
</script>

<style>
#app {
  margin-top: 60px;
}
.nav-container {
  margin: 0 0 2vw 5vw;
}
</style>
