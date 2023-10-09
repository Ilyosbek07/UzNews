# Generated by Django 4.2.6 on 2023-10-09 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0008_alter_newsview_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newscomment",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="news_comment_to_news",
                to="news.news",
            ),
        ),
    ]
