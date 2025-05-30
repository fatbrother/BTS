<template>
  <div>
    <HeroSection @open-popup="emit('open-popup')" />
    <EventList />
  </div>
</template>

<script setup>
import HeroSection from '../components/HomeView/HeroSection.vue'
import EventList from '../components/HomeView/EventList.vue'

const emit = defineEmits(['open-popup'])
</script>
