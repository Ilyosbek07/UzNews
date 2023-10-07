from apps.users.models import Profile, User
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from apps.users.serializers import RegisterUserSerializer, UserProfileSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        serializer = self.serializer_class(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        profile = self.get_object()

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


# class NotificationsAPIView(generics.ListAPIView):
#     serializer_class = NotificationSerializer
#     queryset = Notification.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class ReadDetailNotificationAPIView(generics.RetrieveAPIView):
#     serializer_class = NotificationSerializer
#     queryset = Notification.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request, *args, **kwargs):
#         self.get_or_create_read_notification()
#         return self.retrieve(request, *args, **kwargs)
#
#     def get_or_create_read_notification(self):
#         ReadNotification.objects.get_or_create(user=self.request.user, notification=self.get_object())
#
#
# class ReadNotificationsAPIView(generics.ListAPIView):
#     serializer_class = ReadNotificationSerializer
#     queryset = ReadNotification.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
