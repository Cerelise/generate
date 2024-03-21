from django.urls import path

from . import views

urlpatterns = [
  path('result',views.getAllResult,name="get_all_result_list"),
  path('result/like/<str:res_id>',views.addLike,name="user_res_like"),
  path('origin-list',views.getUserPic),
  path('current-user',views.get_user_for_current),
  path('record',views.PictureListCreateView.as_view()),
  path('record/<str:pic_id>',views.RecordRetrieveUpdateDeleteView.as_view()),
]