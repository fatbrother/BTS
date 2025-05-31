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
import { ref, onMounted } from 'vue'
import { getEventById } from '@/api'
import EventHero from '../components/EventView/EventHero.vue'
import EventDetails from '../components/EventView/EventDetails.vue'

const props = defineProps({
    id: {
        type: [String, Number],
        required: true
    }
})

const eventData = ref({
    name: '',
    image_url: '',
    introduction: '',
    start_time: '',
    end_time: '',
    location: '',
})

async function fetchEvent() {
    try {
        const response = await getEventById(props.id)
        eventData.value = response.data
    } catch (error) {
        console.error('Error fetching event:', error)
    }
}
onMounted(() => {
    fetchEvent()
})
</script>

<style>
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