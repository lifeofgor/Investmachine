# Generated by Django 3.2.5 on 2021-08-23 03:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0029_auto_20210822_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AlterModelOptions(
            name='lkpage',
            options={'verbose_name': 'Запись в форум', 'verbose_name_plural': 'Записи в форум'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Личный профиль', 'verbose_name_plural': 'Личные профили'},
        ),
        migrations.AlterField(
            model_name='lkpage',
            name='data_page',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 23, 3, 24, 57, 288634, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='lkpage',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='lkpage', to='LK.Tag'),
        ),
    ]
