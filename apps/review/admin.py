from django.contrib import admin

from .models import (Category, Comment, CommentLike, Review, ReviewLiked,
                     ReviewView, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    verbose_name = "Tag"
    verbose_name_plural = "Tags"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name", "slug")
    search_fields = ("name", "slug")
    verbose_name = "Podcast Category"
    verbose_name_plural = "Podcast Categories"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "author", "liked", "view")
    list_filter = ("liked", "view", "author", "tag", "category")
    search_fields = ("title", "subtitle", "author__username")
    verbose_name = "Review"
    verbose_name_plural = "Reviews"
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ReviewLiked)
class ReviewLikedAdmin(admin.ModelAdmin):
    list_display = ("user", "review")
    list_filter = ("user", "review")
    verbose_name = "Review Like"
    verbose_name_plural = "Review Likes"


@admin.register(ReviewView)
class ReviewViewAdmin(admin.ModelAdmin):
    list_display = ("user", "review")
    list_filter = ("user", "review")
    verbose_name = "Review View"
    verbose_name_plural = "Review Views"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "review", "text", "liked")
    list_filter = ("user", "review", "liked")
    search_fields = ("user__username", "review__title")
    verbose_name = "Comment"
    verbose_name_plural = "Comments"


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "comment")
    list_filter = ("user", "comment")
    verbose_name = "Comment Like"
    verbose_name_plural = "Comment Likes"
