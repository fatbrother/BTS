<template>
  <div class="header-container">
    <div class="profile-info">
      <div class="avatar-wrapper">
        <div class="avatar" :style="{ backgroundImage: `url(${profile.image})` }"></div>
        <button class="avatar-button">
          <img src="@/assets/icons/photo.svg" alt="Edit Avatar" class="material-icons" />
        </button>
      </div>
      <div class="user-details">
        <p class="username">{{ profile.name }}</p>
        <p class="handle">{{ profile.handle }}</p>
      </div>
    </div>
    <button class="edit-button">
      <span class="truncate">Edit Profile</span>
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const profile = ref({
  name: 'Sophia Carter',
  handle: '@sophiacarter',
  image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuB_1AToTZLVwuo2TwcmikiTHIrIMzeIESnh6bg7SKp7JveHf3DQ7xxYBAZdtnx1yHrDWz_IRNB8mChLwTlgZoWiWcpfAtvRgyAHIqfN9ekJuyPcDQb1g9lh4xraov9UhRSPL8bRdZh72qPYshNj85ExSNtxHfmg0ZbZJ4xKJ_Y0KYmtPqSKe8d--AeW_yIaxMyh8wv-Z8BITv2KwCevTetRzirTtkkji2LzAmoNAwtjHu2MUNuf-Sf9KtiZujXynEromr12mHY3R8',
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