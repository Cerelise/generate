from django.urls import path

from . import views
urlpatterns = [
  path("current_user/", views.get_user_for_current,
         name="current_user"),
  path('original/',views.OriginListCreateView.as_view(),name="list_origin"),
  path('<str:pic_id>/',views.OriginalRetrieveUpdateDeleteView.as_view(),name="origin_datail")
]