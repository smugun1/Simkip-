# Generated by Django 4.0.4 on 2022-07-31 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mogoon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='crop',
            new_name='crop_data',
        ),
    ]
