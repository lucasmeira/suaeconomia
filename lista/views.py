#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.views.generic.list_detail import object_list
#from django.views.generic.create_update import create_object, update_object, delete_object
from django.db.models import get_model
from django.shortcuts import get_object_or_404, render, redirect
from lista.models import Categoria
from django.views.generic import ListView
from lista.forms import CategoriaForm

# Create your views here.
def index(request):
	#return HttpResponse("Home page Lista")
	return render(request, 'lista/index.html')

def listar(request, model):
	#return render(request, 'lista/listar.html')
	model_object = get_model('categoria', model)
	if model_object:
		model_list = model_object.objects.all()
	else:
		raise Http404()
	
	return object_list(request, queryset=model_list)
	
class ListarCategorias(ListView):
	template_name = 'lista/listarcategorias.html'
	model = Categoria

def categoria(request):
	#if request.method == 'POST':
	#	categorias = Categoria.objects.all()[:10]
	#	form = CategoriaForm()
		#if not form.data['id'] and form.data['describ']:
		#	form.save()
		#	return HttpResponseRedirect('lista/listarcategorias')
	#else:
	#	form = CategoriaForm()
	#return render(request, 'lista/form.html', {'form': form}),
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(categoria)
	categorias = Categoria.objects.all()
	form = CategoriaForm()
	context = {
		'categorias': categorias,
		'form': form,
	}
	return render(request, 'lista/form.html', context)

class ListarProdutos(ListView):
	pass
	
class MostrarLista(ListView):
	pass
