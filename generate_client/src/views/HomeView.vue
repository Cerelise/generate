<script setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";

const onSwiper = (swiper) => {
	console.log(swiper);
};
const onSlideChange = () => {
	console.log("slide change");
};
</script>

<template>
	<section class="container mx-auto bg-gray-100">
		<div class="flex flex-col-reverse p-6 lg:flex-row">
			<div class="flex flex-col space-y-10 mb-44 lg:mt-16 lg:w-1/2">
				<h1
					class="text-5xl font-bold text-center lg:text-6xl lg:max-w-md lg:text-left lg:mt-8"
				>
					深度学习壁画修复系统
				</h1>
				<p class="text-2xl text-center text-gray-400 lg:max-w-md lg:text-left">
					Build your brand's recognition and get detailed insights on how your
					links are performing.
				</p>
				<div class="mx-auto lg:mx-0">
					<a
						href="#"
						class="py-5 px-10 text-2xl font-bold text-white bg-cyan rounded-full hover:opacity-70 lg:py-4"
						>Get Startted</a
					>
				</div>
			</div>
			<div class="my-24 mx-auto md:w-180 lg:mb-0 lg:w-1/2">
				<swiper
					class="w-[40vw] h-full rounded-2xl shadow-lg md:h-[60vh]"
					:slides-per-view="1"
					:space-between="50"
					@swiper="onSwiper"
					@slideChange="onSlideChange"
				>
					<swiper-slide>
						<img
							class="w-full md:h-[60vh]"
							src="../assets/img/306.png"
							alt=""
						/>
					</swiper-slide>
					<swiper-slide>
						<img
							class="w-full md:h-[60vh]"
							src="../assets/img/295.png"
							alt=""
						/>
					</swiper-slide>
					<swiper-slide>
						<img
							class="w-full md:h-[60vh]"
							src="../assets/img/355.png"
							alt=""
						/>
					</swiper-slide>
				</swiper>
			</div>
		</div>
	</section>
</template>

<style></style>
