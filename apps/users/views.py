# coding:utf-8
from django.shortcuts import render

# Create your views here.


def page_not_found(request):
    """
    全局404页面配置
    """
    from django.shortcuts import render_to_response
    reponse = render_to_response('404.html')
    reponse.status_code = 404
    return reponse


def page_error(request):
    """
    全局500页面配置
    """
    from django.shortcuts import render_to_response
    reponse = render_to_response('500.html')
    reponse.status_code = 500
    return reponse