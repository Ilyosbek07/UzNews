# Generated by Django 4.2.6 on 2023-10-16 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contentview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='contentreport',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_comment_user', to='contenttypes.contenttype', verbose_name='Content Report'),
        ),
        migrations.AddField(
            model_name='contentreport',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_report', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='contentlike',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_like', to='contenttypes.contenttype', verbose_name='Content like'),
        ),
        migrations.AddField(
            model_name='contentlike',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_like_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='contentcomment',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_comment', to='contenttypes.contenttype', verbose_name='Content comment'),
        ),
        migrations.AddField(
            model_name='contentcomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_comment_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterUniqueTogether(
            name='contentview',
            unique_together={('content_type', 'object_id', 'device_id'), ('content_type', 'object_id', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='contentreport',
            unique_together={('content_type', 'object_id', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='contentlike',
            unique_together={('content_type', 'object_id', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='contentcomment',
            unique_together={('content_type', 'object_id', 'user')},
        ),
    ]
