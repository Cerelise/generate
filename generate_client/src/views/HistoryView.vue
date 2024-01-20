<script setup>
import { Icon } from "@iconify/vue";
import { useUserStore } from "@/stores/user";
import useAxios from "@/composables/useAxios";
import { ref, onMounted } from "vue";

const axios = useAxios();
const userStore = useUserStore();
const histories = ref([]);

async function getData() {
	let user_id = userStore.user.id;
	console.log(user_id);
	await axios.get(`/generate/${user_id}`).then((res) => {
		histories.value = res;
		console.log(histories.value);
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
				class="inline-flex gap-x-2 items-center py-2.5 px-6 text-white bg-cyan rounded-xl hover:bg-teal-400 focus:outline-none focus:ring-2 focus:ring-offset-1"
			>
				<Icon class="w-6 h-6 fill-current" icon="ic:baseline-plus" />
				<span class="text-sm font-semibold tracking-wide">新建</span>
			</button>
		</div>

		<div class="overflow-auto">
			<table class="max-w-5xl mx-auto table-auto">
				<thead class="justify-between">
					<tr class="bg-[#f3f4f6]">
						<th class="px-16 py-2">
							<span class="font-semibold">Picture</span>
						</th>

						<th class="px-16 py-2">
							<span class="font-semibold">Name</span>
						</th>

						<th class="px-16 py-2">
							<span class="font-semibold">NewPic</span>
						</th>

						<th class="px-16 py-2">
							<span class="font-semibold">status</span>
						</th>

						<th class="px-16 py-2">
							<span class="font-semibold">Date</span>
						</th>

						<th class="px-16 py-2">
							<span class="font-semibold">Setting</span>
						</th>
					</tr>
				</thead>
				<tbody class="bg-gray-200">
					<tr
						v-for="history in histories"
						class="bg-white border-b-2 border-gray-200 hover:bg-slate-200 transition-colors group"
					>
						<td class="px-4 py-2 flex flex-row items-center">
							<img
								class="h-18 w-18 object-cover"
								:src="history.picture"
								alt=""
							/>
						</td>

						<td>
							<span class="px-16 py-2 font-semibold">{{ history.name }}</span>
						</td>

						<td class="px-4 py-2 flex flex-row items-center">
							<img
								class="h-15 w-15 object-cover"
								:src="history.result"
								alt=""
							/>
						</td>

						<td class="px-16 py-2">
							<div
								v-if="history.is_modify == true"
								class="relative grid items-center font-sans font-bold uppercase whitespace-nowrap select-none bg-green-500/20 text-green-900 py-1 px-2 text-xs rounded-md"
							>
								<span>success</span>
							</div>
							<div
								v-else
								class="relative grid items-center text-center font-sans font-bold uppercase whitespace-nowrap select-none bg-[#ef4444] text-[#7f1d1d] py-1 px-2 text-xs rounded-md"
								style="opacity: 1"
							>
								<span>failed</span>
							</div>
						</td>
						<td class="px-16 py-2">
							<span>{{ history.created_at.split("T")[0] }}</span>
						</td>

						<td class="px-16 py-2">
							<span class="text-yellow-500 flex">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5 text-green-700 mx-2"
									viewBox="0 0 20 20"
									fill="currentColor"
								>
									<path
										d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"
									/>
									<path
										fill-rule="evenodd"
										d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
										clip-rule="evenodd"
									/>
								</svg>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5 text-red-700"
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
