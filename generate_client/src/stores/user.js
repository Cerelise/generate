import { defineStore } from "pinia";
import useAxios from "../composables/useAxios";

const axios = useAxios();

export const useUserStore = defineStore("user", {
	state: () => ({
		user: {
			isAuthenticated: false,
			id: null,
			username: null,
			email: null,
			token: null,
		},
	}),
	actions: {
		initStore() {
			console.log("initStore");
			const token = localStorage.getItem("user.token");

			if (token) {
				axios.get(`auth/login/`).then((res) => {
					this.user.id = res.id;
					this.user.email = res.email;
					this.user.avatar = res.avatar;
					this.user.username = res.username;
					this.user.phone = res.phone;
					this.user.description = res.description;
					this.user.is_vip = res.is_vip;
					this.user.isAuthenticated = true;
				});
			}
		},

		setToken(data) {
			console.log("setToken", data);

			this.user.token = data;

			this.user.isAuthenticated = true;

			localStorage.setItem("user.token", data);

			console.log("用户的token已设置：" + this.user.token);
		},

		removeToken() {
			console.log("removeToken");

			this.user.id = null;
			this.user.email = null;
			this.user.avatar = null;
			this.user.username = null;
			this.user.phone = null;
			this.user.description = null;
			this.user.is_vip = null;
			this.user.isAuthenticated = false;

			localStorage.setItem("user.token", "");
		},

		setUserInfo(user) {
			console.log("setUserInfo", user);

			this.user.avatar = user.avatar;
			this.user.username = user.username;
			this.user.phone = user.phone;
			this.user.description = user.description;

			console.log("User :>> ", this.user);
		},
	},
});
