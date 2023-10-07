from modeltranslation.translator import TranslationOptions, register

from apps.photoreport.models import PhotoReport


@register(PhotoReport)
class InterviewTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "desc")
