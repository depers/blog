# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=50, default='', verbose_name='文章标签')
    tag_2 = models.CharField(max_length=50, default='', verbose_name="额外标签", null=True, blank=True)
    tag_3 = models.CharField(max_length=50, default='', verbose_name='其他标签', null=True, blank=True)
    chickRate = models.IntegerField(default=0, verbose_name='点击率')
    date = models.DateTimeField(default=datetime.now, verbose_name='时间')

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tag

    def get_art_nums(self):
        return self.article_set.all().count()
    get_art_nums.short_description = "文章数"


class Column(models.Model):
    name = models.CharField(verbose_name="专栏名称", max_length=20, default='')
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
    column = models.ForeignKey(Column, verbose_name="文章专栏")
    tags = models.ForeignKey(Tags, verbose_name='文章标签', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    author = models.CharField(max_length=20, default='', verbose_name='作者')
    chickRate = models.IntegerField(default=0, verbose_name='点击率')
    overView = models.TextField(verbose_name="文章概述", default='')
    garTitle = models.CharField(max_length=100, default='', verbose_name='段落标题')
    garagraph = UEditorField(verbose_name='段落文章', width=1200, height=300, imagePath="article/ueditor/",
                          filePath="article/ueditor/", default='')
    passed = models.BooleanField(verbose_name="是否审核通过", default=False)

    class Meta:
        verbose_name = '文章撰写'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</a>")
    go_to.short_description = "跳转"


class PassArticle(Article):
    """
    在xadmin中注册不同数据；
    """
    class Meta:
        verbose_name = '文章审核'
        verbose_name_plural = verbose_name
        proxy = True

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='https://www.baidu.com'>跳转</a>")
    go_to.short_description = "跳转"


class PassedArticle(Article):
    """
    在xadmin中注册不同数据；
    """
    class Meta:
        verbose_name = '已审核文章'
        verbose_name_plural = verbose_name
        proxy = True

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</a>")
    go_to.short_description = "跳转"


class HeadInfo(models.Model):
    page = models.CharField(choices=(('home', '主页'), ('archive', '存档'), ('tags', '标签'),\
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













