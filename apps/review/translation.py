from modeltranslation.translator import TranslationOptions, register

from apps.review.models import Review


@register(Review)
class InterviewTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "desc")
