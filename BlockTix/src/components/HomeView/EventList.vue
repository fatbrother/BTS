<template>
	<section class="events">
		<div class="events-header">
			<h1>Upcoming Events</h1>
			<a href="#" class="view-all">View All</a>
		</div>
		<div class="event-list">
			<EventCard v-for="event in events"
				:key="event.id"
				:id="event.id"
				:title="event.title"
				:image="event.image"
				:reserveDate="event.reserveDate"
			/>
		</div>
	</section>
</template>

<script setup>
import EventCard from './EventCard.vue'

const events = [
	{
		id: 1,
		title: 'Indie Rock Fest',
		image: '@/assets/event1.png',
		reserveDate: 'July 15th'
	},
	{
		id: 2,
		title: 'Summer Beats Festival',
		image: '@/assets/event2.png',
		reserveDate: 'August 1st'
	},
	{
		id: 3,
		title: "Broadway's Newest Hit",
		image: '@/assets/event3.png',
		reserveDate: 'September 10th'
	},
	{
		id: 4,
		title: 'Tech Innovations Expo',
		image: '@/assets/event4.png',
		reserveDate: 'October 5th'
	},
	{
		id: 5,
		title: 'Culinary Delights Gala',
		image: '@/assets/event5.png',
		reserveDate: 'November 20th'
	}
]
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
