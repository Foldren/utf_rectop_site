# Generated by Django 3.2.3 on 2022-08-19 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0030_auto_20220819_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filial',
            name='status',
            field=models.IntegerField(choices=[(0, 'Подгружен с сервиса'), (1, 'Подключен'), (2, 'Приостановлен')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='platformaccount',
            name='last_date_load_filials',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 23, 45, 10, 484408)),
        ),
        migrations.AlterField(
            model_name='platformaccount',
            name='last_date_load_reviews',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 23, 45, 10, 484340)),
        ),
    ]
