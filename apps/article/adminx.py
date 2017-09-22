# -*- coding: utf-8 -*-
__author__ = 'fengxiao'
__date__ = '2017/2/18 18:21'
import xadmin
from models import Article, HeadInfo, pageInfo, Tags, Column
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "FengXiao博客系统"
    site_footer = "FengXiao博客系统"
    # menu_style = "accordion"

# 在一个页面组装外键信息
class TagInline(object):
    model = Tags
    extra = 0


class ArticleAdmin(object):
    list_display = ['title', 'author', 'chickRate', 'passed', 'date', 'go_to']
    search_fields = ['title', 'author']
    list_filter = ['title', 'author', 'chickRate', 'date']
    model_icon = 'fa fa-eyedropper'
    exclude = ['passed']
    style_fields = {"garagraph": "ueditor"}
    list_editable = ['passed']
    readonly_fields = ['chickRate']
    inlines = [TagInline]


class HeadInfoAdmin(object):
    list_display = ['page', 'date']
    search_fields = ['page']
    list_filter = ['page', 'content', 'date']
    model_icon = 'fa fa-heart-o'
    style_fields = {"content": "ueditor"}


class PageInfoAmdin(object):
    list_display = ['type', 'content', 'date']
    search_fields = ['type', 'content']
    list_filter = ['type', 'content', 'date']
    model_icon = 'fa fa-bell'
    style_fields = {"content": "ueditor"}


class TagsAmdin(object):
    list_display = ['tag', 'chickRate', 'get_art_nums', 'date']
    search_fields = ['tag']
    list_filter = ['tag', 'chickRate', 'date']
    model_icon = 'fa fa-bookmark'
    relfield_style = 'fk-ajax'
    readonly_fields = ['chickRate']


class ColumnAdmin(object):
    list_display = ['name', 'overView', 'get_art_nums', 'date']
    search_fields = ['name']
    list_filter = ['name', 'date']
    module_icon = 'fa fa-archive'
    ordering = ['date']
    relfield_style = 'fk-ajax'

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Column, ColumnAdmin)
xadmin.site.register(HeadInfo, HeadInfoAdmin)
xadmin.site.register(pageInfo, PageInfoAmdin)
xadmin.site.register(Tags, TagsAmdin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)