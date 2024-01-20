<script setup>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import { useUserStore } from "./stores/user";

const userStore = useUserStore();

userStore.initStore();
</script>

<template>
	<Navbar />
	<router-view></router-view>
	<Footer />
</template>
