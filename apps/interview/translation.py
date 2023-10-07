from apps.interview.models import Interview, InterviewTag
from modeltranslation.translator import TranslationOptions, register


@register(Interview)
class InterviewTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'desc')


@register(InterviewTag)
class InterviewTagTranslationOptions(TranslationOptions):
    fields = ('name',)
