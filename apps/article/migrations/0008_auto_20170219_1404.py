# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-19 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': '\u6807\u7b7e\u7ba1\u7406', 'verbose_name_plural': '\u6807\u7b7e\u7ba1\u7406'},
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Tags', verbose_name='\u6587\u7ae0\u6807\u7b7e'),
        ),
    ]