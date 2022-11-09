# Generated by Django 3.2.3 on 2022-08-05 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0019_auto_20220804_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_date_load_2gis',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 19, 27, 30, 918140)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_date_load_google',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 19, 27, 30, 918096)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_date_load_yandex',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 19, 27, 30, 918168)),
        ),
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Не прочитано'), (1, 'Прочитано'), (2, 'С ответом')], default=0),
        ),
    ]
