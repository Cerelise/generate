<template>
	<button class="button" :class="{ primary: color === 'primary', reverse }">
		<slot></slot>
	</button>
</template>
<script setup>
defineProps({
	color: {
		type: String,
		default: "primary",
	},
	reverse: Boolean,
});
</script>
<style scoped>
.button {
	/* background-color: #6adede; */
	color: #fff;
	font-size: 15px;
	padding: 10px 45px;
	border: 1px solid transparent;
	border-radius: 8px;
	font-weight: 600;
	letter-spacing: 0.5px;
	text-transform: uppercase;
	margin-top: 10px;
	cursor: pointer;
}

.button.primary {
	background: #81ecec;
}

.button.reverse {
	background: none;
	border: 1px solid #e8e8e8;
	color: initial;
}
</style>
