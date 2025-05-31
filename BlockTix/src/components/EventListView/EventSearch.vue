<template>
	<div class="search-container">
		<label class="search-label">
			<div class="search-input-wrapper">
				<img class="search-icon" src="@/assets/icons/search.svg" alt="Search Icon" />
				<input
					type="text"
					class="search-input"
					placeholder="Search events by name or keywords"
					:value="searchQuery"
					@keyup="handleKeyUp"
				/>
			</div>
		</label>
	</div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

defineProps({
	searchQuery: {
		type: String,
		default: ''
	}
});

const emit = defineEmits(['update:searchQuery']);

function handleKeyUp(event) {
	if (event.key === 'Enter') {
		emit('update:searchQuery', event.target.value);
		event.target.blur();
	}
}

</script>

<style scoped>
.search-container {
	padding: 12px 16px;
	margin-bottom: 24px;
}

.search-label {
	display: flex;
	flex-direction: column;
	min-width: 160px;
	width: 100%;
	height: 48px;
}

.search-input-wrapper {
	display: flex;
	align-items: center;
	background-color: #1e293b;
	border-radius: 12px;
	height: 100%;
	transition: all 0.2s ease;
}

.search-input-wrapper:focus-within {
	outline: 2px solid #3b82f6;
	outline-offset: 2px;
}

.search-icon {
	padding-left: 16px;
	height: 36px;
	width: 36px;
}

.search-input {
	flex: 1;
	background-color: #1e293b;
	border: none;
	border-radius: 12px;
	color: #e2e8f0;
	font-size: 16px;
	padding: 0 16px;
	height: 100%;
	outline: none;
}

.search-input::placeholder {
	color: #94a3b8;
}
</style>