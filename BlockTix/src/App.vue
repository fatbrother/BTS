<template>
	<AppHeader @open-popup="openPopup" />
	<transition name="fade" mode="out-in">
		<RouterView @open-popup="openPopup" />
	</transition>
	<div v-if="isPopupOpen" class="modal-overlay" @click.self="closePopup">
		<IdentityVerification @close="closePopup" />
	</div>
	<footer class="footer">
		<p class="footer-text">© 2024 BlockTix. All rights reserved. Powered by Web3.</p>
	</footer>
</template>

<script setup>
import { ref } from 'vue';
import AppHeader from './components/AppHeader.vue';
import IdentityVerification from './components/IdentityVerification.vue';
import { useWallet } from './composables/useWallet';

const {
	disconnectWallet,
} = useWallet()


const isPopupOpen = ref(false);

function openPopup() {
	isPopupOpen.value = true;
}

function closePopup() {
	isPopupOpen.value = false;


	const token = localStorage.getItem('token');
	if (!token) {
		disconnectWallet();
	}
}
</script>

<style scoped>
.modal-overlay {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 1000;
}

.footer {
	padding: 16px;
	text-align: center;
}

.footer-text {
	color: #64748b;
	font-size: 14px;
}
</style>