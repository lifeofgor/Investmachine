# Generated by Django 3.2.5 on 2021-08-05 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0010_lkpage_data_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 16, 5, 15, 246333), verbose_name='Дата'),
        ),
    ]
