from django.contrib import admin

from apps.review.models import Category, Comment, CommentLike, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name", "slug")
    search_fields = ("name", "slug")
    verbose_name = "Podcast Category"
    verbose_name_plural = "Podcast Categories"
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "author", "liked", "view")
    list_filter = ("liked", "view", "author", "tag", "category")
    search_fields = ("title", "subtitle", "author__username")
    verbose_name = "Review"
    verbose_name_plural = "Reviews"
    prepopulated_fields = {"slug": ("title",)}


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
