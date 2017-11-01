from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event 
from .forms import UploadFileForm
import json, base64, os
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#import base64

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect, render

def landingpage(request):
    return render(request, 'landing.html')

@csrf_protect
def home(request):
    c = {}
    events = Event.objects.all()
    return render(request, 'base.html', {'events':events}, c)

@csrf_protect
def eventpage(request):
    c = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES.get('input-b1')
            print(str(filename))
            if filename != None:
                filename = filename.name
                path = '/home/depuleio/aroundMe/static/uploads/' + filename
                handle_uploaded_file(request.FILES['input-b1'],path)
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'eventpage.html', {'form':form}, c)

def handle_uploaded_file(f,path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_protect
def createEvent(request):
    
    response = {"code": 400, "message": "request failed to send"}
    
    try:
        print("enter try")
        data = json.loads(request.body.decode("utf-8"))
        filename = str(data.get(u'filename'))
        if filename == None:
            path = "https://i.pinimg.com/originals/9b/87/0b/9b870b29291ee7502d0ec99ab3b6733d.png"
        else:
            path = str("../static/uploads/" + filename)

        newEvent = Event(event_title= str(data[u'title']), event_date= str(data[u'date']), event_time= str(data[u'time']), 
            event_location= str(data[u'location']), category= str(data[u'category']),reader= path,)
        
        newEvent.save()
        print("saved")
        response["code"] = 200
        response["message"] = "success"
        
    
    except Exception as e:
        response["error"] = str(e)
        
    
    return JsonResponse(response)


# @login_required
# def event(request, pk):
#     board = get_object_or_404(Event, pk=pk)
#     if request.method == 'POST':
        
