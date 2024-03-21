from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
  path("signup",views.SignUpView.as_view(),name="signup"),
  path("login", views.LoginView.as_view(), name="login"),
  path("refresh", TokenRefreshView.as_view(), name="token_refresh"),
  path("edit",views.profileUpdateView.as_view(),name="edit_profile")
]