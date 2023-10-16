# Generated by Django 4.2.6 on 2023-10-16 10:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(default='', verbose_name='Slug')),
                ('desc', ckeditor.fields.RichTextField(default='', verbose_name='Description')),
                ('desc_uz', ckeditor.fields.RichTextField(default='', null=True, verbose_name='Description')),
                ('desc_ru', ckeditor.fields.RichTextField(default='', null=True, verbose_name='Description')),
                ('desc_en', ckeditor.fields.RichTextField(default='', null=True, verbose_name='Description')),
                ('style_type', models.CharField(choices=[('Style 1', 'Style 1'), ('Style 2', 'Style 2'), ('Style 3', 'Style 3')], default='Style 1', max_length=55, verbose_name='Style Type')),
                ('status', models.CharField(choices=[('published', 'Published'), ('in_moderation', 'In Moderation'), ('draft', 'Draft')], default='draft', max_length=55, verbose_name='Status')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('subtitle_uz', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('subtitle_ru', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('subtitle_en', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('video_url', models.URLField(verbose_name='Video Url')),
                ('is_main', models.BooleanField(default=False, verbose_name='Is Main')),
                ('tag', models.ManyToManyField(related_name='interview_tag', to='common.tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Interview',
                'verbose_name_plural': 'Interviews',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='interview/comment_images', verbose_name='Image')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('liked', models.IntegerField(default=0, verbose_name='Liked')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interview', verbose_name='Interview')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interview.comment', verbose_name='Parent Comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
