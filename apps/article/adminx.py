# -*- coding: utf-8 -*-
__author__ = 'fengxiao'
__date__ = '2017/2/18 18:21'
import xadmin
from models import Article, HeadInfo, pageInfo, PassArticle, PassedArticle, Tags, Column
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "FengXiao博客系统"
    site_footer = "FengXiao博客系统"
    # menu_style = "accordion"


class ArticleAdmin(object):
    list_display = ['title', 'tags', 'author', 'chickRate', 'date', 'go_to']
    search_fields = ['title', 'tags', 'author']
    list_filter = ['title', 'tags', 'author', 'chickRate', 'date']
    model_icon = 'fa fa-eyedropper'
    exclude = ['passed']
    style_fields = {"garagraph": "ueditor"}



class PassArticleAdmin(object):
    list_display = ['title', 'tags', 'author', 'chickRate', 'passed', 'date', 'go_to']
    search_fields = ['title', 'tags', 'author']
    list_filter = ['title', 'tags', 'author', 'chickRate', 'date']
    model_icon = 'fa fa-graduation-cap'
    list_editable = ['passed']

    style_fields = {"garagraph": "ueditor"}

    # 对课程菜单的列表页面数据进行过滤；
    def queryset(self):
        qs = super(PassArticleAdmin, self).queryset()
        qs = qs.filter(passed = False)
        return qs


class PassedArticleAdmin(object):
    list_display = ['title', 'tags', 'author', 'chickRate', 'passed', 'date', 'go_to']
    search_fields = ['title', 'tags', 'author']
    list_filter = ['title', 'tags', 'author', 'chickRate', 'date']
    model_icon = 'fa fa-paper-plane'
    list_editable = ['passed']
    style_fields = {"garagraph": "ueditor"}

    # 对课程菜单的列表页面数据进行过滤；
    def queryset(self):
        qs = super(PassedArticleAdmin, self).queryset()
        qs = qs.filter(passed = True)
        return qs


class HeadInfoAdmin(object):
    list_display = ['page', 'content', 'date']
    search_fields = ['page', 'content']
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
    # relfield_style = 'fk-ajax'


class ColumnAdmin(object):
    list_display = ['name', 'get_art_nums', 'date']
    search_fields = ['name']
    list_filter = ['name', 'date']
    module_icon = 'fa fa-archive'
    ordering = ['date']
    # relfield_style = 'fk-ajax'

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(PassArticle, PassArticleAdmin)
xadmin.site.register(PassedArticle, PassedArticleAdmin)
xadmin.site.register(HeadInfo, HeadInfoAdmin)
xadmin.site.register(pageInfo, PageInfoAmdin)
xadmin.site.register(Tags, TagsAmdin)
xadmin.site.register(Column, ColumnAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)