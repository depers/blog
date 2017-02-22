# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-19 12:22
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20170219_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassArticle',
            fields=[
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5ba1\u6838',
                'proxy': True,
                'verbose_name_plural': '\u6587\u7ae0\u5ba1\u6838',
            },
            bases=('article.article',),
        ),
        migrations.CreateModel(
            name='PassedArticle',
            fields=[
            ],
            options={
                'verbose_name': '\u5df2\u5ba1\u6838\u6587\u7ae0',
                'proxy': True,
                'verbose_name_plural': '\u5df2\u5ba1\u6838\u6587\u7ae0',
            },
            bases=('article.article',),
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u6587\u7ae0\u64b0\u5199', 'verbose_name_plural': '\u6587\u7ae0\u64b0\u5199'},
        ),
        migrations.AlterField(
            model_name='article',
            name='garagraph',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6bb5\u843d\u6587\u7ae0'),
        ),
        migrations.AlterField(
            model_name='headinfo',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u9875\u5934\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='pageinfo',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9'),
        ),
    ]