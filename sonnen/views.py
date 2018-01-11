#from django.shortcuts import render, get_object_or_404
from .models import SonnenBattery
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.views import generic
#from .forms import UserForm



class DetailView(generic.DetailView):
    model = SonnenBattery
    template_name = 'sonnen/detail.html'
    context_object_name = 'all_sonnen'

class IndexView(generic.ListView):
    model = SonnenBattery
    template_name = 'sonnen/index.html'
    context_object_name = 'all_sonnen'
    paginate_by = 50
    queryset = SonnenBattery.objects.order_by('+timestamp')

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


class UserFormView(View):
    form_cl