#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
	
class Categoria(models.Model):
	describ = models.CharField(max_length=30, verbose_name="Categoria")
	
	def __unicode__(self):
		return self.describ

class Produto(models.Model):
	describ = models.CharField(max_length=30, verbose_name="Produto")
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.describ
		
class Lista(models.Model):
	produtos = models.ManyToManyField(Produto, related_name='prod+')
