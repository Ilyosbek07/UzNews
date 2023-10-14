from apps.interview.models import Interview
from modeltranslation.translator import TranslationOptions, register


@register(Interview)
class InterviewTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "desc")

