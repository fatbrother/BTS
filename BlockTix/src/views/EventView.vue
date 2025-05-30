<template>
    <div class="app-container">
        <main class="main-content">
            <div class="content-container">
                <EventHero :event="eventData" />
                <EventDetails :event="eventData" />
            </div>
        </main>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import EventHero from '../components/EventView/EventHero.vue'
import EventDetails from '../components/EventView/EventDetails.vue'

const props = defineProps({
    eventId: {
        type: [String, Number],
        required: true
    }
})

const eventData = ref({
    title: 'Tech Innovators Summit 2024',
    heroImage: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBGpBPbHpx4ot0kg5IvSk8sjRgU_6Ae2cr_ZgkSq2ZmI0lkb2AAPpADLbX2cyFkIpLSWaWV_WAQ-0_e-DCAk2aa5QIp1WERx646V21KybCccloDvvsPVZ0ldeWTpCIcozNiO3BqFLIBPvxLDnhYIQif4XNWWiXezEIepwH_-FxxMiG8FZTHoJjBBlfKHoaxlR-NZN84asJqL5sEqu-8zJpwfEiZBn7QwcwyxGvTZ19t2zzwDn0IOt5gGqloFHOjR25pi9mHhhk6sRs',
    description: 'Join us for an immersive experience at the forefront of technological innovation. This summit brings together industry leaders, visionaries, and enthusiasts to explore the latest trends, challenges, and opportunities shaping our digital future.',
    date: 'October 26, 2024',
    time: '9:00 AM - 6:00 PM',
    venue: 'Innovation Hub, San Francisco',
    tickets: [
        {
            id: 1,
            name: 'General Admission',
            description: 'Standard access to all talks and networking areas.',
            price: 299
        },
        {
            id: 2,
            name: 'VIP Pass',
            description: 'Includes reserved seating, VIP lounge access, and exclusive merch.',
            price: 499
        },
        {
            id: 3,
            name: 'Student Discount',
            description: 'Valid student ID required. Access to all general sessions.',
            price: 199
        }
    ]
})
</script>

<style>
/* Global styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Manrope', 'Noto Sans', sans-serif;
    background-color: #141a1f;
    color: white;
    min-height: 100vh;
}

.app-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.main-content {
    flex: 1;
    display: flex;
    justify-content: center;
    padding: 2rem 1rem;
}

.content-container {
    display: flex;
    flex-direction: column;
    max-width: 64rem;
    width: 100%;
    gap: 2rem;
}

@media (min-width: 640px) {
    .main-content {
        padding: 2rem 1.5rem;
    }
}

@media (min-width: 1024px) {
    .main-content {
        padding: 2rem 2rem;
    }
}
</style>