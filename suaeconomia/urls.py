#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from suaeconomia import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suaeconomia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index_suaeconomia'),
    url(r'^lista/', include('lista.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
