<template>
	<div class="popup-container">
		<div class="form-wrapper">
			<div class="header">
				<img src="@/assets/icons/fingerprint.svg" alt="Fingerprint Icon" class="icon" />
				<h2 class="title">Identify Yourself</h2>
				<p class="description">
					Please provide your phone number and ID information for verification. This helps us ensure a secure
					and
					trustworthy ticketing experience.
				</p>
			</div>
			<form @submit.prevent="handleSubmit" class="form-content">
				<div class="input-group">
					<label for="phone-number" class="input-label">Phone Number</label>
					<div class="input-wrapper">
						<img src="@/assets/icons/phone.svg" alt="Phone Icon" class="input-icon" />
						<input id="phone-number" name="phone-number" type="tel" v-model="form.phoneNumber"
							placeholder="Enter your phone number" class="input-field" />
					</div>
				</div>
				<div class="input-group">
					<label for="id-number" class="input-label">ID Number</label>
					<div class="input-wrapper">
						<img src="@/assets/icons/badge.svg" alt="ID Icon" class="input-icon" />
						<input id="id-number" name="id-number" type="text" v-model="form.idNumber"
							placeholder="Enter your ID number" class="input-field" />
					</div>
				</div>
				<button type="submit" class="submit-button">
					<img src="@/assets/icons/verify.svg" alt="Verify Icon" />
					Verify Information
				</button>
				<div class="info-links">
					<p class="info-text">Why do we need this?</p>
					<a href="#" class="learn-more">
						Learn more
					</a>
				</div>
			</form>
			<p class="footer-text">
				Your information is encrypted and stored securely. By proceeding, you agree to our
				<a href="#" class="policy-link">Verification Policy</a>.
			</p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'IdentityVerification',
	data() {
		return {
			form: {
				phoneNumber: '',
				idType: '',
				idNumber: '',
			},
		};
	},
	methods: {
		handleSubmit() {
			// Validate and emit form data
			if (this.form.phoneNumber && this.form.idType && this.form.idNumber) {
				this.$emit('submit', { ...this.form });
			} else {
				// Handle validation error (e.g., show error message)
				console.log('Please fill in all fields');
			}
		},
	},
};
</script>

<style scoped>
.popup-container {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	min-height: 100vh;
	padding: 16px;
}

.form-wrapper {
	background-color: var(--color-background);
	box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
	border-radius: 16px;
	padding: 16px;
	width: 100%;
	max-width: 448px;
	transition: transform 0.3s ease-in-out;
}

.header {
	text-align: center;
	margin-bottom: 32px;
}

.icon {
	width: 64px;
	height: 64px;
	margin-bottom: 16px;
}

.title {
	font-size: 30px;
	font-weight: 700;
	color: var(--color-heading);
	line-height: 1.2;
	margin-bottom: 12px;
}

.description {
	font-size: 16px;
	font-weight: 400;
	color: var(--color-text);
	line-height: 1.5;
}

.form-content {
	display: flex;
	flex-direction: column;
	gap: 24px;
}

.input-group {
	display: flex;
	flex-direction: column;
}

.input-label {
	font-size: 14px;
	font-weight: 500;
	color: var(--color-text);
	margin-bottom: 6px;
}

.input-wrapper {
	position: relative;
	display: flex;
	align-items: center;
}

.input-icon {
	height: 24px;
	width: 24px;
	position: absolute;
	left: 12px;
}

.input-field {
	width: 100%;
	height: 48px;
	padding: 0 12px 0 40px;
	background-color: #293548;
	border: 1px solid #3a4c62;
	border-radius: 8px;
	color: #ffffff;
	font-size: 16px;
	outline: none;
	transition: all 0.2s ease;
}

.input-field::placeholder {
	color: #64748b;
}

.input-field:focus {
	border-color: transparent;
	outline: 2px solid #5695f1;
}

.submit-button {
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 12px;
	width: 100%;
	height: 48px;
	padding: 0 24px;
	background-color: #5695f1;
	color: #ffffff;
	font-size: 16px;
	font-weight: 700;
	letter-spacing: 0.05em;
	border-radius: 12px;
	border: none;
	cursor: pointer;
	transition: all 0.2s ease;
}

.submit-button:hover {
	background-color: #4a80d1;
}

.submit-button:focus {
	outline: 2px solid #5695f1;
	outline-offset: 2px;
}

.info-links {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 16px;
	font-size: 14px;
}

@media (min-width: 640px) {
	.info-links {
		flex-direction: row;
		justify-content: center;
	}
}

.info-text {
	color: #9daebe;
}

.learn-more {
	display: flex;
	align-items: center;
	gap: 4px;
	color: #dce8f3;
	font-weight: 500;
	text-decoration: underline;
	text-underline-offset: 4px;
	transition: color 0.2s ease;
}

.learn-more:hover {
	color: #ffffff;
}

.info-icon {
	font-size: 16px;
}

.footer-text {
	margin-top: 32px;
	text-align: center;
	font-size: 12px;
	color: #64748b;
}

.policy-link {
	color: #64748b;
	text-decoration: underline;
	transition: color 0.2s ease;
}

.policy-link:hover {
	color: #9daebe;
}

@media (min-width: 768px) {
	.form-wrapper {
		padding: 48px;
	}
}
</style>