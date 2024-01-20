<script setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/user";
import useAxios from "../composables/useAxios";

const userStore = useUserStore();
const router = useRouter();
const axios = useAxios();

const user = reactive({
	email: "",
	password: "",
});

async function signup() {
	const userForm = new FormData();
	userForm.append("email", user.email);
	userForm.append("password", user.password);
	console.log(userForm);
	await axios.post(`auth/signup/`, userForm).then((res) => {
		console.log(res);
		if ((res.message = "User Created Successfully")) {
			router.push({ name: "login" });
		}
	});
}

async function login() {
	const userForm = new FormData();
	userForm.append("email", user.email);
	userForm.append("password", user.password);
	await axios.post(`auth/login/`, userForm).then((res) => {
		console.log(res);
		userStore.setToken(res.tokens.access);
		userStore.initStore();
		router.push({ name: "home" });
	});
}

const box = ref(null);

const toRegister = () => {
	box.value.classList.add("active");
};

const toLogin = () => {
	box.value.classList.remove("active");
};
</script>

<template>
	<div class="container mx-auto p-6 lg:flex-row">
		<div class="box" ref="box">
			<div class="form-container sign-up">
				<div class="form">
					<h1>创建账号</h1>
					<span>请补充下面的信息</span>
					<input type="email" placeholder="Email" v-model="user.email" />
					<input type="password" placeholder="密码" v-model="user.password" />
					<button @click="signup">注 册</button>
				</div>
			</div>
			<div class="form-container sign-in">
				<div class="form">
					<h1>登录</h1>
					<span>欢迎使用画容！</span>
					<input type="email" v-model="user.email" placeholder="Email" />
					<input type="password" v-model="user.password" placeholder="密码" />
					<a href="#">忘记密码？</a>
					<button @click="login">登 录</button>
				</div>
			</div>
			<div class="toggle-container">
				<div class="toggle">
					<div class="toggle-panel toggle-left">
						<h1>欢迎回来！</h1>
						<p>输入您的个人详细信息以使用网站的所有功能。</p>
						<button class="hide" @click="toLogin">去登录</button>
					</div>
					<div class="toggle-panel toggle-right">
						<h1>你好，新朋友！</h1>
						<p>使用您的个人详细信息注册一个新账号用于使用该网站的所有功能</p>
						<button class="hide" @click="toRegister">去注册</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
.container {
	@apply bg-gray-100 py-[15vh];
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
}

.box {
	background-color: #fff;
	border-radius: 30px;
	box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
	position: relative;
	overflow: hidden;
	width: 768px;
	max-width: 100%;
	min-height: 480px;
}

.box p {
	font-size: 14px;
	line-height: 20px;
	letter-spacing: 0.3px;
	margin: 20px 0;
}

.box span {
	font-size: 12px;
}

.box a {
	color: #333;
	font-size: 13px;
	text-decoration: none;
	margin: 15px 0 10px;
}

.box button {
	background-color: #6adede;
	color: #fff;
	font-size: 12px;
	padding: 10px 45px;
	border: 1px solid transparent;
	border-radius: 8px;
	font-weight: 600;
	letter-spacing: 0.5px;
	text-transform: uppercase;
	margin-top: 10px;
	cursor: pointer;
}

.box button.hide {
	background-color: transparent;
	border-color: #fff;
}

.box .form {
	background-color: #fff;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 40px;
	height: 100%;
}

.box input {
	background-color: #eee;
	border: none;
	margin: 8px 0;
	padding: 10px 15px;
	font-size: 13px;
	border-radius: 8px;
	width: 100%;
	outline: none;
}

.form-container {
	position: absolute;
	top: 0;
	height: 100%;
	transition: all 0.6s ease-in-out;
}

.sign-in {
	left: 0;
	width: 50%;
	z-index: 2;
}

.box.active .sign-in {
	transform: translateX(100%);
}

.sign-up {
	left: 0;
	width: 50%;
	opacity: 0;
	z-index: 1;
}

.box.active .sign-up {
	transform: translateX(100%);
	opacity: 1;
	z-index: 5;
	animation: move 0.6s;
}

@keyframes move {
	0%,
	49.99% {
		opacity: 0;
		z-index: 1;
	}
	50%,
	100% {
		opacity: 1;
		z-index: 5;
	}
}

.social-icons {
	margin: 20px 0;
}

.social-icons a {
	border: 1px solid #ccc;
	border-radius: 20%;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	margin: 0 3px;
	width: 40px;
	height: 40px;
}

.toggle-container {
	position: absolute;
	top: 0;
	left: 50%;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: all 0.6s ease-in-out;
	border-radius: 150px 0 0 100px;
	z-index: 1000;
}

.box.active .toggle-container {
	transform: translateX(-100%);
	border-radius: 0 150px 100px 0;
}

.toggle {
	background-color: #6adede;
	height: 100%;
	/* background: linear-gradient(to right, #5c6bc0, #512da8); */
	background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
	color: #fff;
	position: relative;
	left: -100%;
	height: 100%;
	width: 200%;
	transform: translateX(0);
	transition: all 0.6s ease-in-out;
}

.box.active .toggle {
	transform: translateX(50%);
}

.toggle-panel {
	position: absolute;
	width: 50%;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 30px;
	text-align: center;
	top: 0;
	transform: translateX(0);
	transition: all 0.6s ease-in-out;
}

.toggle-left {
	transform: translateX(-200%);
}

.box.active .toggle-left {
	transform: translateX(0);
}

.toggle-right {
	right: 0;
	transform: translateX(0);
}

.box.active .toggle-right {
	transform: translateX(200%);
}
</style>
