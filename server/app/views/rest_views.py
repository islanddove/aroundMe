# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event 

# rest (AJAX HTTPS requests)
@csrf_exempt
def createEvent(request):

	print "GOT HERE"
	title = request.POST["title"]
	desc = request.POST["desc"]
	rsvp = request.POST["rsvp"]

	newEvent = Event(event_title= title, description = desc, rsvp = rsvp)
	newEvent.save()
	return HttpResponse("response")
