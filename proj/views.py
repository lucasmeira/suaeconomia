#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import get_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.forms.models import modelformset_factory
from proj.models import Lista, Produto
from proj.forms import ProdutoForm

#from lista.models import Categoria
#from lista.forms import CategoriaForm


# Create your views here.
def index(request):
    return render(request, 'proj/index.html')


# Fluxo principal da criação de lista
# Loga
def login(request):
    return render(request, 'proj/login.html')


# Se não existe usuário cria o cliente
# Página de cadastro do cliente
def cadastrarCliente(request):
    return render(request, 'proj/cadastrarcliente.html')


# Após logar é mostrado a lista do cliente com opção
# para add produto
def painelCliente(request):
    return render(request, 'proj/painelcliente.html')


# Página de cadastro de lista
def criarLista(request):
    ListaForm = modelformset_factory(Lista)
    # Se for passado dados via POST
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():  # se o formulario for valido
            form.save()      # cria um novo usuario a partir dos dados enviados
            #return HttpResponseRedirect("/proj/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            #return render(request, "painelcliente.html", {"form: form"})
            formset = ListaForm()
        return render_to_response("painelcliente.html", {"form":form})
    # se nenhuma informação for passada, exibe a página de cadastro com o formulario
    #return render(request, "painelcliente.html", {"form": })


#  Adiciona o produto a lista do cliente
def addProdLista(request):
    ListaForm = modelformset_factory(Lista)
    if request.method == 'POST':
        form = ListaForm(request.POST)
        object_list = Lista.objects.all()
    return render_to_response('proj/addprodutolista.html', {"form": form,
                                                            "object_list": object_list})


# Redirects views
def redirect_home(request):
    return HttpResponseRedirect('/proj')