#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=60, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    endereco = models.CharField(max_length=60, verbose_name="Endereço")
    senha = models.CharField(max_length=60, verbose_name="Senha")

    @property
    def __str__(self):
        return self.nome

#class Empresa(models.Model):
#	pass

class Produto(models.Model):
    codBarra = models.CharField(max_length=20, verbose_name="Cod. Barra")
    descricao = models.CharField(max_length=60, verbose_name="Descrição")
    fabricante = models.CharField(max_length=60, verbose_name="Fabricante")

    @property
    def __str__(self):
        return self.descricao + ' ' +  self.fabricante

class Lista(models.Model):
    nome = models.CharField(max_length=40, verbose_name="Nome", default='Nome da Lista')
    produtos = models.ManyToManyField(Produto, related_name='lista+')
    cliente = models.ForeignKey(Cliente)

    @property
    def __str__(self):
        return self.produto.descricao + ' ' +  self.produto.fabricante


#class Listagem(models.Model):
#   lista
#   produto
#	pass
	
#class Listas(models.Model):
#	lista
#	produto = models.ManyToManyField(Produto, related_name='lista+')
#	pass
	
#class Cotacao(models.Model):
#	pass
