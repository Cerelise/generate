<script setup>
import { Icon } from "@iconify/vue";
import { useUserStore } from "@/stores/user";
import useAxios from "@/composables/useAxios";
import { onMounted } from "vue";

const axios = useAxios();
const userStore = useUserStore();

function getData() {
	let user_id = userStore.user.id;
	axios.get(`/generate/${user_id}`).then((res) => {
		console.log(res);
	});
}

onMounted(() => {
	getData();
});

const histories = [
	{
		pic: "/img/295.png",
		pic1: "/img/295.png",
		name: "pic1",
		created_by: "Cerelise",
		status: "success",
		created_at: "24/1/9",
	},
	{
		pic: "/img/323.png",
		pic1: "/img/323.png",
		name: "pic2",
		created_by: "Cerelise",
		status: "failed",
		created_at: "24/1/9",
	},
	{
		pic: "/img/306.png",
		pic1: "/img/306.png",
		name: "pic3",
		created_by: "Cerelise",
		status: "success",
		created_at: "24/1/9",
	},
];
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
			<table
				class="mx-auto mb-5 border-t border-gray-200 md:w-[60vw] lg:w-[80vw] rounded-lg shadow"
			>
				<thead>
					<tr
						class="text-sm font-medium text-gray-700 border-b-2 border-gray-300 mx-auto"
					>
						<th
							class="whitespace-nowrap p-3 w-[30vw] text-center font-semibold tracking-wide"
						>
							picture
						</th>
						<th class="whitespace-nowrap p-3 text-center">Name</th>
						<th
							class="whitespace-nowrap p-3 text-center font-semibold tracking-wide"
						>
							Author
						</th>
						<th
							class="whitespace-nowrap p-3 text-center font-semibold tracking-wide"
						>
							Status
						</th>
						<th
							class="whitespace-nowrap p-3 text-center font-semibold tracking-wide"
						>
							<Icon icon="mdi:filter" />
						</th>
					</tr>
				</thead>

				<tbody>
					<tr
						v-for="history in histories"
						class="hover:bg-slate-200 transition-colors group"
					>
						<td
							class="whitespace-nowrap flex gap-x-4 justify-center items-center py-4"
						>
							<img
								:src="history.pic"
								alt=""
								class="w-60 aspect-[3/2] rounded-lg object-cover border border-gray-200"
							/>
							<!-- <img
								:src="history.pic1"
								alt=""
								class="w-60 aspect-[3/2] rounded-lg object-cover border border-gray-200"
							/> -->
						</td>
						<td class="whitespace-nowrap font-medium text-center">
							<div>
								<a href="#" class="text-lg font-semibold text-gray-700">
									{{ history.name }}
								</a>
							</div>
						</td>
						<td class="whitespace-nowrap font-medium text-center">
							{{ history.created_by }}
						</td>
						<td class="whitespace-nowrap font-medium text-center">
							{{ history.status }}
						</td>
						<td class="whitespace-nowrap">
							<span class="inline-block w-20 group-hover:hidden">
								{{ history.created_at }}
							</span>
							<div
								class="hidden group-hover:flex group-hover:w-20 group-hover:items-center group-hover:text-gray-500 group-hover:gap-x-2"
							>
								<button class="p-2 hover:rounded-md hover:bg-gray-200">
									<Icon icon="mdi:edit" class="w-6 h-6 fill-current" />
								</button>
								<button class="p-2 hover:rounded-md hover:bg-gray-200">
									<Icon class="w-6 h-6 fill-current" icon="mdi:trash" />
								</button>
							</div>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</main>
</template>
