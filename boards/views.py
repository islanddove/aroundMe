from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event 
import json
from django.http import JsonResponse

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect, render

def home(request):
    events = Event.objects.all()
    return render(request, 'base.html', {'events':events})


def eventpage(request):
	return render(request, 'eventpage.html')

@csrf_exempt
def createEvent(request):

	response = {"code": 400, "message": "request failed to send"}

	try:

		data = json.loads(request.body.decode("utf-8"))

		title = str(data[u'title'])
		date = str(data[u'date'])
		time = str(data[u'time'])
		location = str(data[u'location'])
		category = str(data[u'category'])
		
		newEvent = Event(event_title= title, event_date= date, event_time= time, event_location= location, category= category)
		newEvent.save()

		response["code"] = 200
		response["message"] = "success"

	except Exception as e:

		response["error"] = str(e)

	return JsonResponse(response)


# @login_required
# def event(request, pk):
#     board = get_object_or_404(Event, pk=pk)
#     if request.method == 'POST':
        