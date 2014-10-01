#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from proj.models import Produto
from proj.models import Lista


class ProdutoForm(forms.Form):
    class Meta:
        model = Produto

class ListaForm(forms.Form):
    class Meta:
        model = Lista