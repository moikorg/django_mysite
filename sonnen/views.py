from django.shortcuts import render, get_object_or_404
from .models import SonnenBattery
from django.http import HttpResponse
from django.views import generic

# def index(request):
#     all_sonnenData = SonnenBattery.objects.all()
#     return render(request, 'sonnen/index.html', {'all_sonnen': all_sonnenData})
#
# def detail(request, sonnen_id):
#     sonnenData = get_object_or_404(SonnenBattery, id=sonnen_id, )
#     return render(request, 'sonnen/detail.html', {'all_sonnen': sonnenData})

class DetailView(generic.DetailView):
    model = SonnenBattery
    template_name = 'sonnen/detail.html'

class IndexView(generic.ListView):
    template_name = 'sonnen/index.html'
    context_object_name = 'all_sonnen'

    def get_queryset(self):
        return SonnenBattery.objects.all()

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
