# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-11 17:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='\u4e13\u680f\u540d\u79f0')),
                ('amount', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u6570\u91cf')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2\u4e13\u680f',
                'verbose_name_plural': '\u535a\u5ba2\u4e13\u680f',
            },
        ),
    ]
