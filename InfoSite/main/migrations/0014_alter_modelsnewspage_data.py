# Generated by Django 3.2.5 on 2021-07-28 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_modelsnewspage_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsnewspage',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 3, 9, 47, 749816), verbose_name='Дата'),
        ),
    ]