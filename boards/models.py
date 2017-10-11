from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator

from django.utils import timezone

# Create your models here.


class Event(models.Model):    

    event_title = models.CharField(max_length=30,default='')
    event_date = models.CharField(max_length=30,default='')
    event_time = models.CharField(max_length=15,default='')
    event_location = models.CharField(max_length=30,default='')

    pub_date = models.DateTimeField(default=timezone.now)

    EDUCATIONAL = 'EDU'
    ARTSCRAFTS = 'ART'
    SOCIAL = 'SOC'
    LATENIGHT = 'LAT'
    EVENT_CATEGORIES = [ (EDUCATIONAL, 'Educational'), (ARTSCRAFTS, 'Arts & Crafts'), (SOCIAL, 'Social'), (LATENIGHT, 'Late Night'), ]

    category = models.CharField(
        max_length=3,
        choices=EVENT_CATEGORIES,
        default=SOCIAL,
    )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
