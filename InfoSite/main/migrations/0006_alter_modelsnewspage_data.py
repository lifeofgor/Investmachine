# Generated by Django 3.2.5 on 2021-07-20 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210720_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsnewspage',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 21, 0, 49, 19, 17005), verbose_name='Дата'),
        ),
    ]