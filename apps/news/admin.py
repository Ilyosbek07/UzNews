from django.contrib import admin

from .models import (BreakingNews, News, NewsCancelReason, NewsCategory,
                     NewsComment, NewsCommentReport, NewsLike, NewsTag,
                     NewsView)


@admin.register(NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "type")
    list_filter = ("status", "type")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewsLike)
class NewsLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "news")


@admin.register(NewsComment)
class NewsCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "news", "text")


@admin.register(NewsCommentReport)
class NewsCommentReportAdmin(admin.ModelAdmin):
    list_display = ("user", "comment")


@admin.register(NewsView)
class NewsViewAdmin(admin.ModelAdmin):
    list_display = ("user", "news")


@admin.register(BreakingNews)
class BreakingNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "news", "expire_time")
    list_filter = ("expire_time",)
    search_fields = ("title",)


@admin.register(NewsCancelReason)
class NewsCancelReasonAdmin(admin.ModelAdmin):
    list_display = ("user", "news")
    list_filter = ("news",)
    search_fields = ("news", "user")
