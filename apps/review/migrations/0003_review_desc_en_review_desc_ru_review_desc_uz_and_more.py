# Generated by Django 4.2.6 on 2023-10-10 17:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="desc_en",
            field=ckeditor.fields.RichTextField(
                default="", null=True, verbose_name="Description"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="desc_ru",
            field=ckeditor.fields.RichTextField(
                default="", null=True, verbose_name="Description"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="desc_uz",
            field=ckeditor.fields.RichTextField(
                default="", null=True, verbose_name="Description"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="subtitle_en",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Subtitle"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="subtitle_ru",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Subtitle"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="subtitle_uz",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Subtitle"
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="review",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="review",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
    ]