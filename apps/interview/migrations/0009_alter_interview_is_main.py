# Generated by Django 4.2.6 on 2023-10-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0008_alter_interview_desc_alter_interview_desc_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Is Main'),
        ),
    ]
