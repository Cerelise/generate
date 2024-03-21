<script setup>
// import TheAvatar from "@/components/TheAvatar.vue";
import TheButton from "@/components/TheButton.vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import { ref, reactive } from "vue";
import useAxios from "../composables/useAxios";

const axios = useAxios();
const router = useRouter();
const userStore = useUserStore();
const avatarUrl = ref(userStore.user.avatar);
const pressImg = ref(null);
const fileInputRef = ref(null);

const form = reactive({
	email: userStore.user.email,
	avatar: userStore.user.avatar,
	username: userStore.user.username,
	description: userStore.user.description,
	phone: userStore.user.phone,
});

function openFilePicker() {
	fileInputRef.value.click();
}

function avatarChange(e) {
	let file = e.target.files[0];
	// 预览base64
	let fr = new FileReader();
	fr.readAsDataURL(file);
	fr.onload = function () {
		console.log(avatarUrl.value);
		avatarUrl.value = fr.result;
		let pressCanvas = document.createElement("canvas");
		pressCanvas.width = pressImg.value.width;
		pressCanvas.height = pressImg.value.height;
		// 不使用canvas对象转化为blob
		let ctx = pressCanvas.getContext("2d");
		// drawImage
		ctx.drawImage(
			pressImg.value,
			0,
			0,
			pressImg.value.width,
			pressImg.value.height
		);
	};
}

function submitForm() {
	let formData = new FormData();
	formData.append("avatar", fileInputRef.value.files[0]);
	formData.append("username", form.username);
	formData.append("description", form.description);
	formData.append("phone", form.phone);

	axios.post("auth/edit", formData, {}).then((res) => {
		console.log(res);

		userStore.setUserInfo({
			username: form.username,
			avatar: res.user.avatar,
			description: form.description,
			phone: form.phone,
		});

		router.back();
	});
}
</script>

<template>
	<section class="container mx-auto bg-gray-100">
		<div class="p-5">
			<h2 class="title">编辑个人资料</h2>
			<div class="space-y-5">
				<input
					type="file"
					class=""
					ref="fileInputRef"
					@change="avatarChange"
					style="display: none"
				/>
				<img
					:src="avatarUrl"
					class="rounded-full w-24 h-24"
					ref="pressImg"
					@click="openFilePicker"
				/>
			</div>
		</div>
		<form class="profileForm p-6" @submit.prevent="submitForm">
			<label for="nickname">昵称：</label>
			<input type="text" v-model="form.username" />
			<label for="intro">简介：</label>
			<textarea rows="12" v-model="form.description"></textarea>
			<label for="phone">手机号：</label>
			<input type="text" v-model="form.phone" />
			<div class="actions">
				<TheButton type="reset" reverse @click.prevent="router.push('/profile')"
					>取消</TheButton
				>
				<TheButton type="submitForm">确认</TheButton>
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
