from apps.interview.choices import LikeStatusChoices


def perform_liked(profile, content, InterviewLike):
    user_preference = InterviewLike.objects.filter(
        profile=profile, content=content
    )
    if user_preference.exists():
        user_preference = user_preference.first()
        if user_preference.status == LikeStatusChoices.LIKED:
            user_preference.status = LikeStatusChoices.NEUTRAL
            content.like_count -= 1
        elif user_preference.status == LikeStatusChoices.DISLIKED:
            user_preference.status = LikeStatusChoices.LIKED
            content.like_count += 1
            content.dislike_count -= 1
        else:
            user_preference.status = LikeStatusChoices.LIKED
            content.like_count += 1
    else:
        user_preference = InterviewLike.objects.create(
            profile=profile, content=content,
            status=LikeStatusChoices.LIKED
        )
        content.like_count += 1
    user_preference.save()
    content.save()


def perform_disliked(profile, content, InterviewLike):
    user_preference = InterviewLike.objects.filter(
        profile=profile, content=content
    )
    if user_preference.exists():
        user_preference = user_preference.first()
        if user_preference.status == LikeStatusChoices.DISLIKED:
            user_preference.status = LikeStatusChoices.NEUTRAL
            content.dislike_count -= 1
        elif user_preference.status == LikeStatusChoices.LIKED:
            user_preference.status = LikeStatusChoices.DISLIKED
            content.dislike_count += 1
            content.like_count -= 1
        else:
            user_preference.status = LikeStatusChoices.DISLIKED
            content.dislike_count += 1
    else:
        user_preference = InterviewLike(
            profile=profile, content=content,
            status=LikeStatusChoices.DISLIKED
        )
        content.dislike_count += 1
    user_preference.save()
    content.save()
