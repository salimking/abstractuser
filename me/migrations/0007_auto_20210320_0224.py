# Generated by Django 3.1.7 on 2021-03-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0006_auto_20210320_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]
