<template>
	<div class="event-card" @click="viewEvent">
		<img :src="image" alt="Event Image" v-if="image" />
		<div class="event-card-content">
			<h3>{{ title }}</h3>
			<p>{{ introduction }}</p>
			<div class="event-time-info">
				<p>Reserve by: {{ new Date(reserveDate).toLocaleDateString() }}</p>
			</div>
		</div>
	</div>
</template>

<script setup>
const props = defineProps({
	id: {
		type: [String, Number],
		required: true
	},
	title: {
		type: String,
		required: true
	},
	introduction: {
		type: String,
		default: ''
	},
	image: {
		type: String,
		default: ''
	},
	reserveDate: {
		type: Number,
		default: () => Date.now()
	}
});
import { useRouter } from 'vue-router';
const router = useRouter();
function viewEvent() {
	router.push({ name: 'event', params: { id: props.id } });
}

</script>

<style scoped>
.event-card {
	display: flex;
	flex-direction: column;
	background-color: #1a2633;
	border-radius: 12px;
	overflow: hidden;
	min-width: 300px;
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	transition: box-shadow 0.3s ease;
}

.event-card:hover {
	box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
	cursor: pointer;
}

.event-card img {
	width: 100%;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	height: 200px; /* Adjust height as needed */
}

.event-card-content {
	padding: 1.25rem;
	display: flex;
	flex-direction: column;
	flex-grow: 1;
}

.event-card h3 {
	color: #ffffff;
	font-size: 1.125rem;
	font-weight: 600;
	line-height: 1.5;
	margin-bottom: 0.25rem;
}

.event-card p {
	color: #90adcb;
	font-size: 0.875rem;
	font-weight: 400;
	line-height: 1.5;
	margin-bottom: 0.75rem;
}

.event-time-info {
	margin-top: auto;
	padding-top: 0.5rem;
	border-top: 1px solid #223649;
}
</style>
