# -*- coding:utf-8 -*-

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views
from material.frontend import urls as frontend_urls
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'article/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'category/(?P<id>\d+)/$', views.category, name='category'),
    url(r'search$', views.search, name='search'),
    url(r'intro$', views.intro, name='intro'),
    url(r'archives$', views.archives, name='archives'),
    url(r'', include(frontend_urls)),
    url(r'admin/', include(admin.site.urls)),
    url(r'404$', views.page_not_found, name='404'),
    url(r'500$', views.page_error, name='500'),
#    url(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),
] 
urlpatterns += staticfiles_urlpatterns()
