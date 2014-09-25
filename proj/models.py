#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

class Cliente(models.Model):
	nome = models.CharField(max_length=60, verbose_name="Nome")
	email = models.EmailField(verbose_name="E-mail")
	endereco = models.CharField(max_length=60, verbose_name="Endereço")
	
class Empresa(models.Model):
	pass

class Produto(models.Model):
	#descricao
	#codBarra
	pass
	
class Lista(models.Model):
	#listagem
	#produtos
	pass

class Listagem(models.Model):
	#lista
	#produto
	pass
	
class Listas(models.Model):
	#lista
	#cliente
	pass
	
class Cotacao(models.Model):
	pass
	
