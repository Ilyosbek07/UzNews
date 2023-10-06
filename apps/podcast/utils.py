from .choices import PreferenceStatusChoices

def perform_liked(profile, content, UserContentPreferenceModel):
    user_preference = UserContentPreferenceModel.objects.filter(
        profile = profile, content = content
    )
    if user_preference.exists():
        user_preference = user_preference.first()
        if user_preference.status == PreferenceStatusChoices.LIKED:
            user_preference.status = PreferenceStatusChoices.NEUTRAL
            content.like_count -= 1
        elif user_preference.status == PreferenceStatusChoices.DISLIKED:
            user_preference.status = PreferenceStatusChoices.LIKED
            content.like_count += 1
            content.dislike_count -= 1
        else:
            user_preference.status = PreferenceStatusChoices.LIKED
            content.like_count += 1
    else:
        user_preference = UserContentPreferenceModel.objects.create(
            profile = profile, content = content,
            status = PreferenceStatusChoices.LIKED
        )
        content.like_count += 1
    user_preference.save()
    content.save()

def perform_disliked(profile, content, UserContentPreferenceModel):
    user_preference = UserContentPreferenceModel.objects.filter(
        profile = profile, content = content
    )
    if user_preference.exists():
        user_preference = user_preference.first()
        if user_preference.status == PreferenceStatusChoices.DISLIKED:
            user_preference.status = PreferenceStatusChoices.NEUTRAL
            content.dislike_count -= 1
        elif user_preference.status == PreferenceStatusChoices.LIKED:
            user_preference.status = PreferenceStatusChoices.DISLIKED
            content.dislike_count += 1
            content.like_count -= 1
        else:
            user_preference.status = PreferenceStatusChoices.DISLIKED
            content.dislike_count += 1
    else:
        user_preference = UserContentPreferenceModel(
            profile = profile, content = content,
            status = PreferenceStatusChoices.DISLIKED
        )
        content.dislike_count += 1
    user_preference.save()
    content.save()
    