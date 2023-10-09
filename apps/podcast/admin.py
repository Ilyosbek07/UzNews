from django.contrib import admin

from .models import (Category, Comment, CommentComplaint, Podcast,
                     ProfilePodcastCommentLike, ProfilePodcastLike, Tag)


class PodcastAdmin(admin.ModelAdmin):
    readonly_fields = ["view_count"]
    prepopulated_fields = {"slug": ["title"]}


class PodcastLikeAdmin(admin.ModelAdmin):
    readonly_fields = ["status", "profile", "podcast"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["profile", "podcast", "text", "image", "parent"]


class CommentComplaintAdmin(admin.ModelAdmin):
    readonly_fields = ["comment", "profile", "text"]


class CommentLikeAdmin(admin.ModelAdmin):
    readonly_fields = ["status", "profile", "comment"]


admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentComplaint, CommentComplaintAdmin)
admin.site.register(ProfilePodcastLike, PodcastLikeAdmin)
admin.site.register(ProfilePodcastCommentLike, CommentLikeAdmin)
