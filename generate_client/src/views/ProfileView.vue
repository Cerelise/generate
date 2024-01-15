<script setup>
import TheAvatar from "@/components/TheAvatar.vue";
</script>

<template>
	<section class="container mx-auto bg-gray-100">
		<div class="flex flex-col lg:flex-row">
			<div class="profile-photo space-y-10 mt-10 mb-20 lg:mt-16 lg:w-1/2">
				<TheAvatar :width="186" :height="186" />
			</div>
			<div
				class="profile text-xl text-center lg:max-w-md lg:mt-12 lg:text-left"
			>
				<p class="name flex justify-center gap-5 lg:justify-start">
					<span>Cerelise</span>
					<router-link to="/editprofile">编辑个人资料</router-link>
				</p>
				<p class="handle">@cerelise_wong</p>
				<div class="description text-center mx-auto lg:text-left lg:mx-0">
					Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum
					dolor sit amet. Lorem ipsum dolor sit amet.
				</div>
				<p class="my-5">github.com</p>
			</div>
		</div>
	</section>
</template>

<style scoped>
.profileContainer {
	@apply py-[25vh];
	display: grid;
	grid-template-columns: 1fr 1fr;
	column-gap: 10vw;
}

.profile-photo {
	display: flex;
	justify-content: center;
}

.profile-photo img {
	width: 200px;
	height: 200px;
	border-radius: 50%;
	background: #eee;
	object-fit: cover;
	object-position: top center;
}

.profile .name > span {
	font-size: 26px;
}
.profile .name > a {
	color: #1da0ff;
	text-decoration: none;
	margin-left: 26px;
}

.profile .handle {
	margin-top: 4px;
	color: #848484;
}

.profile .description {
	margin-top: 26px;
	word-wrap: break-word;
	max-width: 500px; /* 设置容器的最大宽度 */
}
</style>
