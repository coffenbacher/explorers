# Create your views here.
from models import *
from django.http import HttpResponse
from django.core import serializers
import json

import pdb

def search(request):
    p = {
            "type": request.GET["type"],
            "latitude": float(request.GET["latitude"]),
            "longitude": float(request.GET["longitude"]),
            "radius": float(request.GET["radius"]),
            "min_difficulty": request.GET.get("difficulty", 0),
            "max_difficulty": request.GET.get("difficulty", 10),
            "min_hours": float(request.GET.get("min_hours", 0)),
            "max_hours": float(request.GET.get("max_hours", 1000)),
            }
    
    dr_lat = float(p["radius"]) / 69.0
    dr_lng = float(p["radius"]) / 50.0
    #pdb.set_trace()

    activities = Activity.objects.filter(type__name__iexact=p['type'], 
                                            place__latitude__lt = p['latitude'] + dr_lat,
                                            place__latitude__gt = p['latitude'] - dr_lng,
                                            place__longitude__lt = p['longitude'] + dr_lat,
                                            place__longitude__gt = p['longitude'] - dr_lng,
                                            difficulty__gte = p['min_difficulty'],
                                            difficulty__lte = p['max_difficulty'],
                                            hours__gte = p['min_hours'],
                                            hours__lte = p['max_hours'],)



    d = []
    for a in activities:
        di = {
            "name": a.name,
            "description": a.description,
            "latitude": a.place.latitude,
            "longitude": a.place.longitude,
            "difficulty": a.difficulty,
            "hours": a.hours,
            "images": [i.photo.get_absolute_url() for i in a.place.images.all()]
        }

        d.append(di)
    return HttpResponse(json.dumps(d))


