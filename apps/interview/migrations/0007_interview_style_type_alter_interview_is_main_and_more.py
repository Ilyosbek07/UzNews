# Generated by Django 4.2.6 on 2023-10-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_interview_desc_en_interview_desc_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='style_type',
            field=models.CharField(choices=[('Style 1', 'Style 1'), ('Style 2', 'Style 2'), ('Style 3', 'Style 3')], default='Style 1', max_length=55, verbose_name='Style Type'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='is_main',
            field=models.BooleanField(default=False, unique='interview', verbose_name='Is Main'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='slug',
            field=models.SlugField(default='', verbose_name='Slug'),
        ),
    ]
