# Generated by Django 3.2.22 on 2023-10-30 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addproduct',
            old_name='created_on',
            new_name='expires_on',
        ),
    ]
