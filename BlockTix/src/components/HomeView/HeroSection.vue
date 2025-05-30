<template>
	<section class="hero">
		<div class="hero-content">
			<h1 class="welcome-text">Secure Your Spot with BlockTix</h1>
			<p class="info-text">Experience the future of ticketing with blockchain technology. Say goodbye to scalpers and hello to fair pricing and secure transactions.</p>
			<button v-if="!isConnected" @click="onConnectButtonClick">
				Connect Wallet To Get Started
			</button>
			<p v-else class="info-text">Connected Wallet: {{ shortAddress }}</p>
		</div>
	</section>
</template>

<script setup>
import { useWallet } from '@/composables/useWallet'

const emit = defineEmits(['open-popup'])

const {
	isConnected,
	shortAddress,
	connectWallet
} = useWallet()

function onConnectButtonClick() {
	connectWallet()

	emit('open-popup')
}

</script>

<style scoped>
.hero {
	padding: 4rem 2rem;
	text-align: center;
	border-radius: 12px;
	background: linear-gradient(135deg, rgba(30, 30, 30, 0.356), rgba(29, 35, 44, 0.669)), url('@/assets/concert.jpg') center/cover no-repeat;
	min-height: 50vh;
}

.welcome-text {
	color: #fff;
	font-size: 2.5rem;
	margin-bottom: 1rem;
	font-weight: 700;
}

.welcome-text::after {
	content: '';
	display: block;
	width: 350px;
	height: 2px;
	background: #d2e2f3;
	margin: 1rem auto;
	border-radius: 2px;
}

.info-text {
	color: #d2e2f3;
	font-size: 1.2rem;
	margin-bottom: 2rem;
}

.hero-content {
	max-width: 800px;
	margin: 0 auto;
	padding: 2rem;
	background: rgba(255, 255, 255, 0.1);
	border-radius: 12px;
	box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

button {
	background: #d2e2f3;
	padding: 0.8rem 1.6rem;
	border-radius: 8px;
	border: none;
}

button:hover {
	background: #c0d4e6;
	cursor: pointer;
}
</style>
