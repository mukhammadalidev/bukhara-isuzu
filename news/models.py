from django.db import models
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-created_at']



class Aksiya(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='aksiya/',blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.title