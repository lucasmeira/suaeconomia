# -*- coding: utf-8 -*-
from django.forms import ModelForm
from lista.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['id','describ']
