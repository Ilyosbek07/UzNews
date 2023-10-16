# Generated by Django 4.2.6 on 2023-10-16 10:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photoreport/comment_images', verbose_name='Image')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('liked', models.IntegerField(default=0, verbose_name='Liked')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Comment like',
                'verbose_name_plural': 'Comment likes',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='photoreport/gallery_images', verbose_name='Image')),
                ('order', models.PositiveIntegerField(blank=True, null=True, verbose_name='Order')),
                ('is_main', models.BooleanField(default=False, verbose_name='Is Main')),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
        migrations.CreateModel(
            name='PhotoReport',
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
                ('subtitle', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('subtitle_uz', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('subtitle_ru', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('subtitle_en', models.CharField(max_length=255, null=True, verbose_name='Subtitle')),
                ('status', models.CharField(choices=[('published', 'Published'), ('in_moderation', 'In Moderation'), ('draft', 'Draft')], max_length=16, null=True, verbose_name='Status')),
                ('liked', models.IntegerField(default=0, verbose_name='Liked')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('is_prime', models.BooleanField(default=False, verbose_name='Is prime')),
            ],
            options={
                'verbose_name': 'Photo Report',
                'verbose_name_plural': 'Photo Reports',
            },
        ),
        migrations.CreateModel(
            name='PhotoReportLiked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Photo report like',
                'verbose_name_plural': 'Photo report likes',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='PhotoReportView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_report_view', to='photoreport.photoreport', verbose_name='Photo report')),
            ],
            options={
                'verbose_name': 'Photo report view',
                'verbose_name_plural': 'Photo report views',
            },
        ),
    ]
