from django.shortcuts import render
from .models import SonnenBattery
from django.http import Http404

from django.http import HttpResponse

def index(request):
#    all_sonnenData = SonnenBattery.objects.last()
    all_sonnenData = SonnenBattery.objects.all()
    return render(request, 'sonnen/index.html', {'all_sonnen': all_sonnenData})

def detail(request, sonnen_id):
    try:
        sonnenData = SonnenBattery.objects.get(id=sonnen_id)
        ts = str(sonnenData.timestamp)
    except SonnenBattery.DoesNotExist:
        raise Http404("Sonnen detail does not exist")
#    return HttpResponse('<h2>Details for Sonnen data set ' + str(sonnen_id) + ' </h2>ts: ' + ts + '</h2>')
    return render(request, 'sonnen/detail.html', {'all_sonnen': sonnenData})