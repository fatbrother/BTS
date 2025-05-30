import { useWalletStore } from '@/stores/wallet'
import { computed } from 'vue'

export function useWallet() {
  const walletStore = useWalletStore()

  return {
    // State
    address: computed(() => walletStore.address),
    isConnected: computed(() => walletStore.isConnected),
    isConnecting: computed(() => walletStore.isConnecting),
    error: computed(() => walletStore.error),
    balance: computed(() => walletStore.balance),
    network: computed(() => walletStore.network),
    shortAddress: computed(() => walletStore.shortAddress),

    // Actions
    connectWallet: walletStore.connectWallet,
    disconnectWallet: walletStore.disconnectWallet,
    clearError: walletStore.clearError,
    refreshBalance: walletStore.getBalance
  }
}