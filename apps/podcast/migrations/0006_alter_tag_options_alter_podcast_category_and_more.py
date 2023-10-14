# Generated by Django 4.2.6 on 2023-10-13 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_category'),
        ('podcast', '0005_comment_commentcomplaint_profilepodcastcommentlike_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='podcast',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to='common.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
