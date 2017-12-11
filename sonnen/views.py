from django.shortcuts import render, get_object_or_404
from .models import SonnenBattery

from django.http import HttpResponse

def index(request):
    all_sonnenData = SonnenBattery.objects.all()
    return render(request, 'sonnen/index.html', {'all_sonnen': all_sonnenData})

def detail(request, sonnen_id):
    sonnenData = get_object_or_404(SonnenBattery, id=sonnen_id, )
    return render(request, 'sonnen/detail.html', {'all_sonnen': sonnenData})
