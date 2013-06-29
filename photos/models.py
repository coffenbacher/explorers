from photologue.models import ImageModel
from django.contrib.auth.models import User
from django.db import models
from activity.models import ActivityType
from place.models import Place

class Image(ImageModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_by = models.ForeignKey(User)

    places = models.ManyToManyField(Place, related_name='images', blank=True, null=True)
    activity = models.ForeignKey(ActivityType)
    
