# Generated by Django 4.2.6 on 2023-10-16 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='podcasts', to='users.profile', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to='podcast.category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='tags',
            field=models.ManyToManyField(related_name='podcasts', to='podcast.tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='commentcomplaint',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='podcast.comment', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='commentcomplaint',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='podcast_comment_complaints', to='users.profile', verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='podcast.comment', verbose_name='Parent'),
        ),
        migrations.AddField(
            model_name='comment',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='podcast.podcast', verbose_name='Podcast'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='podcast_comments', to='users.profile', verbose_name='Owner'),
        ),
    ]
