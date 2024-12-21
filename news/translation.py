from modeltranslation.translator import register, TranslationOptions
from .models import News,Aksiya

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Aksiya)
class AksiyaTranslationOption(TranslationOptions):
    fields = ('title','description',)