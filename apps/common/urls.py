from django.urls import path
from apps.common.views import AdvertisingListAPIView, SocialMediaListAPIView

urlpatterns = [
    path("advertising/", AdvertisingListAPIView.as_view(), name="advertising_list"),
    path("socialmedia/", SocialMediaListAPIView.as_view(), name="socialmedia_list"),
]
