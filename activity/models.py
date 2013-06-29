from django.db import models
from place.models import Place

class ActivityType(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey("ActivityType")
    place = models.ForeignKey(Place)
    distance = models.FloatField(null=True, blank=True)
    difficulty = models.IntegerField(choices = zip(range(1,10), range(1,10)), null=True, blank=True)
    hours = models.FloatField(null=True, blank=True)
    rafting_whitewater = models.IntegerField(choices = zip(range(1,6), range(1,6)), null=True, blank=True)
    fishing_shore = models.NullBooleanField(null=True, blank=True)
    
    def __unicode__(self):
        return '%s %s' % (self.name, self.type)
        
