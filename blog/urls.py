# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import PostListView, PostDetailView, CommentView, TagView, IndexView

urlpatterns = patterns('blog.views',
    url(r'^$', IndexView.as_view(), name="index_view"),

    url(r'^posts/$', PostListView.as_view()),
    url(r'^posts/(?P<page>\d+)/$', PostListView.as_view(), name="post_list_view"),

    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_view"),

    url(r'^post/(?P<post_id>\d+)/comment/$', CommentView.as_view(), name='comment_view'),

    url(r'^tags/(?P<tag>.+)/$', TagView.as_view(), name='tag_view'),
    # url(r'^tags/(?P<tags>[\w\+]+)/$', TagView.as_view(), name='tag_view'),

    url(r'^search/$', 'tag_search', name='tag_search_view'),
)
