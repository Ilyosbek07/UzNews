from django.urls import path
from apps.common.views import AdvertisingListAPIView, SocialMediaListAPIView, get_exchange_rate, TagCreateAPIView, \
    TagListAPIView

urlpatterns = [
    path("exchange-rate/", get_exchange_rate, name="exchange_rate"),
    path("advertising/", AdvertisingListAPIView.as_view(), name="advertising_list"),
    path("socialmedia/", SocialMediaListAPIView.as_view(), name="socialmedia_list"),

    path("tag/list/", TagListAPIView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateAPIView.as_view(), name="tag_create"),

]
