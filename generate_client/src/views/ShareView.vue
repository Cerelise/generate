<script setup>
import TheAvatar from "@/components/TheAvatar.vue";
import { Icon } from "@iconify/vue";
import useAxios from "../composables/useAxios";

import { ref, onMounted } from "vue";

const axios = useAxios();
const resultList = ref([]);

function getData() {
	axios.get(`/generate/result`).then((res) => {
		resultList.value = res;
		console.log(resultList.value);
	});
}

function toggleFavorite(resId) {
	axios.post(`/generate/result/like/${resId}`).then((res) => {
		// console.log(res);
		getData();
	});
}

onMounted(() => {
	getData();
});
</script>

<template>
	<section class="container mx-auto bg-gray-100">
		<div class="p-5 flex flex-col">
			<div
				class="flex flex-col items-center justify-between py-3 px-10 lg:flex-row"
			>
				<div class="mb-10 text-center lg:text-left">
					<h1 class="text-2xl font-semibold leading-relaxed text-gray-800">
						共享社区
					</h1>
					<p class="text-sm font-medium text-gray-500">
						您可以在这里查看用户们分享的照片！
					</p>
				</div>
			</div>
			<div class="px-5">
				<div class="mt-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
					<div v-for="item in resultList" class="cursor-pointer">
						<div class="relative overflow-hidden aspect-square rounded-xl">
							<img :src="item.modified_pic" alt="" />
						</div>
						<div class="mt-4 flex justify-between">
							<div class="flex gap-2">
								<TheAvatar :src="item.created_by.avatar" />
								<p class="text-md text-gray-400">
									{{ item.created_by.username }}
								</p>
							</div>
							<div
								class="flex items-center gap-1"
								@click="toggleFavorite(item.id)"
							>
								<Icon icon="icon-park-outline:like" />
								<p class="text-md text-gray-400">{{ item.like_count }}</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<style scoped></style>
