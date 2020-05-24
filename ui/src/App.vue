<template>
  <div
    class="pantry-bg-body"
    id="app"
  >
    <navbar />
    <router-view class="h-screen" />
  </div>
</template>

<script>
import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: { Navbar },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
}
</style>
