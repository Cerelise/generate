from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  path("signup/",views.SignUpView.as_view(),name="signup"),
  path("login/", views.LoginView.as_view(), name="login"),
  path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]