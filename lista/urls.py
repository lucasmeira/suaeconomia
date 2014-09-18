#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from lista import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# Categoria
	url(r'^listarcategorias', views.ListarCategorias.as_view()),
	# Produto
	url(r'^listarprodutos', views.ListarProdutos.as_view()),
	# Lista
	url(r'^mostrarlista', views.MostrarLista.as_view()),
)
