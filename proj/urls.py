#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from proj import views

urlpatterns = patterns('',
    # urls principais
	url(r'^$', views.index, name='index'),
    url(r'login', views.login, name='login'),
    url(r'cadastrarcliente', views.cadastrarCliente, name='cadastrarcliente'),
    url(r'painelcliente', views.painelCliente, name='painelcliente'),
    url(r'addprodutolista', views.addProdLista, name='addprodutolista'),
)
