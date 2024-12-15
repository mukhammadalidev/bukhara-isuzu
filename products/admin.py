from django.contrib import admin
from .models import Characteristic,FuelType,Product,Category
# Register your models here.
admin.site.register(Characteristic)
admin.site.register(FuelType)
admin.site.register(Category)
admin.site.register(Product)