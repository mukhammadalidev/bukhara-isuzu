# products/apps.py

from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        import products.translation  # translation.py faylini ready() metodida import qilish
