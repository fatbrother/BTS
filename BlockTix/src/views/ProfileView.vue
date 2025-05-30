<template>
  <main class="main-container">
    <div class="content-wrapper">
      <ProfileHeader />
      <ProfileTabs v-model:active-tab="activeTab" />
      <section v-if="activeTab === 'collected'" class="section">
        <h2 class="section-title">Owned NFT Tickets</h2>
        <div class="ticket-grid">
          <TicketCard
            v-for="ticket in nftTickets"
            :key="ticket.title"
            :ticket="ticket"
            type="nft"
          />
        </div>
      </section>
      <section v-if="activeTab === 'reserved'" class="section">
        <h2 class="section-title">Reserved Tickets</h2>
        <div class="ticket-grid">
          <TicketCard
            v-for="ticket in reservedTickets"
            :key="ticket.title"
            :ticket="ticket"
            type="reserved"
          />
        </div>
      </section>
      <!-- Placeholder for other tabs -->
      <section v-if="activeTab === 'history'" class="section">
        <h2 class="section-title">Settings</h2>
        <p class="section-placeholder">Settings page coming soon.</p>
      </section>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import ProfileHeader from '../components/ProfileView/ProfileHeader.vue';
import ProfileTabs from '../components/ProfileView/ProfileTabs.vue';
import TicketCard from '../components/ProfileView/TicketCard.vue';

const activeTab = ref('collected');

const nftTickets = ref([
  {
    title: 'NFT Ticket: The Stellar Symphony',
    edition: '1 of 1',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAZ6GOf9QV17r1mOn6Ex9W85ivVoX7Zooc7EvYE71ozKjQDnQ1TIsIxVDaOQKo95ENBIbJrA_0pVSrXj3YZQkvpBxvEB1chk5Q0vyGSAJayOhR_1hxcHYCZn388rvNUWvMW5L9baYYgUuM5tmEnFSsakg3IUEzjUBLvj-mMWX9hl_LeOQMxRyYODOw55EqcTN8fHySutoalz_K7RUpTUpFVgGHlUxrGsxZWLEj4n42mUfuBDOUe9Ehcuw7esoMcoz-cWHcKQhBlnc4',
  },
  {
    title: 'NFT Ticket: The Galactic Groove',
    edition: '1 of 1',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC7B4gUAtZwD1Pu34FqSW4DDQ8HNIlc_1MtKruKI7Wp1jlJyWOibEk5dBwasm1bSlc7-SnCYahWqzFUsAd5nGX0EZagtd9fJIwaRLPmvaPUfwGxsAk8hMmnTeZqH95mi3P9usUkeE7jDAwreS4d04lCQeKOY1guNyEPD5yl0nqatZKp8jJWOSWLGwxk3VdFGg5EcGaV8Tx64cg4yp0Fmq1DZRbBCYiL8RzkmOhcSlfFsPaginrvWq9fShpExCs3nwJDJ9o3OGmYzHk',
  },
  {
    title: 'NFT Ticket: The Cosmic Concert',
    edition: '1 of 1',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBe4EunEfzwqnTZJJILQqJsPN2dTv968icAqHKsSyNR0Ghtt9kDSFHf7IthoKpb5lsPmSy1aoPSQwHRDfMTi0uLX9oU5QUBud1q0E_b_ZPVP-LUo3djElhxDVJEQJOKoZN0KOmMw_eVqOZXYAwMH7U16NjqrMi6cYgyfb3idJxGqyA8IjaoN2VOeR4a-dPP71dt5_pf2ZJ3VwwokZ2W_SqDrgvA5oKJ06Drf7X4fcMsuNCv2HcNMpZUb0_WGDOIeZRuXRPBKsYggzA',
  },
]);

const reservedTickets = ref([
  {
    title: 'Event: Quantum Leap Festival',
    details: 'Date: 2024-08-15 | Seat: A-12',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCZU1aNqpXeGqtidMAWI3jRq3kFZMpD4ui7Kvn7xw1cZLz3cvxO3kNJeCvWqMWOEkeqmtV2rBOeN5YqHVxoVyf8B4OEu8tUkzCgIjQqRtY1oJJnsmOrlTB17Xln0xfvNTrtvMdUidXrCMpO3h4Jyk-z8PQ38A5I1sfffHVzdXd2xpLK4dHCXziAZtmxNBuqolQYyMVHoma1ucOYK1jiJQDdewtNp3Yifoti3yoVmucldShMxYYJkZhjSoO9OC8fGZVBZSlx57NO-oI',
  },
  {
    title: 'Event: Nebula Nights Rave',
    details: 'Date: 2024-09-22 | Seat: VIP-3',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuA2tVsVpZqFc6uS59vGMu8HwM4dgQeHrVZ48rV6i8uNYEdO4ahLSLCsDCJfdG8s7OFbdK0PSNXt_WUJJpCrcIx83EpbpsNwJls_Dnf-nGjnR1gNBTVjUDT7Gg3xPyzotlL8dliVB4Jj2G-LOLHlvNmJNxBFWwXTfuHjIHj85juTftCCX3eSp8Z7T4GYySUeF1TWPtbGAXejeGGfsim0SyM1BL0_xn8pONfjRXOJwMSdCYlR-pehqhge3Wbx5LCoG-M05KRv7BzuOGU',
  },
  {
    title: 'Event: Cyberpunk Cinema Marathon',
    details: 'Date: 2024-10-05 | Seat: C-7',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCTFaxYOfr4QUWIrfOpCdiAqNKtZhcHB48SHiTcOTmgrjDGIdnH283CPOQsFCvEPk3vHglSko18JoP99HFWbJbxbnAOosHX1bu-i-JLoTiseVCYJzkhlnbuNEVP8JGWaTIIVmUbRyIkfiK4VIgC-XpvkjDxsd-VKgjVULa6ZRS_iUKZUzVsQ9XBKD8uC7AhjYmiqovYiI4h9SEhWxMWQRZ6ESzbU1qcviCKvUvHKg-O4UANlvG304NJBMUpeQ7LNrg4C8kvQuxBprE',
  },
]);
</script>

<style scoped>
.main-container {
  padding: 32px 40px;
  display: flex;
  justify-content: center;
  flex: 1;
}

@media (min-width: 768px) {
  .main-container {
    padding-left: 80px;
    padding-right: 80px;
  }
}

@media (min-width: 1024px) {
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
}

.section {
  padding: 32px 0;
}

.section-title {
  color: #dce8f3;
  font-size: 24px;
  font-weight: 700;
  line-height: 1.2;
  padding: 0 16px 24px;
}

.ticket-grid {
  display: grid;
  gap: 24px;
  padding: 16px;
  grid-template-columns: repeat(1, 1fr);
}

@media (min-width: 640px) {
  .ticket-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 768px) {
  .ticket-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 1024px) {
  .ticket-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.section-placeholder {
  color: #9daebe;
  font-size: 16px;
  text-align: center;
  padding: 16px;
}
</style>