from django.contrib import admin
from proj.models import Produto
from proj.models import Cliente
from proj.models import Lista

# Register your models here.
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Lista)