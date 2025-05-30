<template>
  <div class="tabs-container">
    <a
      v-for="tab in tabs"
      :key="tab"
      :href="`#${tab.toLowerCase()}`"
      class="tab"
      :class="{ 'tab-active': activeTab === tab.toLowerCase() }"
      @click.prevent="setActiveTab(tab.toLowerCase())"
    >
      <p class="tab-text">{{ tab }}</p>
    </a>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const tabs = ref(['Collected', 'Reserved', 'History']);
const activeTab = defineModel('activeTab', { type: String, default: 'collected' });

const setActiveTab = (tab) => {
  activeTab.value = tab;
};
</script>

<style scoped>
.tabs-container {
  display: flex;
  justify-content: center;
  gap: 24px;
  padding: 24px 16px 16px;
  border-bottom: 1px solid #3d4d5c;
}

@media (min-width: 768px) {
  .tabs-container {
    gap: 32px;
  }
}

.tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px 0 12px;
  color: #9daebe;
  text-decoration: none;
  border-bottom: 3px solid transparent;
  transition: all 0.3s ease;
}

.tab:hover {
  color: #ffffff;
  border-bottom-color: #dce8f3;
}

.tab-active {
  color: #ffffff;
  border-bottom-color: #dce8f3;
}

.tab-text {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.015em;
}

.tab:hover .tab-text {
  color: #ffffff;
}
</style>