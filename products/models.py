from django.db import models
from datetime import datetime
from django.utils.text import slugify

class FuelType(models.Model):
    name = models.CharField(max_length=100)

class Characteristic(models.Model):
    weight = models.CharField(max_length=100)
    compacity = models.CharField(max_length=100)
    wheel_formula = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=100)
    working_volume = models.CharField(max_length=10)
    wheelbase = models.CharField(max_length=100)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255, default='yuk avtomobile')
    image = models.ImageField(upload_to='category/')
    slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

   
      

    def __str__(self):
        return self.title


