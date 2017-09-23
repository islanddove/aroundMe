from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Event 

# main (initial HTTPS Request) for rendering templates only

def index(request):
	return render(request,'app/aroundMeFront.html')

def login_page(request):
	return render(request, 'app/login.html')

def event_page(request):
	return render(request, 'app/eventpage.html')