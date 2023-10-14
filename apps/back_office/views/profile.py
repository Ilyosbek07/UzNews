from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.users.models import Profile, User
from apps.users.serializers import ProfileUpdateSerializer, UserUpdateSerializer, UserProfileSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer


class ProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        profile = Profile.objects.get(user=self.request.user)
        return profile

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
