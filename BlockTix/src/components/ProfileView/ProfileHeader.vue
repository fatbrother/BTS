<template>
	<div class="header-container">
		<div class="profile-info">
			<div class="avatar-wrapper">
				<div class="avatar"></div>
				<button class="avatar-button">
					<img src="@/assets/icons/photo.svg" alt="Edit Avatar" class="material-icons" />
				</button>
			</div>
			<div class="user-details">
				<p class="username">{{ user.username }}</p>
				<p class="handle">{{ shortAddress }}</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useWallet } from '@/composables/useWallet';

const { shortAddress } = useWallet();

defineProps({
	user: {
		type: Object,
		required: true,
	},
});

</script>

<style scoped>
.header-container {
	padding: 24px;
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 24px;
}

@media (min-width: 480px) {
	.header-container {
		flex-direction: column;
		align-items: center;
	}
}

.profile-info {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 24px;
}

.avatar-wrapper {
	position: relative;
}

.avatar {
	background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCDTiqwHhEgdtraSBA4Tk_Qj41L1b_QSBH48ERzSRWCCxxQS3E8rxbhkHYhRrjbJpHA2_BpTZVSPpSWhrQWovpAvDht9ZmDOxbhoZROmFdaUMyoJF8Y845qShD9-DNTyGZQ_hr4Gh5ksAdDpdjOpRMgBINgmkwMxSMnCAu7tbSr06RnlTLmNvzXH9-MlzV8tBde1NFBJbJRqjWLPq9IoG0Zg79BUNlVhYKYJbXp-Noff0rIIRj8gLShcIrZcvhQHCueTS4amWorO94");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
	width: 128px;
	height: 128px;
	background-size: cover;
	background-position: center;
	border-radius: 9999px;
	border: 4px solid #dce8f3;
	box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

@media (min-width: 768px) {
	.avatar {
		width: 160px;
		height: 160px;
	}
}

.avatar-button {
	position: absolute;
	bottom: 8px;
	right: 8px;
	width: 40px;
	height: 40px;
	background-color: #dce8f3;
	color: #141a1f;
	border-radius: 9999px;
	display: flex;
	align-items: center;
	justify-content: center;
	border: none;
	cursor: pointer;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	transition: background-color 0.3s ease;
}

@media (min-width: 768px) {
	.avatar-button {
		width: 48px;
		height: 48px;
	}
}

.avatar-button:hover {
	background-color: #ffffff;
}

.material-icons {
	font-size: 20px;
}

@media (min-width: 768px) {
	.material-icons {
		font-size: 24px;
	}
}

.user-details {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}

.username {
	color: #dce8f3;
	font-size: 24px;
	font-weight: 700;
	line-height: 1.2;
}

@media (min-width: 768px) {
	.username {
		font-size: 30px;
	}
}

.handle {
	color: #9daebe;
	font-size: 16px;
	font-weight: 400;
	line-height: 1.5;
}

@media (min-width: 768px) {
	.handle {
		font-size: 18px;
	}
}

.edit-button {
	display: flex;
	align-items: center;
	justify-content: center;
	width: 100%;
	max-width: 280px;
	min-width: 120px;
	height: 48px;
	padding: 0 24px;
	background-color: #dce8f3;
	color: #141a1f;
	font-size: 16px;
	font-weight: 700;
	letter-spacing: 0.015em;
	border-radius: 9999px;
	border: none;
	cursor: pointer;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	transition: background-color 0.3s ease;
}

@media (min-width: 480px) {
	.edit-button {
		width: auto;
	}
}

.edit-button:hover {
	background-color: #ffffff;
}
</style>