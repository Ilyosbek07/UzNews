from django.urls import path
from apps.common.views import AdvertisingListAPIView, SocialMediaListAPIView

urlpatterns = [
    path("advertisings/", AdvertisingListAPIView.as_view(), name="advertising-list"),
    path("socialmedia/", SocialMediaListAPIView.as_view(), name="socialmedia-list"),
]
