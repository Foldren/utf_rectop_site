# Generated by Django 3.2.3 on 2022-08-05 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0020_auto_20220805_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_date_load_2gis',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 2, 24, 37, 173639)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_date_load_google',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 2, 24, 37, 173592)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_date_load_yandex',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 2, 24, 37, 173669)),
        ),
    ]
