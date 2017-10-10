from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator

from django.utils import timezone

# Create your models here.


class Event(models.Model):  
    
    event_title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)
    rsvp = models.BooleanField(default=False)

    private = models.BooleanField(default=False)

    SEMINAR = 'SEM'
    SOCIAL = 'SOC'
    PARTY = 'PAR'
    CONFERENCE = 'CON'
    MEETING = 'MTG'
    EVENT_CATEGORIES = [ (SEMINAR, 'Seminar'), (SOCIAL, 'Social'), (PARTY, 'Party'), (CONFERENCE, 'Conference'), (MEETING,'Meeting') ]


    category = models.CharField(
        max_length=3,
        choices=EVENT_CATEGORIES,
        default=SOCIAL,
    )


    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
