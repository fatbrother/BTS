<template>
    <header class="header">
        <div class="header-brand">
            <div class="logo-icon">
                <svg fill="none" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
                    <path clip-rule="evenodd" d="M24 4H42V17.3333V30.6667H24V44H6V30.6667V17.3333H24V4Z"
                        fill="currentColor" fill-rule="evenodd"></path>
                </svg>
            </div>
            <h1 class="brand-title">BlockTix</h1>
        </div>
        <nav class="navigation">
            <RouterLink to="/" class="nav-link">Home</RouterLink>
            <RouterLink to="/events" class="nav-link">Discover Events</RouterLink>
            <RouterLink to="/profile" class="nav-link">User Profile</RouterLink>
        </nav>
        <div class="header-actions">
            <button v-if="!isConnected" @click="onConnectButtonClick" class="connect-button">
                Connect Wallet
            </button>
            <div v-else class="user-avatar"></div>
        </div>
    </header>
</template>

<script setup>
import { useWallet } from '@/composables/useWallet'
import { RouterLink } from 'vue-router'

const emit = defineEmits(['open-popup'])

const {
    isConnected,
    connectWallet
} = useWallet()

function onConnectButtonClick() {
	connectWallet()

	emit('open-popup')
}

</script>

<style scoped>
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    white-space: nowrap;
    border-bottom: 1px solid #2b3640;
    padding: 1rem 1.5rem;
    margin-bottom: 1rem;
}

.header-brand {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.logo-icon {
    width: 1.5rem;
    height: 1.5rem;
    color: #dce8f3;
}

.brand-title {
    color: #dce8f3;
    font-size: 1.25rem;
    font-weight: bold;
    line-height: 1.2;
    letter-spacing: -0.015em;
    user-select: none;
}

.navigation {
    display: none;
    align-items: center;
    gap: 2rem;
}

.nav-link {
    color: #dce8f3;
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    line-height: normal;
    transition: color 0.2s;
}

.nav-link:hover {
    color: white;
}

.header-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.connect-button {
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    border-radius: 0.5rem;
    height: 2.5rem;
    background-color: #2b3640;
    color: #dce8f3;
    gap: 0.5rem;
    font-size: 0.875rem;
    font-weight: bold;
    line-height: normal;
    letter-spacing: 0.015em;
    min-width: 0;
    padding: 0 0.75rem;
    border: none;
    transition: background-color 0.2s;
}

.connect-button:hover {
    background-color: #354350;
}

.user-avatar {
    background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCDTiqwHhEgdtraSBA4Tk_Qj41L1b_QSBH48ERzSRWCCxxQS3E8rxbhkHYhRrjbJpHA2_BpTZVSPpSWhrQWovpAvDht9ZmDOxbhoZROmFdaUMyoJF8Y845qShD9-DNTyGZQ_hr4Gh5ksAdDpdjOpRMgBINgmkwMxSMnCAu7tbSr06RnlTLmNvzXH9-MlzV8tBde1NFBJbJRqjWLPq9IoG0Zg79BUNlVhYKYJbXp-Noff0rIIRj8gLShcIrZcvhQHCueTS4amWorO94");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 50%;
    width: 2.5rem;
    height: 2.5rem;
    border: 2px solid #2b3640;
    transition: border-color 0.2s;
    cursor: pointer;
}

.user-avatar:hover {
    border-color: #dce8f3;
}

@media (min-width: 768px) {
    .navigation {
        display: flex;
    }

    .header {
        padding: 1rem 2.5rem;
    }

    .lang-text {
        display: inline;
    }
}
</style>