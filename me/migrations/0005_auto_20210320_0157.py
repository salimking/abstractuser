# Generated by Django 3.1.7 on 2021-03-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0004_auto_20210320_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]