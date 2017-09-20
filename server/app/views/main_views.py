from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event 

# main (initial HTTPS Request)

def index(request):
	return render(request,'app/index.html')