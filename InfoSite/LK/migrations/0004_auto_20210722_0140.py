# Generated by Django 3.2.5 on 2021-07-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0003_auto_20210721_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='VK',
            field=models.CharField(default='', max_length=100, verbose_name='ВК'),
        ),
        migrations.AddField(
            model_name='account',
            name='telegram',
            field=models.CharField(default='', max_length=100, verbose_name='Телеграмм'),
        ),
    ]