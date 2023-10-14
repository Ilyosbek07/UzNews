# Generated by Django 4.2.6 on 2023-10-07 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="PhotoReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("slug", models.SlugField(default="", verbose_name="Slug")),
                ("desc", models.TextField(verbose_name="Description")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "subtitle",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Subtitle"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("published", "Published"),
                            ("in_moderation", "In Moderation"),
                            ("draft", "Draft"),
                        ],
                        max_length=16,
                        null=True,
                        verbose_name="Status",
                    ),
                ),
                ("liked", models.IntegerField(default=0, verbose_name="Liked")),
                ("views", models.IntegerField(default=0, verbose_name="Views")),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
                (
                    "tag",
                    models.ManyToManyField(
                        null=True, to="photoreport.tag", verbose_name="Tags"
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo Report",
                "verbose_name_plural": "Photo Reports",
            },
        ),
        migrations.CreateModel(
            name="GalleryImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        upload_to="photoreport/gallery_images", verbose_name="Image"
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Order"
                    ),
                ),
                ("is_main", models.BooleanField(default=False, verbose_name="Is Main")),
                (
                    "photo_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gallery_image",
                        to="photoreport.photoreport",
                        verbose_name="Photo report",
                    ),
                ),
            ],
            options={
                "verbose_name": "Gallery Image",
                "verbose_name_plural": "Gallery Images",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        null=True,
                        upload_to="photoreport/comment_images",
                        verbose_name="Image",
                    ),
                ),
                ("text", models.TextField(blank=True, null=True, verbose_name="Text")),
                ("liked", models.IntegerField(default=0, verbose_name="Liked")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="photoreport.comment",
                        verbose_name="Parent Comment",
                    ),
                ),
                (
                    "photo_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="photoreport.photoreport",
                        verbose_name="Photo Report",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.CreateModel(
            name="PhotoReportView",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "photo_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_report_view",
                        to="photoreport.photoreport",
                        verbose_name="Photo report",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_report_view",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo report view",
                "verbose_name_plural": "Photo report views",
                "unique_together": {("user", "photo_report")},
            },
        ),
        migrations.CreateModel(
            name="PhotoReportLiked",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "photo_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_report_liked",
                        to="photoreport.photoreport",
                        verbose_name="Photo report",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_report_liked",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo report like",
                "verbose_name_plural": "Photo report likes",
                "unique_together": {("user", "photo_report")},
            },
        ),
        migrations.CreateModel(
            name="CommentLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_like",
                        to="photoreport.comment",
                        verbose_name="Comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_like",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment like",
                "verbose_name_plural": "Comment likes",
                "unique_together": {("user", "comment")},
            },
        ),
    ]
