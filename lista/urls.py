#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from lista import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
