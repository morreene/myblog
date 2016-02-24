# coding:utf-8
__author__ = 'bxl'
 
from django.conf.urls import url
 
urlpatterns = [
    url(r'^$', 'blog.views.home'),
    url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'^(?P<tag_name>\w+)/$', 'blog.views.get_articles', name='get_articles'),
]