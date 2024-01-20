from django.urls import path

from . import views

urlpatterns = [
  path('record/',views.PictureListCreateView.as_view(),name="pic_list"),
  path('record/<str:pic_id>/',views.RecordRetrieveUpdateDeleteView.as_view(),name="record_datail"),
  path('<str:user_id>/',views.UserPictureListView.as_view(),name="user_pic_list"),
]