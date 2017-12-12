from django.shortcuts import render, get_object_or_404
from .models import SonnenBattery
from django.http import HttpResponse
import json
from django.core import serializers

def index(request):
    all_sonnenData = SonnenBattery.objects.all()
    return render(request, 'sonnen/index.html', {'all_sonnen': all_sonnenData})

def detail(request, sonnen_id):
    sonnenData = get_object_or_404(SonnenBattery, id=sonnen_id, )
    return render(request, 'sonnen/detail.html', {'all_sonnen': sonnenData})

def status(request):
    qs = SonnenBattery.objects.latest('timestamp')
#    qs = SonnenBattery.objects.all()
#    qs_json = serializers.serialize('json', qs)
    context = {'timestamp': qs.timestamp,
               'consumption': qs.consumption,
               'production': qs.production,
               'gridConsumption': qs.gridConsumption,
               }
    return render(request, 'sonnen/status.html', context)
