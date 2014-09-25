#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import get_model
from django.views.generic import ListView
#from lista.models import Categoria
#from lista.forms import CategoriaForm

# Create your views here.
def index(request):
	return render(request, 'proj/index.html')
