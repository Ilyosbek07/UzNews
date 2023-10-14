from django.db.models import Count
from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from apps.users.choices import Role
from apps.users.models import Profile, User, UserSearch
from apps.users.serializers import (
    PopularSearchSerializer,
    ProfileUpdateSerializer,
    RegisterUserSerializer,
    UserProfileSerializer,
    UserSearchSerializer,
    UserUpdateSerializer,
)


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer


class AuthorProfileListView(generics.ListAPIView):
    queryset = Profile.objects.filter(role=Role.author).order_by("-post_view_count")
    serializer_class = UserProfileSerializer


class UserSearchesListView(generics.ListAPIView):
    queryset = UserSearch.objects.all()
    serializer_class = UserSearchSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserSearch.objects.filter(user=self.request.user).order_by("-created_at")
        return UserSearch.objects.none()


class PopularSearchesListView(generics.ListAPIView):
    queryset = UserSearch.objects.all()
    serializer_class = PopularSearchSerializer

    def get_queryset(self):
        return UserSearch.objects.values("search_text").annotate(count=Count("search_text")).order_by("-count")
