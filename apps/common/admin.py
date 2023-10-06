from django.contrib import admin
from apps.common.models import Advertising, SocialMedia

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type')  # Customize the list display fields
    list_filter = ('type',)  # Add filtering options based on 'type'
    search_fields = ('type',)  # Enable search by 'type'

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'number', 'desc')  # Customize the list display fields
    search_fields = ('url', 'desc')  # Enable search by 'url' and 'desc'
