from django.contrib import admin
from .models import Tag, Category, Podcast, UserPodcastPreference

class PodcastAdmin(admin.ModelAdmin):
    readonly_fields = ['view_count', 'like_count', 'dislike_count']
    prepopulated_fields = {"slug": ["title"]}

class PodcastPreferenceAdmin(admin.ModelAdmin):
    readonly_fields = ['status', 'profile', 'content']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}

admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(UserPodcastPreference, PodcastPreferenceAdmin)
