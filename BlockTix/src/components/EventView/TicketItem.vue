<template>
	<div :class="['ticket-item', { selected: selected }]">
		<div class="ticket-info">
			<p class="ticket-name">{{ ticket.name }}</p>
			<p class="ticket-description">{{ ticket.description }}</p>
		</div>
		<p class="ticket-price">${{ ticket.price }}</p>
	</div>
</template>

<script setup>
const props = defineProps({
    ticket: {
        type: Object,
        required: true
    },
    selected: {
        type: Boolean,
        default: false
    }
})
</script>

<style scoped>
.ticket-item {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 1rem;
	background-color: #25303c;
	border-radius: 0.5rem;
	transition: background-color 0.2s;
	cursor: pointer;
}

.ticket-item.selected {
    background-color: #3a4755;
}

.ticket-item:hover {
	background-color: #2b3640;
}

.selected {
    background-color: #3a4755;
}

.ticket-info {
	flex: 1;
	min-width: 0;
}

.ticket-name {
	color: white;
	font-size: 1rem;
	font-weight: 600;
	margin-bottom: 0.25rem;
}

.ticket-description {
	color: #89a6c5;
	font-size: 0.75rem;
	line-height: 1.4;
}

.ticket-price {
	color: #dce8f3;
	font-size: 1.125rem;
	font-weight: bold;
	flex-shrink: 0;
}
</style>