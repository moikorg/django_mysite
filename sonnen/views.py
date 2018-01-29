import django.shortcuts
from .models import SonnenBattery
from django.views import generic
import datetime

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
    context_object_name = 'all_sonnen'


class IndexView(generic.ListView):
    model = SonnenBattery
    template_name = 'sonnen/index.html'
    context_object_name = 'all_sonnen'
    paginate_by = 200
    queryset = SonnenBattery.objects.order_by('-pk')

    def get_queryset(self):
        return SonnenBattery.objects.all()


def status(request):
    qs = SonnenBattery.objects.latest('timestamp')
#    qs = SonnenBattery.objects.filter(timestamp__lt=datetime.date(2018, 1, 25)).latest('timestamp')

    discharging = False
    charging = False
    holding = False
    if qs.pacTotal > 0:
        discharging = True
    if qs.production > qs.consumption:
        charging = True
    else:
        holding = True
    context = {'timestamp': qs.timestamp,
               'consumption': qs.consumption,
               'production': qs.production,
               'pacTotal': qs.pacTotal,
               'pacTotalAbsolut': abs(qs.pacTotal),
               'gridConsumption': qs.gridConsumption,
               'gridConsumptionAbsolut': abs(qs.gridConsumption),
               'uBat': qs.uBat,
               'usoc': qs.usoc,
               'discharging': discharging,
               'charging': charging,
               'holding': holding,
               }
    return django.shortcuts.render(request, 'sonnen/status.html', context)
