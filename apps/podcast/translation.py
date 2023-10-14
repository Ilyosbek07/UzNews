from modeltranslation.translator import TranslationOptions, register

from apps.podcast.models import Podcast


@register(Podcast)
class PodcastTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "body")
