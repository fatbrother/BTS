<template>
  <div class="hero">
    <div class="hero-image" :style="{ backgroundImage: `url('${event.heroImage}')` }"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <h2 class="hero-title">{{ event.title }}</h2>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
    event: {
        type: Object,
        required: true
    }
})
</script>

<style scoped>
.hero {
  position: relative;
  width: 100%;
  height: 16rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.hero-image {
  position: absolute;
  inset: 0;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(20, 26, 31, 0.8) 0%, rgba(20, 26, 31, 0) 100%);
}

.hero-content {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1.5rem;
  color: white;
}

.hero-title {
  font-size: 1.875rem;
  font-weight: bold;
  line-height: 1.2;
  letter-spacing: -0.025em;
}

@media (min-width: 640px) {
  .hero {
    height: 20rem;
  }

  .hero-content {
    padding: 2rem;
  }

  .hero-title {
    font-size: 2.25rem;
  }
}

@media (min-width: 768px) {
  .hero {
    height: 24rem;
  }
}
</style>