from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField() #should be region
    longitude = models.FloatField() #should be region
    related = models.ManyToManyField("Place", symmetrical=True, blank=True)

    def __unicode__(self):
        return self.name
