# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ['title', 'pub_date', 'content']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
