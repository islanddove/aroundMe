
from django.conf.urls import url

from . import views

urlpatterns = [

	#renders templates
    url(r'^home/', views.index, name='index'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^event_page/', views.event_page, name='event_page'),

    #AJAX
    url(r'^createEvent/', views.createEvent, name='createEvent'),
]

