# Generated by Django 3.2.5 on 2021-08-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AddField(
            model_name='comment',
            name='img_сom',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='Комментарий'),
        ),
    ]