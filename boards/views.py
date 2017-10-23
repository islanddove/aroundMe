from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event 
import json, base64
from django.http import JsonResponse
#import base64

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
        data = str(data[u'data'])
        filename = str(data[u'filename'])
        
        ## Decode the image
        data_index = data.index('base64') + 7
        filedata = data[data_index:]
        decoded_image = base64.b64decode(filedata)
        # write file to system
        print("HELLLLLOOOOOO")
        path = "/static/uploads/" + filename
        with open(path,'w') as f:
            f.write(decoded_image)
        
        newEvent = Event(event_title= title, reader= path, event_date= date, event_time= time, event_location= location, category= category)
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
        
