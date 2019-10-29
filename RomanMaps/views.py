from django.shortcuts import render
from RomanMaps.models import Maps
from django.views.generic import ListView


class ListMaps(ListView):
    model = Maps
    # queryset = Maps.objects.all().order_by('id')
    context_object_name = 'maps'
    # template_name='RomanMaps/Maps.html'

def index(request):
    maps = Maps.objects.all()
    context = {
        'maps' : maps
    }
    return render(request, 'RomanMaps/maps_list.html', context)