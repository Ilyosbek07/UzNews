from rest_framework.parsers import MultiPartParser

from apps.users.choices import Role
from apps.users.models import Profile, User
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from apps.users.serializers import RegisterUserSerializer, UserProfileSerializer, ProfileUpdateSerializer, \
    UserUpdateSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class AuthorProfileListView(generics.ListAPIView):
    queryset = Profile.objects.filter(role=Role.author).order_by('-post_view_count')
    serializer_class = UserProfileSerializer


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    parser_classes = (MultiPartParser,)


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        profile = self.get_object()

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
