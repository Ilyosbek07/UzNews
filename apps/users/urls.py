from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from apps.users.views import (AuthorProfileListView, PopularSearchesListView,
                              ProfileUpdateView, RegistrationAPIView,
                              UserProfileAPIView, UserSearchesListView,
                              UserUpdateView)

urlpatterns = [
    path(
        "searches/",
        UserSearchesListView.as_view(),
        name="user_searches",
    ),
    path(
        "popular-searches/",
        PopularSearchesListView.as_view(),
        name="popular_searches",
    ),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("registration/", RegistrationAPIView.as_view(), name="user_register"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("author/list/", AuthorProfileListView.as_view(), name="author_list"),
]
