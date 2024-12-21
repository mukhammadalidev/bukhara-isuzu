from django.contrib import admin
from .models import Characteristic,FuelType,Product,Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category',)

admin.site.register(Product,ProductAdmin)

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('weight','compacity','wheel_formula','dimensions','working_volume','wheelbase','fuel_type')

admin.site.register(Characteristic,CharacteristicAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug',)

admin.site.register(Category,CategoryAdmin)

class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(FuelType,FuelTypeAdmin)