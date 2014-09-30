from django import forms
from proj.models import Lista

class ListaForm(forms.Form):
    Lista.produto