# Generated by Django 3.2.22 on 2023-11-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_favouriteselection'),
    ]

    operations = [
        migrations.AddField(
            model_name='favouriteselection',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]