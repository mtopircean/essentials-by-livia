# Generated by Django 3.2.22 on 2023-11-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_appuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpromotion',
            name='expires_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
