<script setup>
import { Icon } from "@iconify/vue";
import { useUserStore } from "@/stores/user";
import useAxios from "@/composables/useAxios";
import { ref, onMounted } from "vue";

const axios = useAxios();
const userStore = useUserStore();
const histories = ref([]);

function getData() {
	let user_id = userStore.user.id;
	// console.log(user_id);
	axios.get(`/generate/origin-list?id=${user_id}`).then((res) => {
		histories.value = res;
		// console.log(histories.value);
	});
}

function deleteDetail(originId) {
	axios.delete(`/generate/record/${originId}`).then((res) => {
		// console.log(res);
		getData();
	});
}

onMounted(() => {
	getData();
});
</script>

<template>
	<main class="container bg-gray-100 mx-auto">
		<div
			class="flex flex-col items-center justify-between py-5 px-10 lg:flex-row"
		>
			<div class="mb-10 text-center lg:text-left">
				<h1 class="text-2xl font-semibold leading-relaxed text-gray-800">
					历史记录
				</h1>
				<p class="text-sm font-medium text-gray-500">
					您可以在这里查看您的图片修复历史！
				</p>
			</div>
			<button
				class="inline-flex gap-x-2 items-center py-2.5 px-6 text-white bg-cyan rounded-xl outline-none focus:ring-2 focus:ring-offset-1 hover:bg-[#81ecec]"
			>
				<Icon class="w-6 h-6 fill-current" icon="ic:baseline-plus" />
				<router-link class="text-sm font-semibold tracking-wide" to="/repair"
					>新建</router-link
				>
			</button>
		</div>

		<div class="overflow-auto">
			<table class="max-w-5xl mx-auto table-auto">
				<thead class="justify-between">
					<tr class="bg-[#f3f4f6]">
						<th class="px-12 py-2">
							<span class="font-semibold">原始图片</span>
						</th>

						<th class="px-4 py-2">
							<span class="font-semibold">图片名</span>
						</th>

						<th class="px-12 py-2">
							<span class="font-semibold">修复后图片</span>
						</th>

						<th class="px-4 py-2">
							<span class="font-semibold">状态</span>
						</th>

						<th class="px-4 py-2">
							<span class="font-semibold">日期</span>
						</th>

						<th class="px-8 py-2">
							<span class="font-semibold">操作</span>
						</th>
					</tr>
				</thead>
				<tbody class="bg-gray-200">
					<tr
						v-for="history in histories"
						class="bg-white border-b-2 border-gray-200 hover:bg-slate-200 transition-colors group"
					>
						<td class="px-4 py-2 flex flex-row items-center">
							<img class="w-[15vw] h-[20vh]" :src="history.picture" alt="" />
						</td>

						<td>
							<span class="px-4 py-2 font-semibold">{{ history.name }}</span>
						</td>

						<td class="px-4 py-2 flex flex-row items-center">
							<img class="w-[15vw] h-[20vh]" :src="history.result" alt="" />
						</td>

						<td class="px-4 py-2">
							<div
								v-if="history.is_modify == true"
								class="relative grid items-center font-sans font-bold uppercase whitespace-nowrap select-none bg-green-500/20 text-green-900 py-1 px-2 text-xs rounded-md"
							>
								<span>修复成功</span>
							</div>
							<div
								v-else
								class="relative grid items-center text-center font-sans font-bold uppercase whitespace-nowrap select-none bg-[#ef4444] text-[#7f1d1d] py-1 px-2 text-xs rounded-md"
								style="opacity: 1"
							>
								<span>修复失败</span>
							</div>
						</td>
						<td class="px-4 py-2">
							<span>{{ history.created_at.split("T")[0] }}</span>
						</td>

						<td class="px-12 py-2">
							<span class="flex" @click="deleteDetail(history.id)">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5 text-orange-700"
									viewBox="0 0 20 20"
									fill="currentColor"
								>
									<path
										fill-rule="evenodd"
										d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
										clip-rule="evenodd"
									/>
								</svg>
							</span>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</main>
</template>
