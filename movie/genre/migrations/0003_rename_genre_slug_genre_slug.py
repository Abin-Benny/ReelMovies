# Generated by Django 3.2.4 on 2021-06-30 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_rename_slug_genre_genre_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_slug',
            new_name='slug',
        ),
    ]
