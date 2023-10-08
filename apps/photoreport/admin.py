from django.contrib import admin
from .models import (
    Tag,
    PhotoReport,
    PhotoReportLiked,
    PhotoReportView,
    GalleryImage,
    Comment,
    CommentLike,
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    verbose_name = "Tag"
    verbose_name_plural = "Tags"


@admin.register(PhotoReport)
class PhotoReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'author', 'status', 'liked', 'views')
    list_filter = ('status', 'liked', 'views', 'author', 'tag')
    search_fields = ('title', 'subtitle', 'author__username')
    verbose_name = "Photo Report"
    verbose_name_plural = "Photo Reports"
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PhotoReportLiked)
class PhotoReportLikedAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo_report')
    list_filter = ('user', 'photo_report')
    verbose_name = "Photo Report Like"
    verbose_name_plural = "Photo Report Likes"


@admin.register(PhotoReportView)
class PhotoReportViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo_report')
    list_filter = ('user', 'photo_report')
    verbose_name = "Photo Report View"
    verbose_name_plural = "Photo Report Views"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('photo_report', 'image', 'order', 'is_main')
    list_filter = ('photo_report', 'is_main')
    search_fields = ('photo_report__title',)
    verbose_name = "Gallery Image"
    verbose_name_plural = "Gallery Images"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo_report', 'text', 'liked')
    list_filter = ('user', 'photo_report', 'liked')
    search_fields = ('user__username', 'photo_report__title')
    verbose_name = "Comment"
    verbose_name_plural = "Comments"


@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')
    list_filter = ('user', 'comment')
    verbose_name = "Comment Like"
    verbose_name_plural = "Comment Likes"
