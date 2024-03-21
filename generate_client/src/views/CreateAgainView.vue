<script setup>
import { Icon } from "@iconify/vue";
import { ref } from "vue";

const style = ref([
	{ label: "效果1" },
	{ label: "效果2" },
	{ label: "效果3" },
	{ label: "效果4" },
	{ label: "效果5" },
	{ label: "效果6" },
	{ label: "效果7" },
]);

const pic3_group = ref([
	{ style: "效果1", pic: "./out/3_stylized_0.jpg" },
	{ style: "效果2", pic: "./out/3_stylized_1.jpg" },
	{ style: "效果3", pic: "./out/3_stylized_2.jpg" },
	{ style: "效果4", pic: "./out/3_stylized_3.jpg" },
	{ style: "效果5", pic: "./out/3_stylized_4.jpg" },
	{ style: "效果6", pic: "./out/3_stylized_5.jpg" },
	{ style: "效果7", pic: "./out/3_stylized_6.jpg" },
]);

const pic4_group = ref([
	{ style: "效果1", pic: "./out/4_stylized_0.jpg" },
	{ style: "效果2", pic: "./out/4_stylized_1.jpg" },
	{ style: "效果3", pic: "./out/4_stylized_2.jpg" },
	{ style: "效果4", pic: "./out/4_stylized_3.jpg" },
	{ style: "效果5", pic: "./out/4_stylized_4.jpg" },
	{ style: "效果6", pic: "./out/4_stylized_5.jpg" },
	{ style: "效果7", pic: "./out/4_stylized_6.jpg" },
]);

const pic5_group = ref([
	{ style: "效果1", pic: "./out/5_stylized_0.jpg" },
	{ style: "效果2", pic: "./out/5_stylized_1.jpg" },
	{ style: "效果3", pic: "./out/5_stylized_2.jpg" },
	{ style: "效果4", pic: "./out/5_stylized_3.jpg" },
	{ style: "效果5", pic: "./out/5_stylized_4.jpg" },
	{ style: "效果6", pic: "./out/5_stylized_5.jpg" },
	{ style: "效果7", pic: "./out/5_stylized_6.jpg" },
]);

const selectStyle = ref("");
const showList = ref(false);

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

async function picUpload() {
	let selected_pic = picture.value.name.split(".")[0];
	// console.log(selected_pic);
	let item;

	if (selected_pic == "photo_3") {
		item = pic3_group.value.filter((i) => i.style === selectStyle.value);
	} else if (selected_pic == "photo_4") {
		item = pic4_group.value.filter((i) => i.style === selectStyle.value);
	} else if (selected_pic == "photo_5") {
		item = pic5_group.value.filter((i) => i.style === selectStyle.value);
	}

	setTimeout(() => {
		img_preview.value.src = item[0]?.pic;
		img_preview.value.style.display = "block";
	}, 2000);
}

const openList = () => {
	showList.value = true;
};

const changeStyle = (value) => {
	selectStyle.value = value;
	showList.value = false;
};

const clearStyle = () => {
	selectStyle.value = "";
};
</script>

<template>
	<section class="container bg-gray-100 mx-auto pb-5">
		<div class="flex flex-col justify-center p-4 lg:flex-row">
			<div class="flex flex-col mb-24 mx-auto lg:w-1/2 lg:mb-0">
				<h1 class="text-2xl text-center font-bold mb-5 lg:text-4xl xl:mb-5">
					原始图像
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
					class="w-1/3 h-[50px] mt-5 mx-auto px-3 py-1 shadow-lg shadow-gray-500/50 bg-cyan text-white rounded-lg text-[15px] cursor-pointer active:scale-[.97] hover:bg-[#81ecec]"
					@click="picUpload"
				>
					开 始 修 复
				</button>
			</div>

			<div
				class="flex items-center mb-20 mx-auto md:w-25 lg:mb-0 lg:w-80 lg:mt-8"
			>
				<div class="rounded-xl">
					<div class="flex justify-center">
						<div class="bg-gray-100">
							<div class="max-w-md mx-auto">
								<label for="select" class="font-semibold block py-2"
									>选择效果</label
								>

								<div class="relative">
									<div
										class="h-10 bg-white flex border border-gray-200 rounded items-center"
									>
										<input
											v-model="selectStyle"
											name="select"
											id="select"
											class="px-4 appearance-none outline-none text-gray-800 w-full"
											checked
										/>

										<button
											@click="clearStyle()"
											class="cursor-pointer outline-none focus:outline-none transition-all text-gray-300 hover:text-gray-600"
										>
											<svg
												class="w-4 h-4 mx-2 fill-current"
												xmlns="http://www.w3.org/2000/svg"
												viewBox="0 0 24 24"
												stroke="currentColor"
												stroke-width="2"
												stroke-linecap="round"
												stroke-linejoin="round"
											>
												<line x1="18" y1="6" x2="6" y2="18"></line>
												<line x1="6" y1="6" x2="18" y2="18"></line>
											</svg>
										</button>

										<div
											@click="openList"
											class="cursor-pointer outline-none focus:outline-none border-l border-gray-200 transition-all text-gray-300 hover:text-gray-600"
										>
											<svg
												class="w-4 h-4 mx-2 fill-current"
												xmlns="http://www.w3.org/2000/svg"
												viewBox="0 0 24 24"
												stroke="currentColor"
												stroke-width="2"
												stroke-linecap="round"
												stroke-linejoin="round"
											>
												<polyline points="18 15 12 9 6 15"></polyline>
											</svg>
										</div>
									</div>

									<input type="checkbox" class="hidden peer" checked />
									<div
										v-if="showList"
										class="absolute rounded shadow bg-white overflow-hidden hidden peer-checked:flex flex-col w-full mt-1 border border-gray-200"
									>
										<div
											class="cursor-pointer group"
											v-for="item in style"
											@click="changeStyle(item.label)"
										>
											<a
												class="block p-2 border-transparent border-l-4 group-hover:border-[#2acfcf] group-hover:bg-gray-100"
												>{{ item.label }}</a
											>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="flex flex-col mb-24 mx-auto lg:mb-0 lg:w-1/2">
				<h1 class="text-2xl text-center font-bold mb-5 lg:text-4xl xl:mb-5">
					特色图像
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
					class="w-1/3 h-[50px] mt-5 mx-auto px-3 py-1 shadow-lg shadow-gray-500/50 bg-cyan text-white rounded-lg text-[15px] cursor-pointer active:scale-[.97] hover:bg-[#81ecec]"
				>
					下 载 图 片
				</button>
			</div>
		</div>
	</section>
</template>

<style scoped>
.desc-bg {
	border-radius: 10px;
	background-color: #ffffff;
	font-size: 18px;
	font-weight: 700;
	padding: 20px;
	box-shadow: 5px 0 10px #00000070, 0 5px 10px #00000070;
}
</style>
