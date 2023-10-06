from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import (
    RecoveryCodeAPIView,
    RecoverySetPasswordAPIView,
    RegistrationAPIView,
    SendCodeAPIView,
    UserProfileAPIView,
    UserProfileUpdateView,
    VerificationRecoveryAPIView,
    VerificationRegistrationCodeAPIView,
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("send-code/", SendCodeAPIView.as_view(), name="send_code"),
    path(
        "code-verify/",
        VerificationRegistrationCodeAPIView.as_view(),
        name="code_verify",
    ),
    path("registration/", RegistrationAPIView.as_view(), name="user_register"),
    path("send-recovery/", RecoveryCodeAPIView.as_view(), name="send_recovery"),
    path(
        "recovery-verify/",
        VerificationRecoveryAPIView.as_view(),
        name="recovery_verify",
    ),
    path(
        "recovery-set-password/",
        RecoverySetPasswordAPIView.as_view(),
        name="recovery_verify",
    ),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    path("profile/edit/", UserProfileUpdateView.as_view(), name="profile_edit"),
    # path("notifications/", NotificationsAPIView.as_view(), name="all_notifications"),
    # path("read-notifications/", ReadNotificationsAPIView.as_view(), name="read_notifications"),
    # path("detail-notifications/<int:pk>/", ReadDetailNotificationAPIView.as_view(), name="detail_notifications"),
]
