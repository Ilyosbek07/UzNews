# Generated by Django 4.2.6 on 2023-10-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='post_view_count',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Post View Count'),
        ),
    ]