<template>
	<main class="main-container">
		<div class="content-wrapper">
			<EventSearch
				v-model:searchQuery="searchQuery"
				@update:searchQuery="searchQuery = $event"
			/>
			<div :class="['events-grid', { 'grid-view': view === 'grid', 'list-view': view === 'list' }]">
				<EventCard v-for="event in events"
					:key="event.title"
					:event="event"
					@click="onEventCardClick(event)"
				/>
			</div>
		</div>
	</main>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import EventSearch from '../components/EventListView/EventSearch.vue';
import EventCard from '../components/EventListView/EventCard.vue';
import { getAllEvents } from '@/api';
import { useRouter } from 'vue-router';
const router = useRouter();

const view = ref('grid');

const events = ref([]);
const searchQuery = ref('');

watch(searchQuery, (newQuery) => {
	// Filter events based on search query
	if (newQuery) {
		events.value = events.value.filter(event => event.name.toLowerCase().includes(newQuery.toLowerCase()));
	} else {
		fetchEvents(); // Reset to all events if search query is empty
	}
});

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

function onEventCardClick(event) {
	router.push({ name: 'event', params: { id: event.id } });
}

</script>

<style scoped>
.main-container {
	padding: 32px 16px;
	display: flex;
	justify-content: center;
	flex: 1;
}

@media (min-width: 640px) {
	.main-container {
		padding-left: 32px;
		padding-right: 32px;
	}
}

@media (min-width: 768px) {
	.main-container {
		padding-left: 48px;
		padding-right: 48px;
	}
}

@media (min-width: 1024px) {
	.main-container {
		padding-left: 80px;
		padding-right: 80px;
	}
}

@media (min-width: 1280px) {
	.main-container {
		padding-left: 160px;
		padding-right: 160px;
	}
}

.content-wrapper {
	display: flex;
	flex-direction: column;
	max-width: 1280px;
	width: 100%;
	flex: 1;
}

.events-grid {
	display: grid;
	gap: 24px;
	padding: 16px;
}

.events-grid.grid-view {
	grid-template-columns: repeat(1, 1fr);
}

@media (min-width: 768px) {
	.events-grid.grid-view {
		grid-template-columns: repeat(2, 1fr);
	}
}

@media (min-width: 1024px) {
	.events-grid.grid-view {
		grid-template-columns: repeat(3, 1fr);
	}
}

.events-grid.list-view {
	grid-template-columns: 1fr;
}
</style>