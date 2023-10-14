from django.contrib import admin

from .models import BreakingNews, News, NewsCancelReason, NewsCategory


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "type")
    list_filter = ("status", "type")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


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
