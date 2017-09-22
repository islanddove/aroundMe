# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
#from .models import Event 


def index(request):
    return render(request,'app/index.html')

def createEvent(request):
    return HttpResponse("response")