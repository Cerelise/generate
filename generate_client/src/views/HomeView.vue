<script setup>
import { Swiper, SwiperSlide } from "swiper/vue";
import { ref } from "vue";
import { Controller } from "swiper/modules";

import "swiper/css";

const controlledSwiper1 = ref(null);
const controlledSwiper2 = ref(null);
const setControlledSwiper = (swiper) => {
	controlledSwiper1.value = swiper;
};
const setControlledSwiper1 = (swiper) => {
	controlledSwiper2.value = swiper;
};
const intro = ref([
	{
		picture: "img/swiper/1.png",
		title: "莫高窟 第420窟",
		desc: `该窟创建于隋，宋、西夏重绘部分壁画，主室为覆斗形顶，南、西、北壁各开一龛，被称为“三龛窟”。
    主室窟顶为斗四莲花藻井，花饰三兔纹样井心。藻井内岔角绘童子形飞天，外岔绘有翼兽，方井外框饰以忍冬狮子联珠纹。
    四边垂慢铺于四披。四披绘有大幅的经变场画。各场面间以树石花卉、塔庙寺院、流泉莲池、行云飞花等景物作为分隔。`,
	},
	{
		picture: "img/swiper/2.png",
		title: "观无量寿经变",
		desc: `佛经中常讲到西方净土，称这个世界有“七宝池，八功德水”，“池底以金沙布地，四边道阶，金银琉璃合成，上有楼阁，金银琉璃玻璃碎碟赤珠玛瑙而严饰之”。
    画工根据佛经的说法，精心布局，以雕栏平台天宫水池为活动环境，以阿弥陀佛为中心，两侧为观音、大势至和众多圣众，以向心式的构图，将佛国世界的种种欢乐景象以一幅巨形画面的形式生动地展示在人们面前。`,
	},
	{
		picture: "img/swiper/3.png",
		title: "菩提树双飞天",
		desc: `画工将普通的八朵花朵组成一个团花，团花心内，利用散点形式，将八朵小蓓蕾组合在一起，外围的大朵团花中，包裹着绽开的花瓣。
    四角角花为蝴蝶花，十分精巧、纯熟，蝴蝶花的触须更增添了灵动之感。细看团花，其赋色对比明亮，底色外围丹红，内层底白色，团花青、绿、红相间隔交错，对比强烈，多种层次的纹样显得赋色鲜艳无比。`,
	},
	{
		picture: "img/swiper/4.png",
		title: "乘象入胎",
		desc: `在这个窟里，只绘制了佛传故事的“乘象入胎”和“夜半逾城”两个较为重要的情节。
    这两个情节最能代表释迦牟尼一生从入世到出世而成道的经历。
    淡黄的底色上，大象和马已经变为深豬色，色彩上形成了强烈的对比。
    右边飞奔的大象，健壮威武，前后两脚站在两个飞天所托的莲花上，前面是一乘龙天人引路。
    左边的飞马，潇洒矫健，天王紧托马蹄飞奔，前面是一乘龙天人一路。
    大象和飞马的周围是飞动的流云和盛开的鲜花，整个龛顶给人一种满壁风动，热烈而又欢快的气氛。`,
	},
	{
		picture: "img/swiper/5.png",
		title: "飞天伎乐",
		desc: `洞窟主室为覆斗形顶的方形窟,西壁开一斜顶敞口佛龛,龛内初唐塑一跌坐佛、二弟子、二菩萨、二天王(清修)，清塑二菩萨。
    龛顶画跌坐佛九身、飞天二十三身。龛壁塑佛光，两侧各画四弟子、四菩萨。
    龛沿用团花边作为装饰。龛外南侧画文殊变，下画菩萨一身，龛外北侧画普贤变，下画菩萨一身。
    窟顶藻井井心为牡丹团花，垂角帷慢铺于四披，四披还画千佛，西、北披有一部分被毁坏了。`,
	},
]);
</script>

<template>
	<section class="container mx-auto bg-gray-100">
		<div class="flex flex-col mx-auto p-6 lg:flex-row">
			<div class="flex space-y-10 mb-20 lg:mt-16 lg:w-1/2">
				<swiper
					:modules="[Controller]"
					class="w-full rounded-2xl shadow-lg"
					:slides-per-view="1"
					:space-between="50"
					:controller="{ control: controlledSwiper1 }"
					@swiper="setControlledSwiper1"
				>
					<swiper-slide v-for="item in intro">
						<img :src="item.picture" alt="" />
					</swiper-slide>
				</swiper>
			</div>
			<div class="my-20 lg:mt-16 lg:w-1/2">
				<div
					class="w-[720px] rounded-[20px] border shadow-xl lg:w-3/4 lg:h-full lg:ml-20"
				>
					<swiper
						@swiper="setControlledSwiper"
						:modules="[Controller]"
						class="w-full"
						:controller="{ control: controlledSwiper2 }"
					>
						<swiper-slide class="p-10" v-for="item in intro">
							<h1 class="text-3xl text-center mb-6">
								{{ item.title }}
							</h1>

							<div
								class="text-semibold border-t-2 border-slate-600 p-5 text-wrap lg:text-2xl lg:tracking-widest"
							>
								{{ item.desc }}
							</div>
						</swiper-slide>
					</swiper>
				</div>
			</div>
		</div>
	</section>
</template>

<style scoped>
.swiper-slide img {
	width: 100%;
	height: 100%;
	object-fit: cover;
}
</style>
