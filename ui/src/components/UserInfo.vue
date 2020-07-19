<template>
  <div class="pantry-bg-yellow2 p-4">
    <div class="h-16 w-16 bg-gray-400 rounded-full mx-auto">
      <p class="text-center text-white text-3xl">{{ profile.username[0] }}</p>
    </div>
    <span class="block text-gray-700 text-center px-4 py-2 text-xl">
      {{ profile.username }}
      <br />
    </span>
    <span class="block text-gray-700 text-center px-4 py-2 text-sm">
      User Since:
      {{ translateDate(profile.date_joined) }}
      <br />
    </span>
    <span class="block text-gray-700 text-center px-4 py-2 text-sm">
      Email: {{ profile.email }}
      <br />
    </span>
  </div>
</template>
<script>
export default {
  name: "UserInfo",
  props: {
    profile: {
      type: Object,
      required: true
    }
  },
  methods: {
    translateDate(date) {
      return new Date(date).toDateString();
    }
  }
};
</script>