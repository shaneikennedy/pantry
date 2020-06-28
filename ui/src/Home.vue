<template>
  <div class="TagLine BackgroundImage pt-48">
    <h1 class="text-6xl text-center pantry-text-brown mb-8">
      Be your own personal chef
    </h1>
    <router-link
      class="flex items-center button-center pantry-bg-yellow pantry-text-brown font-bold text-2xl py-4 px-8 rounded focus:outline-none focus:shadow-outline mx-auto"
      :to="{ name: 'register' }"
      tag="button"
    >
      Get Started
    </router-link>
  </div>
</template>

<style scoped>
.TagLine {
  font-family: "Rubik", sans-serif;
}

.BackgroundImage {
  background-image: url(assets/pantry-background-2.png);
  background-position: top;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
