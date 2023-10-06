from django.contrib import admin

from apps.interview.models import Interview, InterviewTag


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_main')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(InterviewTag)
class InterviewTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
