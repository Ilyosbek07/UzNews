# Generated by Django 4.2.6 on 2023-10-07 12:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Description'),
        ),
    ]