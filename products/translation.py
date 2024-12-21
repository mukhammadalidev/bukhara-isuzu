from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category,Characteristic,FuelType

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Characteristic)
class CharacteristicTranslationOptions(TranslationOptions):
    fields = ('weight','compacity','wheel_formula','dimensions','working_volume','wheelbase','fuel_type')


@register(FuelType)
class FuelTypeTranslationOptions(TranslationOptions):
    fields= ('name',)


