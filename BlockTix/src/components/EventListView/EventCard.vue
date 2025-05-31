<template>
  <div class="event-card">
    <div class="image-container">
      <img :src="event.image_url" :alt="event.name" class="event-image" />
      <button class="bookmark-button">
        <img src="@/assets/icons/bookmark.svg" alt="BookMark Icon" height="24" width="24" />
      </button>
    </div>
    <div class="event-details">
      <p class="event-title">{{ event.name }}</p>
      <p class="event-info">{{ new Date(event.start_time).toLocaleString() }}</p>
      <p class="event-info">{{ event.location }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  event: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.event-card {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding-bottom: 12px;
  background-color: #1e293b;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.event-card:hover {
  box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
}

.image-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.event-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.event-card:hover .event-image {
  transform: scale(1.05);
}

.bookmark-button {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  background-color: rgba(0, 0, 0, 0.5);
  color: #ffffff;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.bookmark-button:hover {
  background-color: #3b82f6;
}

.bookmark-icon {
  font-size: 18px;
}

.event-details {
  padding: 0 16px;
}

.event-title {
  color: #ffffff;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 4px;
}

.event-info {
  color: #94a3b8;
  font-size: 14px;
  font-weight: 400;
}
</style>