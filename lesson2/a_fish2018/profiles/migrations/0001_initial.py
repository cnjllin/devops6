# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 08:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(blank=True, default=b'', max_length=11)),
                ('role', models.CharField(blank=True, choices=[(b'0', '\u65e0'), (b'1', '\u603b\u76d1'), (b'2', '\u7ecf\u7406'), (b'3', '\u7814\u53d1')], default=b'0', max_length=1)),
                ('note', models.CharField(blank=True, default=b'', max_length=128)),
            ],
        ),
    ]