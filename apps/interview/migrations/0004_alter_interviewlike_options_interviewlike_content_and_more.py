# Generated by Django 4.2.6 on 2023-10-07 06:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('interview', '0003_alter_interview_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interviewlike',
            options={'verbose_name': 'User Interview Like', 'verbose_name_plural': 'User Interview Likes'},
        ),
        migrations.AddField(
            model_name='interviewlike',
            name='content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='interview_like', to='interview.interview', verbose_name='Interview'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewlike',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewlike',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='interview_user_like', to='users.profile', verbose_name='Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewlike',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='interviewlike',
            name='status',
            field=models.CharField(choices=[('l', 'Liked'), ('d', 'Disliked'), ('n', 'Neutral')], max_length=10, verbose_name='Status'),
        ),
    ]
