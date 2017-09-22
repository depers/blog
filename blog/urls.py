# coding=utf-8
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from blog.settings import MEDIA_ROOT, STATIC_ROOT
from django.views.static import serve


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^blog/', include('article.urls')),

    url(r'^ueditor/',include('DjangoUeditor.urls' )),

    url(r'^media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),

    # 将debug修改为False时，我们需要配置static
    url(r'^static/(?P<path>.*)', serve, {'document_root': STATIC_ROOT}),

]

# 全局404. 500页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
