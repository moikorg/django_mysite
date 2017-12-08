from django.http import HttpResponse
from django.shortcuts import render
from .models import SonnenBattery

from django.http import HttpResponse

def index(request):
#    all_sonnenData = SonnenBattery.objects.last()
    all_sonnenData = SonnenBattery.objects.all()
    context = {'all_sonnen': all_sonnenData}
    return render(request, 'sonnen/index.html', context)

def detail(request, sonnen_id):
    sonnenData = SonnenBattery.objects.get(id=sonnen_id)
    ts = str(sonnenData.timestamp)
    return HttpResponse('<h2>Details for Sonnen data set ' + str(sonnen_id) + ' </h2>ts: ' + ts + '</h2>')