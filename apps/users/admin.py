from django.contrib import admin
from apps.users.models import User, Profile


@admin.register(User)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "email")  # Customize the list display fields
    list_filter = ("phone_number",)  # Add filtering options based on 'type'
    search_fields = ("phone_number",)  # Enable search by 'type'


@admin.register(Profile)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("id", "surname", "role")
    list_filter = ("surname",)
    search_fields = ("surname",)
