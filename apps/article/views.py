# coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger

from models import Article, HeadInfo, Tags, pageInfo, Column
from users.models import UserProfile


class ArtHome(View):

    def get(self, request):
        article = Article.objects.filter(passed=True).order_by('-date')
        columns = Column.objects.all().order_by('date')
        headInfo = HeadInfo.objects.filter(page='home').order_by('-date')[0]
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')


        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(article, 10, request=request)
        articles = p.page(page)

        return render(request, 'index.html', {
            'articles': articles,
            'hotarts': hotArts,
            'headInfo': headInfo,
            'tags': tags,
            'user': user,
            'columns': columns
        })

class Columns(View):
    def get(self, request):
        columns = Column.objects.all().order_by('date')
        columnsAll = Column.objects.all().order_by('-date')
        headInfo = HeadInfo.objects.filter(page='column').order_by('-date')
        if headInfo:
            headInfo = HeadInfo.objects.filter(page='column').order_by('-date')[0]
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')
        artNum = columns.all().count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(columnsAll, 10, request=request)
        columnsAll = p.page(page)

        return render(request, 'column.html', {
            'hotarts': hotArts,
            'headInfo': headInfo,
            'tags': tags,
            'user': user,
            'num': artNum,
            'columns': columns,
            'columnList': columnsAll
        })


class ColumnArticle(View):
    def get(self, request, cId):
        article = Article.objects.filter(column_id=cId).order_by('-date')
        columns = Column.objects.all().order_by('date')
        column = Column.objects.get(id=cId)
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')
        artNum = article.all().count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(article, 10, request=request)
        articles = p.page(page)

        return render(request, 'colarticle.html', {
            'articles': articles,
            'hotarts': hotArts,
            'tags': tags,
            'user': user,
            'num': artNum,
            'columns': columns,
            'column': column
        })


class Tag(View):
    def get(self, request):

        tag = request.GET.get('tag', '')
        if tag:
            article = Article.objects.filter(passed=True, tags=int(tag)).order_by('-date')
            tag = Tags.objects.get(id=int(tag))
            tag.chickRate += 1
            tag.save()
        else:
            article = Article.objects.filter(passed=True).order_by('-date')
        headInfo = HeadInfo.objects.filter(page='tags').order_by('-date')
        if headInfo:
            headInfo = HeadInfo.objects.filter(page='column').order_by('-date')[0]
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        columns = Column.objects.all().order_by('date')
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')
        artNum = article.all().count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(article, 10, request=request)
        articles = p.page(page)

        return render(request, 'tags.html', {
            'tagc': tag,
            'articles': articles,
            'hotarts': hotArts,
            'headInfo': headInfo,
            'tags': tags,
            'user': user,
            'num': artNum,
            'columns': columns
        })


class Art(View):
    def get(self, request, art_id):
        art = Article.objects.get(id=art_id)
        art.chickRate += 1
        art.save()
        tags = Tags.objects.filter(art_id=art_id)

        return render(request, 'article.html', {
            'art': art,
            'tags': tags,
        })


class About(View):
    def get(self, request):
        content = pageInfo.objects.filter(type='about').order_by('-date')
        if content:
            content = pageInfo.objects.filter(type='about').order_by('-date')[0]
        headInfo = HeadInfo.objects.filter(page='about').order_by('-date')
        if headInfo:
            headInfo = HeadInfo.objects.filter(page='column').order_by('-date')[0]
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        columns = Column.objects.all().order_by('date')
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')

        return render(request, 'about.html', {
            'hotarts': hotArts,
            'tags': tags,
            'headInfo': headInfo,
            'user': user,
            'content': content,
            'columns': columns
        })


class Friend(View):
    def get(self, request):
        content = pageInfo.objects.filter(type='friends').order_by('-date')
        if content:
            content = pageInfo.objects.filter(type='friends').order_by('-date')[0]
        headInfo = HeadInfo.objects.filter(page='friends').order_by('-date')
        if headInfo:
            headInfo = HeadInfo.objects.filter(page='column').order_by('-date')[0]
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        columns = Column.objects.all().order_by('date')
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')

        return render(request, 'friend.html', {
            'hotarts': hotArts,
            'tags': tags,
            'headInfo': headInfo,
            'user': user,
            'content': content,
            'columns': columns
        })


class Search(View):
    def get(self, request):
        all_tags = []
        all_arts = []
        search_keyword = ''
        hotArts = Article.objects.filter(passed=True).order_by('-chickRate')[:7]
        columns = Column.objects.all().order_by('date')
        tags = Tags.objects.all().order_by('-chickRate')[:25]
        user = UserProfile.objects.get(username='fengxiao')

        search_keyword = request.GET.get('keywords', '')
        if search_keyword:
            all_arts = Article.objects.filter(Q(title__icontains=search_keyword)|
                        Q(overView__icontains=search_keyword))
            all_tags = Tags.objects.filter(Q(tag__icontains=search_keyword))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_arts, 10, request=request)
        articles = p.page(page)

        return render(request, 'search.html', {
            'hotarts': hotArts,
            'tags': tags,
            'user': user,
            'articles': articles,
            'all_tags': all_tags,
            'search_keyword': search_keyword,
            'columns': columns
        })


