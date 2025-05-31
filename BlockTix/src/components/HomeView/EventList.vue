<template>
	<section class="events">
		<div class="events-header">
			<h1>Upcoming Events</h1>
			<RouterLink to="/events" class="view-all">
				View All
			</RouterLink>
		</div>
		<div class="event-list">
			<EventCard v-for="event in events"
				:key="event.id"
				:event="event"
			/>
		</div>
	</section>
</template>

<script setup>
import EventCard from './EventCard.vue'
import { ref, onMounted } from 'vue'
import { getAllEvents } from '@/api'

const events = ref([])
async function fetchEvents() {
	try {
		const response = await getAllEvents();
		events.value = response.data;
	} catch (error) {
		console.error('Error fetching events:', error);
	}
}

onMounted(() => {
	fetchEvents();
});
</script>

<style scoped>
.events {
	padding: 2rem 0;
}

.events-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.view-all {
	color: #4a90e2;
	text-decoration: none;
	font-weight: bold;
}

.event-list {
	display: flex;
	gap: 1.5rem;
	margin-top: 1rem;
	overflow-x: auto;
	scrollbar-color: #c0d4e6 transparent;
	scrollbar-width: thin;
}
</style>
