# Generated by Django 5.1.4 on 2024-12-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_description_en_news_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
