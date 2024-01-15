<script setup>
import TheAvatar from "@/components/TheAvatar.vue";
import TheButton from "@/components/TheButton.vue";
</script>

<template>
	<section class="container mx-auto bg-gray-100">
		<div class="p-5">
			<h2 class="title">编辑个人资料</h2>
			<div class="space-y-5">
				<input type="file" class="inputFile" />
				<TheAvatar :width="60" :height="60" />
			</div>
		</div>
		<form class="profileForm p-6">
			<label for="nickname">昵称：</label>
			<input type="text" />
			<label for="intro">简介：</label>
			<textarea rows="12"></textarea>
			<label for="phone">手机号：</label>
			<input type="text" />
			<div class="actions">
				<TheButton type="reset" reverse>取消</TheButton>
				<TheButton type="submit">确认</TheButton>
			</div>
		</form>
	</section>
</template>

<style scoped>
.title {
	margin-bottom: 42px;
	font-size: 24px;
	font-weight: 600;
}

.changeAvatar {
	display: flex;
	align-items: center;
}

.inputFile {
	display: none;
}

.profileForm {
	display: grid;
	grid-template-columns: max-content 1fr;
	row-gap: 32px;
	column-gap: 10px;
}

.profileForm label {
	grid-column: 1 / 2;
	justify-self: end;
	position: relative;
	top: 2px;
}

.profileForm .actions {
	grid-column: 1 / 3;
	justify-self: end;
	display: flex;
	gap: 16px;
}
</style>
