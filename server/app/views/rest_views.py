# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Event 
import json

# rest (AJAX HTTPS requests) for AJAX only
@csrf_exempt
def createEvent(request):
	print "type " + str(type(request.body))
	data = json.loads(request.body)
	title = data[u'title']
	desc = data[u'desc']
	rsvp = data[u'rsvp']

	newEvent = Event(event_title= title, description = desc, rsvp = rsvp)
	newEvent.save()
	return HttpResponse("response")