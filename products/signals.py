# products/signals.py

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product

@receiver(pre_save, sender=Product)
def product_pre_save(sender, instance, **kwargs):
    # Signalning bajarilishi
    pass
