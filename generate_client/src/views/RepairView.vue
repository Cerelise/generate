<script setup>
import { Icon } from "@iconify/vue";
import { useUserStore } from "@/stores/user";
import { ref } from "vue";
import useAxios from "@/composables/useAxios";

const userStore = useUserStore();
const axios = useAxios();

const img = ref(null);
const imgInput = ref(null);
const plus = ref(null);
const img_preview = ref(null);

const picture = ref(null);

function openImg() {
	imgInput.value.click();
}

function picChange(e) {
	img.value.style.display = "block";
	picture.value = e.target.files[0];
	let img_url = URL.createObjectURL(e.target.files[0]);
	img.value.src = img_url;
	// plus.value.style.display = "none";
}

function picUpload() {
	let formData = new FormData();
	formData.append("picture", picture.value);
	formData.append("is_modify", true);
	console.log(formData);
	axios.post("/generate/record/", formData).then((res) => {
		console.log(res);
		img_preview.value.src = res.modified_pic;
		img_preview.value.display = "block";
	});
}
</script>

<template>
	<section class="container bg-gray-100 mx-auto pb-5">
		<div class="flex flex-col justify-center p-4 lg:flex-row">
			<div class="flex flex-col mb-24 mx-auto lg:w-1/2 lg:mb-0">
				<h1 class="text-2xl text-center font-bold mb-5 lg:text-4xl xl:mb-10">
					Original
				</h1>
				<div class="flex justify-center">
					<div class="rounded-lg bg-slate-400 shadow-lg">
						<div
							class="w-[400px] h-[400px] m-10 bg-slate-600/50 overflow-hidden"
							@click="openImg"
							style="border: 10px ridge #676c78"
						>
							<img src="" alt="" ref="img" />
							<input type="file" hidden ref="imgInput" @change="picChange" />
							<Icon
								icon="ic:round-plus"
								ref="plus"
								style="
									font-size: 150px;
									color: #58d2b6;
									align-content: center;
									justify-content: center;
									width: 100%;
									height: 100%;
								"
							/>
						</div>
					</div>
				</div>
				<button
					class="w-1/3 h-[50px] mt-5 mx-auto px-3 py-1 shadow-lg shadow-gray-500/50 bg-cyan text-white rounded-lg text-[15px] cursor-pointer active:scale-[.97]"
					@click="picUpload"
				>
					开 始 修 复
				</button>
			</div>

			<div
				class="flex items-center mb-20 mx-auto md:w-25 lg:mb-0 lg:w-60 lg:mt-8"
			>
				<div class="rounded-xl">
					<div class="flex justify-center">
						<img src="../assets/img/dot.png" alt="" />
					</div>
				</div>
			</div>
			<div class="flex flex-col mb-24 mx-auto lg:mb-0 lg:w-1/2">
				<h1 class="text-2xl text-center font-bold mb-5 lg:text-4xl xl:mb-10">
					Repaired
				</h1>
				<div class="flex justify-center">
					<div class="rounded-lg bg-slate-400 shadow-lg">
						<div
							class="w-[400px] h-[400px] m-10 bg-slate-600/50 overflow-hidden"
							style="border: 10px ridge #676c78"
						>
							<img
								src=""
								alt=""
								ref="img_preview"
								style="min-width: 100%; min-height: 100%"
							/>
						</div>
					</div>
				</div>
				<button
					class="w-1/3 h-[50px] mt-5 mx-auto px-3 py-1 shadow-lg shadow-gray-500/50 bg-cyan text-white rounded-lg text-[15px] cursor-pointer active:scale-[.97]"
				>
					下 载 图 片
				</button>
			</div>
		</div>
	</section>
</template>
