# Generated by Django 4.2.6 on 2023-10-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photoreport", "0002_alter_comment_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="photoreport",
            name="desc_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="desc_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="desc_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="subtitle_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Subtitle"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="subtitle_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Subtitle"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="subtitle_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Subtitle"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="photoreport",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
    ]