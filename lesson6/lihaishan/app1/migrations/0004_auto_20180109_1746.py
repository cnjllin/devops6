# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180109_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='fansnum',
            field=models.IntegerField(default=0, verbose_name='\u7c89\u4e1d\u91cf'),
        ),
        migrations.AddField(
            model_name='author',
            name='income',
            field=models.IntegerField(default=0, verbose_name='\u6536\u5165'),
        ),
        migrations.AlterField(
            model_name='book',
            name='clicknum',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='sellnum',
            field=models.IntegerField(default=0, verbose_name='\u9500\u91cf'),
        ),
    ]
