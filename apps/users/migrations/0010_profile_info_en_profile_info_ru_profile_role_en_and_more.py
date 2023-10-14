# Generated by Django 4.2.6 on 2023-10-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_profile_info_en_remove_profile_info_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='info_en',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='profile',
            name='info_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Info'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role_en',
            field=models.CharField(choices=[('simple user', 'Simple User'), ('author', 'Author'), ('moderator', 'Moderator')], default='simple user', max_length=55, null=True, verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role_ru',
            field=models.CharField(choices=[('simple user', 'Simple User'), ('author', 'Author'), ('moderator', 'Moderator')], default='simple user', max_length=55, null=True, verbose_name='Role'),
        ),
    ]