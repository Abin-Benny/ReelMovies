# Generated by Django 3.2.4 on 2021-07-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_details_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
