<template>
    <section class="event-details">
        <h3 class="section-title">Event Details</h3>
        <p class="event-description">{{ event.description }}</p>
        <div class="details-grid">
            <div class="detail-item">
                <img class="detail-icon" src="@/assets/icons/calendar.svg" alt="Calendar Icon" height="24" width="24" />
                <div class="detail-content">
                    <p class="detail-label">Reserve Date</p>
                    <p class="detail-value">{{ new Date(event.start_time).toLocaleString() + ' -'}}</p>
                    <p class="detail-value">{{ new Date(event.end_time).toLocaleString() }}</p>
                </div>
            </div>
            <div class="detail-item">
                <img class="detail-icon" src="@/assets/icons/ticket.svg" alt="Ticket Icon" height="24" width="24" />
                <div class="detail-content">
                    <p class="detail-label">Total Tickets</p>
                    <p class="detail-value">{{ event.total_tickets }}</p>
                </div>
            </div>
            <div class="detail-item">
                <img class="detail-icon" src="@/assets/icons/location.svg" alt="Location Icon" height="24" width="24" />
                <div class="detail-content">
                    <p class="detail-label">Venue</p>
                    <p class="detail-value">{{ event.location }}</p>
                </div>
            </div>
        </div>
        <div class="action-container">
            <button class="reserve-btn" @click="handleReserveTicket">
                <svg fill="currentColor" height="20" viewBox="0 0 256 256" width="20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M208,80H176V56a8,8,0,0,0-16,0V80H96V56a8,8,0,0,0-16,0V80H48a16,16,0,0,0-16,16v96a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V96A16,16,0,0,0,208,80ZM208,192H48V96H80v24a8,8,0,0,0,16,0V96h64v24a8,8,0,0,0,16,0V96h32Z">
                    </path>
                </svg>
                <span>Reserve Ticket</span>
            </button>
        </div>
    </section>
</template>

<script>
export default {
    name: 'EventDetails',
    props: {
        event: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
.event-details {
    background-color: #1a222a;
    padding: 1.5rem;
    border-radius: 0.75rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.section-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #dce8f3;
    margin-bottom: 1rem;
}

.event-description {
    color: #b0c7de;
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.details-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.detail-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    background-color: #25303c;
    border-radius: 0.5rem;
}

.detail-icon {
    color: #89a6c5;
    flex-shrink: 0;
}

.detail-content {
    min-width: 0;
}

.detail-label {
    color: #89a6c5;
    font-size: 0.75rem;
    font-weight: 500;
    margin-bottom: 0.25rem;
}

.detail-value {
    color: white;
    font-size: 0.875rem;
    font-weight: 600;
}

.action-container {
	margin-top: 2rem;
	display: flex;
	justify-content: flex-end;
}

.reserve-btn {
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 0.5rem;
	min-width: 150px;
	max-width: 480px;
	cursor: pointer;
	border-radius: 0.75rem;
	height: 3rem;
	padding: 0 1.5rem;
	background-color: #dce8f3;
	color: #141a1f;
	font-size: 1rem;
	font-weight: bold;
	line-height: normal;
	letter-spacing: 0.015em;
	border: none;
	transition: all 0.2s;
	box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.reserve-btn:hover {
	background-color: #c0d6e8;
	box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}


@media (min-width: 640px) {
    .event-details {
        padding: 2rem;
    }

    .details-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
</style>