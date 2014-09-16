#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
	#return HttpResponse("Home page Index")
	return render(request, 'suaeconomia/index.html')
