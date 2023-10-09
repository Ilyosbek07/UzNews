from datetime import date, timedelta

import django_filters
from rest_framework.exceptions import ValidationError

from .models import News, NewsCategory


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", label="News Name contains")
    category = django_filters.ModelChoiceFilter(
        queryset=NewsCategory.objects.all(), field_name="category", label="Category"
    )
    date = django_filters.DateFilter(field_name="created_at", label="Date")

    this_week = django_filters.BooleanFilter(
        label="This Week",
        method="filter_this_week",
        widget=django_filters.widgets.BooleanWidget(attrs={"class": "switch"}),
    )
    all_time = django_filters.BooleanFilter(
        label="All Time",
        method="filter_all_time",
        widget=django_filters.widgets.BooleanWidget(attrs={"class": "switch"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get("this_week") and self.data.get("all_time"):
            raise ValidationError("Both 'This Week' and 'All Time' filters cannot be selected simultaneously.")

    def filter_this_week(self, queryset, name, value):
        if value:
            end_date = date.today()
            start_date = end_date - timedelta(days=7)
            return queryset.filter(created_at__range=(start_date, end_date))
        return queryset

    def filter_all_time(self, queryset, name, value):
        if value:
            return queryset.all()
        return queryset

    class Meta:
        model = News
        fields = []
