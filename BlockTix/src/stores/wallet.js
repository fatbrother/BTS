
// stores/wallet.js
import { defineStore } from 'pinia'

export const useWalletStore = defineStore('wallet', {
	state: () => ({
		address: null,
		isConnected: false,
		isConnecting: false,
		error: null,
		balance: null,
		network: null
	}),

	getters: {
		shortAddress: (state) => {
			if (!state.address) return null
			return `${state.address.slice(0, 6)}...${state.address.slice(-4)}`
		},

		isMetaMaskAvailable: () => {
			return typeof window !== 'undefined' && !!window.ethereum
		}
	},

	actions: {
		async connectWallet() {
			if (!this.isMetaMaskAvailable) {
				this.error = 'MetaMask not detected. Please install MetaMask extension.'
				return false
			}

			this.isConnecting = true
			this.error = null

			try {
				// Request account access
				const accounts = await window.ethereum.request({
					method: 'eth_requestAccounts'
				})

				if (accounts.length > 0) {
					this.address = accounts[0]
					this.isConnected = true

					// Get additional wallet info
					await this.getBalance()
					await this.getNetwork()

					// Listen for account changes
					this.setupEventListeners()

					return true
				}
			} catch (error) {
				console.error('Connection error:', error)
				this.error = error.message || 'Failed to connect wallet'
				return false
			} finally {
				this.isConnecting = false
			}
		},

		async disconnectWallet() {
			this.address = null
			this.isConnected = false
			this.balance = null
			this.network = null
			this.error = null

			// Remove event listeners
			if (window.ethereum) {
				window.ethereum.removeAllListeners('accountsChanged')
				window.ethereum.removeAllListeners('chainChanged')
			}
		},

		async getBalance() {
			if (!this.address || !window.ethereum) return

			try {
				const balance = await window.ethereum.request({
					method: 'eth_getBalance',
					params: [this.address, 'latest']
				})

				// Convert from wei to ETH
				this.balance = parseInt(balance, 16) / Math.pow(10, 18)
			} catch (error) {
				console.error('Error getting balance:', error)
			}
		},

		async getNetwork() {
			if (!window.ethereum) return

			try {
				const chainId = await window.ethereum.request({ method: 'eth_chainId' })
				this.network = this.getNetworkName(chainId)
			} catch (error) {
				console.error('Error getting network:', error)
			}
		},

		getNetworkName(chainId) {
			const networks = {
				'0x1': 'Ethereum Mainnet',
				'0x3': 'Ropsten Testnet',
				'0x4': 'Rinkeby Testnet',
				'0x5': 'Goerli Testnet',
				'0x89': 'Polygon Mainnet',
				'0x13881': 'Polygon Mumbai Testnet'
			}
			return networks[chainId] || `Unknown Network (${chainId})`
		},

		setupEventListeners() {
			if (!window.ethereum) return

			// Handle account changes
			window.ethereum.on('accountsChanged', (accounts) => {
				if (accounts.length === 0) {
					this.disconnectWallet()
				} else if (accounts[0] !== this.address) {
					this.address = accounts[0]
					this.getBalance()
				}
			})

			// Handle network changes
			window.ethereum.on('chainChanged', () => {
				this.getNetwork()
				this.getBalance()
			})
		},

		clearError() {
			this.error = null
		}
	}
})