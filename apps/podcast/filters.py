from datetime import datetime, timedelta


def filter_comments(queryset, filter_type):
    if filter_type == "this_week":
        start_date = datetime.now().date() - timedelta(days=7)
        end_date = datetime.now().date() + timedelta(days=1)
        return queryset.filter(created_at__range=[start_date, end_date]).order_by("created_at")
    elif filter_type == "recent":
        return queryset.order_by("-created_at")
    elif filter_type == "popular":
        return sorted(queryset, key=lambda obj: obj.get_like_dislike_count()["total"], reverse=True)
    return queryset.order_by("created_at")
