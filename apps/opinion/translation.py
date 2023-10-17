from modeltranslation.translator import TranslationOptions, register

from apps.opinion.models import Opinion


@register(Opinion)
class OpinionTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "body")
