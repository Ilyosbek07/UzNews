from django.contrib import admin

from .models import Comment, CommentComplaint, Podcast


class PodcastAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["profile", "podcast", "text", "image", "parent"]


class CommentComplaintAdmin(admin.ModelAdmin):
    readonly_fields = ["comment", "profile", "text"]


admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentComplaint, CommentComplaintAdmin)
