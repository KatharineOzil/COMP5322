# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views
from material.frontend import urls as frontend_urls
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'article/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'search$', views.search, name='search'),
    url(r'intro$', views.introduction, name='introduction'),
    url(r'archives$', views.archives, name='archives'),
    url(r'', include(frontend_urls)),
] 