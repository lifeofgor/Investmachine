# Generated by Django 3.2.5 on 2021-08-18 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0022_alter_lkpage_data_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 6, 33, 9, 572726, tzinfo=utc), verbose_name='Дата'),
        ),
    ]
