# Generated by Django 3.2.5 on 2021-08-06 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0014_alter_lkpage_data_page'),
        ('forum', '0002_auto_20210806_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='lkpage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='LK.lkpage', verbose_name='пост'),
        ),
    ]