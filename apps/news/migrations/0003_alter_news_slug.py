# Generated by Django 4.2.6 on 2023-10-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Slug'),
        ),
    ]
