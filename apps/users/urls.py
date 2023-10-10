from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import RegistrationAPIView, UserProfileAPIView, AuthorProfileListView, \
    ProfileUpdateView, UserUpdateView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("registration/", RegistrationAPIView.as_view(), name="user_register"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),

    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("profile/list/", AuthorProfileListView.as_view(), name="profile-list"),

    path("profile/edit/<int:pk>/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("edit/<int:pk>/", UserUpdateView.as_view(), name="user_edit"),
]
