from photologue.models import ImageModel
from django.contrib.auth.models import User
from django.db import models

class Image(ImageModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_by = models.ForeignKey(User)

