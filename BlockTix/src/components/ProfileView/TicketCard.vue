<template>
  <div class="ticket-card">
    <div class="ticket-image" :style="{ backgroundImage: `url(${ticket.image})` }"></div>
    <div class="ticket-details">
      <p class="ticket-title">{{ ticket.title }}</p>
      <p class="ticket-info">{{ ticket.type === 'nft' ? ticket.edition : ticket.details }}</p>
    </div>
    <button class="action-button">
      {{ ticket.type === 'nft' ? 'View Details' : 'Manage Ticket' }}
    </button>
  </div>
</template>

<script setup>
defineProps({
  ticket: {
    type: Object,
    required: true,
    validator: (ticket) => {
      return (
        'title' in ticket &&
        'image' in ticket &&
        ('edition' in ticket || 'details' in ticket)
      );
    },
  },
  type: {
    type: String,
    required: true,
    validator: (type) => ['nft', 'reserved'].includes(type),
  },
});
</script>

<style scoped>
.ticket-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-bottom: 16px;
  background-color: #1e2730;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: all 0.3s ease;
}

.ticket-card:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
  transform: scale(1.05);
}

.ticket-image {
  width: 100%;
  aspect-ratio: 1 / 1;
  background-size: cover;
  background-position: center;
}

.ticket-details {
  padding: 0 16px;
}

.ticket-title {
  color: #dce8f3;
  font-size: 18px;
  font-weight: 600;
  line-height: 1.5;
}

.ticket-info {
  color: #9daebe;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
}

.action-button {
  margin: 0 16px 8px;
  padding: 8px 16px;
  background-color: #dce8f3;
  color: #141a1f;
  font-size: 14px;
  font-weight: 500;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.action-button:hover {
  background-color: #ffffff;
}
</style>