# Generated by Django 3.1.7 on 2021-03-19 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_auto_20210320_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='ph',
            new_name='phone',
        ),
    ]
