from django.contrib import admin
from apps.common.models import Advertising, SocialMedia, Tag, ContentView


@admin.register(Tag)
class InterviewTagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "type")
    list_filter = ("type",)
    search_fields = ("type",)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "number", "desc")  # Customize the list display fields
    search_fields = ("url", "desc")  # Enable search by 'url' and 'desc'


@admin.register(ContentView)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "content_object")

