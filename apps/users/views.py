from django.db.models import Count
from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from apps.users.choices import Role
from apps.users.models import Profile, User, UserSearch
from apps.users.serializers import (PopularSearchSerializer,
                                    ProfileUpdateSerializer,
                                    RegisterUserSerializer,
                                    UserProfileSerializer,
                                    UserSearchSerializer, UserUpdateSerializer)


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer


class AuthorProfileListView(generics.ListAPIView):
    queryset = Profile.objects.filter(role=Role.author).order_by("-post_view_count")
    serializer_class = UserProfileSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        profile = self.get_object()

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


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
