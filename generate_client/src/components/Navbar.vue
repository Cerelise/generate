<script setup>
// import { Icon } from "@iconify/vue";
import TheAvatar from "./TheAvatar.vue";
import { ref } from "vue";

const menu = ref(null);
const menu_btn = ref(null);

function navToggle() {
	menu_btn.value.classList.toggle("open");
	menu.value.classList.toggle("flex");
	menu.value.classList.toggle("hidden");
}
</script>

<template>
	<!-- 导航栏容器 -->
	<nav class="relative container mx-auto p-6">
		<!-- 为所有导航栏元素准备的浮动容器 -->
		<div class="flex items-center justify-between">
			<!-- 菜单项和logo的容器 -->
			<div class="flex items-center space-x-10">
				<!-- logo -->
				<div class="space-x-2 font-bold">
					<h1>Generate</h1>
				</div>
				<!-- 左侧菜单 -->
				<div class="hidden space-x-8 font-bold lg:flex">
					<router-link
						to="/"
						class="text-grayishViolet hover:text-veryDarkViolet"
					>
						首页
					</router-link>
					<router-link
						to="/repair"
						class="text-grayishViolet hover:text-veryDarkViolet"
						>修复图片</router-link
					>
					<router-link
						to="/history"
						class="text-grayishViolet hover:text-veryDarkViolet"
						>历史记录</router-link
					>
					<a href="#" class="text-grayishViolet hover:text-veryDarkViolet"
						>下载</a
					>
				</div>
			</div>
			<!-- 右侧菜单 -->
			<div
				class="hidden items-center space-x-6 font-bold text-grayishViolet lg:flex"
			>
				<!-- <router-link
					to="/login"
					class="px-8 py-3 font-bold text-white bg-cyan rounded-full opacity-70"
				>
					登录/注册
				</router-link> -->
				<div class="flex gap-6 text-right">
					<div class="info">
						<p>Cerelise</p>
						<small class="text-muted">VIP</small>
					</div>
					<div class="profile-photo">
						<TheAvatar :width="48" :height="48" />
					</div>
				</div>
			</div>
			<!-- 汉堡菜单 -->
			<button
				ref="menu_btn"
				class="block hamburger lg:hidden focus:outline-none"
				type="button"
				@click="navToggle"
			>
				<span class="hamburger-top"></span>
				<span class="hamburger-middle"></span>
				<span class="hamburger-bottom"></span>
			</button>
		</div>
		<!-- 移动端菜单 -->
		<div
			ref="menu"
			class="absolute hidden p-6 rounded-lg bg-darkViolet left-6 right-6 top-20 z-100"
		>
			<div
				class="flex flex-col items-center justify-center w-full space-y-6 font-bold text-white rounded-sm"
			>
				<a href="#" class="w-full text-center">首页</a>
				<a href="#" class="w-full text-center">修复图片</a>
				<a href="#" class="w-full text-center">历史记录</a>
				<a href="#" class="w-full text-center">下载</a>
				<!-- <a href="#" class="w-full pt-6 border-t border-gray-400 text-center"
					>登录/注册</a
				> -->
				<a href="#" class="w-full py-3 text-center rounded-full bg-cyan"
					>登录/注册</a
				>
			</div>
		</div>
	</nav>
</template>

<style scoped>
.profile-photo {
	width: 2.8rem;
	height: 2.8rem;
	border-radius: 50%;
	overflow: hidden;
}
</style>
