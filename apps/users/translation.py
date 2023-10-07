from modeltranslation.translator import TranslationOptions, register

from apps.users.models import Profile


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ("info", "role")
