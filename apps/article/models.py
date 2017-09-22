# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.


class Column(models.Model):
    name = models.CharField(verbose_name="专栏名称", max_length=20, default='')
    overView = models.TextField(verbose_name="文章概述", default='')
    date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '博客专栏'
        verbose_name_plural = verbose_name

    def get_art_nums(self):
        return self.article_set.all().count()
    get_art_nums.short_description = "文章数"

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, default='', verbose_name='文章标题')
    column = models.ForeignKey(Column, verbose_name="所属专栏", null=True)
    date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    author = models.CharField(max_length=20, default='', verbose_name='作者')
    chickRate = models.IntegerField(default=0, verbose_name='点击率')
    overView = models.TextField(verbose_name="文章概述", default='')
    garagraph = UEditorField(verbose_name='段落文章', width=950, height=300, imagePath="article/ueditor/",
                          filePath="article/ueditor/", default='')
    passed = models.BooleanField(verbose_name="是否审核通过", default=False)

    class Meta:
        verbose_name = '文章撰写'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def go_to(self):
        from django.utils.safestring import mark_safe
        url = "/blog/Article/%d/"%(self.id)
        return mark_safe("<a href="+url+">跳转</a>")
    go_to.short_description = "跳转"


class Tags(models.Model):
    tag = models.CharField(max_length=50, default='', verbose_name='文章标签')
    chickRate = models.IntegerField(default=0, verbose_name='点击率')
    art = models.ForeignKey(Article, verbose_name='文章id', null=True)
    date = models.DateTimeField(default=datetime.now, verbose_name='时间')

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name

    def get_art_nums(self):
        return self.art.title
    get_art_nums.short_description = "文章名称"

    def __unicode__(self):
        return self.tag


class HeadInfo(models.Model):
    page = models.CharField(choices=(('home', '主页'), ('column', '博客专栏'), ('tags', '标签'),\
                            ('about', '关于'), ('friends', '朋友圈')), max_length=10, verbose_name='发布页面')
    content = UEditorField(verbose_name='页头内容', width=1200, height=300, imagePath="headinfo/ueditor/",
                          filePath="headinfo/ueditor/", default='')
    date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '页头信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.page


class pageInfo(models.Model):
    type = models.CharField(choices=(('about', '关于'), ('friends', '朋友圈')), max_length=10, verbose_name='发布页面')
    content = UEditorField(verbose_name='内容', width=1200, height=300, imagePath="pageinfo/ueditor/",
                          filePath="pageinfo/ueditor/", default='')
    date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '页面内容'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.type













