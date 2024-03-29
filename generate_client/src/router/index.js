import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import RepairView from "@/views/RepairView.vue";
import HistoryView from "@/views/HistoryView.vue";
import DownloadView from "@/views/DownloadView.vue";
import LoginView from "@/views/LoginView.vue";
import ProfileView from "@/views/ProfileView.vue";
import EditProfileView from "@/views/EditProfileView.vue";
import CreateAgainView from "@/views/CreateAgainView.vue";
import ShareView from "@/views/ShareView.vue";
// import TestView from "@/views/TestView.vue";

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			name: "home",
			component: HomeView,
		},
		{
			path: "/repair",
			name: "repair",
			component: RepairView,
		},
		{
			path: "/create",
			name: "create",
			component: CreateAgainView,
		},
		{
			path: "/share",
			name: "share",
			component: ShareView,
		},
		{
			path: "/history",
			name: "history",
			component: HistoryView,
		},
		{
			path: "/download",
			name: "download",
			component: DownloadView,
		},
		{
			path: "/login",
			name: "login",
			component: LoginView,
		},
		{
			path: "/profile",
			name: "profile",
			component: ProfileView,
		},
		{
			path: "/editprofile",
			name: "editprofile",
			component: EditProfileView,
		},
		// {
		// 	path: "/test",
		// 	name: "test",
		// 	component: TestView,
		// },
	],
});

export default router;
