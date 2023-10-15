from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from rest_framework import status

from apps.common.choices import LikeStatusChoices
from apps.common.models import ContentLike


def time_difference_in_words(created_time):
    numbers_dict = {
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty-one",
        22: "twenty-two",
        23: "twenty-three",
        24: "twenty-four",
        25: "twenty-five",
        26: "twenty-six",
        27: "twenty-seven",
        28: "twenty-eight",
        29: "twenty-nine",
        30: "thirty",
    }
    now = timezone.now()
    delta = (now - created_time).seconds
    if delta < 60:
        return "just now"
    elif delta < 3600:
        units = delta // 60
        if units == 1:
            return "a minute ago"
        else:
            return f"{numbers_dict[units]} minutes ago"
    elif delta < 86400:
        units = delta // 3600
        if units == 1:
            return "an hour ago"
        else:
            return f"{numbers_dict[units]} hours ago"
    elif delta < 604800:
        units = delta // 86400
        if units == 1:
            return "a day ago"
        else:
            return f"{numbers_dict[units]} days ago"
    elif delta < 2592000:
        units = delta // 604800
        if units == 1:
            return "a week ago"
        else:
            return f"{numbers_dict[units]} weeks ago"
    elif delta < 31536000:
        units = delta // 2592000
        if units == 1:
            return "a month ago"
        else:
            return f"{numbers_dict[units]} months ago"
    else:
        units = delta // 31536000
        if units == 1:
            return "a year ago"
        else:
            return f"{numbers_dict[units]} years ago"


def perform_object_liked_disliked(object_id, ObjectModel, queryset, user, liked):
    try:
        queryset.get(pk=object_id)
    except Exception as e:
        return status.HTTP_404_NOT_FOUND
    if liked:
        like_status = LikeStatusChoices.LIKED
    else:
        like_status = LikeStatusChoices.DISLIKED
    like = ContentLike.objects.filter(
        content_type=ContentType.objects.get_for_model(ObjectModel), object_id=object_id, user=user
    )
    if like.exists():
        like = like.first()
        like.status = like_status
    else:
        like = ContentLike.objects.create(
            content_type=ContentType.objects.get_for_model(ObjectModel),
            object_id=object_id,
            user=user,
            status=like_status,
        )
    like.save()
    return status.HTTP_200_OK
