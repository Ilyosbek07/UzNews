from django.contrib import admin
from apps.users.models import User, Profile


@admin.register(User)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "email")
    list_filter = ("phone_number",)
    search_fields = ("phone_number",)


@admin.register(Profile)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("id", "role")
