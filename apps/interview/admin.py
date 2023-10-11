from django.contrib import admin

from apps.interview.models import Interview


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_main")
    list_filter = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
