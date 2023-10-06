import random
import string

from django.core import signing
from django.core.cache import cache
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.users.cache import CacheTypes, generate_cache_key
from apps.users.models import Profile, User
from apps.users.serializers import (
    RecoveryCodeSerializer,
    RegisterUserSerializer,
    SendCodeSerializer,
    UserProfileSerializer,
    VerificationRecoverySerializer,
    VerificationRegistrationCodeSerializer,
    RecoverySetPasswordSerializer,
)
from apps.users.shared import send_verification_code


class SendCodeAPIView(generics.CreateAPIView):
    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone_number"]

        session = "".join(random.choice(string.ascii_lowercase) for _ in range(12))
        send_verification_code(phone, CacheTypes.registration_sms_verification, session)
        return Response({"session": session})


class VerificationRegistrationCodeAPIView(generics.CreateAPIView):
    serializer_class = VerificationRegistrationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data.get("phone_number")
        code = serializer.validated_data.get("code")
        session = serializer.validated_data.get("session")

        cache_key = generate_cache_key(
            CacheTypes.registration_sms_verification, phone, session
        )

        if not self.is_code_valid(cache_key, code):
            return Response(
                {"detail": "Wrong code!"}, status=status.HTTP_400_BAD_REQUEST
            )

        signer = signing.TimestampSigner()
        phone_data = signer.sign_object(
            {"phone": phone, "type": CacheTypes.registration_sms_verification}
        )

        return Response({"phone": phone_data})

    @staticmethod
    def is_code_valid(cache_key, code):
        valid_code = cache.get(cache_key)
        if valid_code != code:
            return False
        return True


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class RecoveryCodeAPIView(generics.CreateAPIView):
    serializer_class = RecoveryCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone_number"]

        session = "".join(random.choice(string.ascii_lowercase) for _ in range(12))

        send_verification_code(phone, CacheTypes.forget_pass_verification, session)
        return Response({"session": session})


class VerificationRecoveryAPIView(generics.CreateAPIView):
    serializer_class = VerificationRecoverySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data.get("phone_number")
        code = serializer.validated_data.get("code")
        session = serializer.validated_data.get("session")

        cache_key = generate_cache_key(
            CacheTypes.forget_pass_verification, phone, session
        )
        if not self.is_code_valid(cache_key, code):
            return Response(
                {"detail": "Wrong code!"}, status=status.HTTP_400_BAD_REQUEST
            )
        signer = signing.TimestampSigner()
        phone_data = signer.sign_object(
            {"phone": phone, "type": CacheTypes.forget_pass_verification}
        )

        return Response({"phone": phone_data})

    @staticmethod
    def is_code_valid(cache_key, code):
        valid_code = cache.get(cache_key)
        if valid_code != code:
            return False
        return True


class RecoverySetPasswordAPIView(generics.CreateAPIView):
    serializer_class = RecoverySetPasswordSerializer


class UserProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        # Retrieve and return the user's profile based on the request user
        return Profile.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        profile = self.get_object()

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


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
