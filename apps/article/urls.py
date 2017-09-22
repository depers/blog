# -*- coding: utf-8 -*-
__author__ = 'fengxiao'
__date__ = '2017/2/18 14:23'

from django.conf.urls import url

from views import ArtHome, Columns, Tag, Art, About, Friend, Search, ColumnArticle

urlpatterns = [
    url(r'^Home/$', ArtHome.as_view(), name='index'),

    url(r'^Column/$', Columns.as_view(), name='column'),

    url(r'^ColArticle/(?P<cId>\d+)/$', ColumnArticle.as_view(), name='colArticle'),

    url(r'^Tags/$', Tag.as_view(), name='tag'),

    url(r'^Article/(?P<art_id>\d+)/$', Art.as_view(), name='art'),

    url(r'^About/$', About.as_view(), name='about'),

    url(r'^Friends/$', Friend.as_view(), name='friends'),

    url(r'^Search/$', Search.as_view(), name='search'),
]