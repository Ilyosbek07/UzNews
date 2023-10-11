from django.urls import path

from apps.interview import views

from apps.common.views import (
    TagCreateAPIView, TagDestroyAPIView, TagUpdateAPIView,

)
from apps.users.views import UserProfileAPIView, ProfileUpdateView, UserUpdateView, ProfileListView

urlpatterns = [
    path('interview/list/', views.InterviewListAPIView.as_view(), name='back_interview_list'),
    path('interview/detail/<slug:slug>/', views.InterviewRetrieveAPIView.as_view(), name='back_interview_list'),
    path('interview/create/', views.InterviewCreateAPIView.as_view(), name='back_interview_create'),
    path('interview/update/', views.InterviewUpdateAPIView.as_view(), name='back_interview_update'),
    path('interview/delete/', views.InterviewDestroyAPIView.as_view(), name='back_interview_delete'),

    path("tag/create/", TagCreateAPIView.as_view(), name="back_tag_create"),
    path('tag/update/', TagUpdateAPIView.as_view(), name='back_tag_update'),
    path('tag/delete/', TagDestroyAPIView.as_view(), name='back_tag_delete'),

    path("profile/list/", ProfileListView.as_view(), name="back_profile_list"),
    path("profile/detail/", UserProfileAPIView.as_view(), name="back_profile_detail"),
    path("profile/edit/<int:pk>/", ProfileUpdateView.as_view(), name="back_profile_edit"),
    path("edit/<int:pk>/", UserUpdateView.as_view(), name="back_user_edit"),

]
