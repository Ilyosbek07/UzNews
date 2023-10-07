from django.contrib import admin
from apps.common.models import Advertising, SocialMedia


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "type")
    list_filter = ("type",)
    search_fields = ("type",)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "number", "desc")  # Customize the list display fields
    search_fields = ("url", "desc")  # Enable search by 'url' and 'desc'
