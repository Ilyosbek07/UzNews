# Generated by Django 4.2.6 on 2023-10-10 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0015_delete_interviewtag_alter_interview_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='dislike_count',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='like_count',
        ),
        migrations.CreateModel(
            name='InterviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('l', 'Liked'), ('d', 'Disliked'), ('n', 'Neutral')], max_length=10, verbose_name='Status')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_to_interview', to='interview.interview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(verbose_name='Text')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_interview', to='interview.interview')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='interview.interviewcomment', verbose_name='Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]