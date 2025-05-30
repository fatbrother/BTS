<template>
	<main class="main-container">
		<div class="content-wrapper">
			<EventSearch />
			<div :class="['events-grid', { 'grid-view': view === 'grid', 'list-view': view === 'list' }]">
				<EventCard v-for="event in events" :key="event.title" :event="event" />
			</div>
		</div>
	</main>
</template>

<script setup>
import { ref } from 'vue';
import EventSearch from '../components/EventListView/EventSearch.vue';
import EventCard from '../components/EventListView/EventCard.vue';

const view = ref('grid');
const events = ref([
	{
		title: 'Tech Conference 2024',
		date: 'Jul 15, 2024',
		location: 'San Francisco, CA',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAQDiHA7CjjHbep5RPuRvfYAWGPlvLFAY8kqNU3pI9EsBuUVTLGC-4ELl3D3gRSN7zLFFxy3PoxL8DjmD3hMm9j_4fs6sKxfRQL3-AIT5peqH15fV-rq1pjG9HwHxPT8XbJqPZ1h9hR3nhPlptJ4Nb1IWv2xKykSusockrrz8ogmB3Yvpiv00lRGbRH5UQBiWb79COAnr4k16Sck9yrn8K8b9JuRmkvffiWsSsJP1zsJ3ziE2p6I0z0liXYCh-0qo8d9QOA9ZpdVCA',
	},
	{
		title: 'Summer Music Festival',
		date: 'Aug 5, 2024',
		location: 'Los Angeles, CA',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDIePY8mlM70DZ-kyYKZBmNylftHkhleSlzvL38kT68EPhqwAAAwv11byzsIvRlyCUA4t7lzcCi0CI9tNIxIeAA3aUCMx259oUKUsa2xfsSprxXqOsfwmHTlrOQRFYc7LIzJZ5Ae9P9P03hgWtFURvO0p1s-aO5kp0OnCP4lfOGIfKHtA9kFU72mDZo9sp8MibCXDJTbtsSJWL3n8iQCQUDurIhHtYoZjreWR_TB_96-NTIfFURx-ZSP5OVkQwf4pKzn_O0fy6f41U',
	},
	{
		title: 'Sports Expo',
		date: 'Sep 20, 2024',
		location: 'New York, NY',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuClxr-3EbfqJA-gKA1eMXrAf0wJ5t8ovIksgZ2mBjzuzUGgW0CZW78oXxQVyPAD4eq4lJ59H48QqhBzejVOKSaMdRnGeFYzrAzdkWx7vGM4dnA3wSrv4dFSk_Nt8PLrPQPQm4WI06tmVbOoV_ImVuGB-7R407jamYgaR5vX17OGOarrsbcHouKBrOMr3QSDJWB1-bzccb3aVVcL_rDiiCfWQfnMWr1UEa-K07Qgfmxpk5umgys6N19u2_HDW1FV65GieDpbKGckIh0',
	},
	{
		title: 'Art Exhibition',
		date: 'Oct 10, 2024',
		location: 'Chicago, IL',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAZ7r9HMEms5X7s9UnQS-Hak1EdK5shLPwGY3hb1At8O_7lCS9gunTUx8Axmv1CxIUOJZYdz-fyeYxFc42H1BTBfOE2VtS2TVd2wLk5k5cvzf_Cv6zqy4hPKrgHCbC1CqBxDjSfCw18UAurJ2xLe0kvHsnSmHjSpJPy0KZ5slHKcjpMyefGrydqfWmzNWxA2j4FndaE8ZXUL_TctrytbfGSugxd_laLRQu_9HxMZAWsw_M9vjuzTso5dv2_BJn44mIsA14wxaghEA8',
	},
	{
		title: 'Food & Wine Tasting',
		date: 'Nov 2, 2024',
		location: 'Miami, FL',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC2LkrS6IMldMA-mMYQ-IT6XfuyP_VOrTIIVgtRAojPpUB4wrfpCGxXylkh9h0IkpGzN9vVEubz_hS0iSdAcsL0ZT7kty4O3xqKaJhxrOgkm2_NxzPesZBE-t3V8oJptvVQEkapGSG4lb_ECCaJZzeol55Yv8HmL_mtG4BZhteQMwRhPR96Kd2S45Ckxr5C_VGx7j4_s6QMwr_QX7JS7AUGZYVRDjcLSNPsHdLqBTpCNfevtw8xZyzdh3xrwElp7qMFJ2JvrykZBt4',
	},
	{
		title: 'Business Networking Event',
		date: 'Dec 1, 2024',
		location: 'Austin, TX',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDlRdkmnVnLHb5KWIzLOTQ_Ao2MtYKVG4uWV9FUGbhd4B1GE6_03BOiyDIg5Vub0r3_7s8VNvCpUBAtkNETcHaZaV_QtY2tCoDH95EQxGjVTrI7JIdcKl2PEQTJPtPw_kd5ASH1OdTfmr_h9RXCujzQK0AmrF7X8Kr-BkSTM1B7tv4lGPqOL1ds8UjYgN-PzvCnlCjVVTiRFQXrrNmxXoiRM2ZfSgurRGyaS64v_xL-E3hftxIo7WPaojkw1bf-25FXZdmxWUlq55g',
	},
	{
		title: 'Outdoor Adventure Meetup',
		date: 'Jan 15, 2025',
		location: 'Seattle, WA',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAGxBjJOSOx7SvfbD06kVgM8iqGso-m4atPBKmBlvQV9wRMo39mTXPLY24tyjX5kAeGLomj7r6bwwxCXQAKN9CJXaZrcPhkb7EOykB3hH7wbzdwFOINM6LtEKXKdBnTvoxXKs0uDSvrUSOZqNacTZaRR1DPVFRkjjYmNk6Yn7z1XYNegjs9OELXY-yRxE1VfomZwkbZy8qWo5svNIYMc8Q_5etiBtlE6w7EKzlpVAx0Pmz5EcoOTDUVSZjjQgtwrHLgkmPsc8At4QY',
	},
	{
		title: 'Charity Gala',
		date: 'Feb 28, 2025',
		location: 'Denver, CO',
		image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDDOVcEwjBaVj2Q4e4wc1HD6SaELhgQD5w9tEJjGzFHFluBhnEkiQc8Ztaz8PZIca7IzlyPeIURXP7jcpBRsAp2xqlCCrkHRMf33YwsNyH6eZbVEniNgmQ-Ercz2irBCyekbi_R6orYCDQbgXV9ow09CSxdkkGrq8vGsnLIHUJLXbaeR8VX0hswOfc3WOCVTADjvAh7-nme9yJr9PiqZ5zFzHN61IoQuPMuwcc8Go4eg5xHBxUWbZLhwrssUcPUsZG_sK36GYZZug0',
	},
]);
</script>

<style scoped>
.main-container {
	padding: 32px 16px;
	display: flex;
	justify-content: center;
	flex: 1;
}

@media (min-width: 640px) {
	.main-container {
		padding-left: 32px;
		padding-right: 32px;
	}
}

@media (min-width: 768px) {
	.main-container {
		padding-left: 48px;
		padding-right: 48px;
	}
}

@media (min-width: 1024px) {
	.main-container {
		padding-left: 80px;
		padding-right: 80px;
	}
}

@media (min-width: 1280px) {
	.main-container {
		padding-left: 160px;
		padding-right: 160px;
	}
}

.content-wrapper {
	display: flex;
	flex-direction: column;
	max-width: 1280px;
	width: 100%;
	flex: 1;
}

.events-grid {
	display: grid;
	gap: 24px;
	padding: 16px;
}

.events-grid.grid-view {
	grid-template-columns: repeat(1, 1fr);
}

@media (min-width: 768px) {
	.events-grid.grid-view {
		grid-template-columns: repeat(2, 1fr);
	}
}

@media (min-width: 1024px) {
	.events-grid.grid-view {
		grid-template-columns: repeat(3, 1fr);
	}
}

.events-grid.list-view {
	grid-template-columns: 1fr;
}
</style>