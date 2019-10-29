from django.urls import path
from django.views.generic import ListView
from RomanMaps.models import Maps
from RomanMaps import views


urlpatterns = [
    path('', ListView.as_view(queryset = Maps.objects.all().order_by('id'), context_object_name = 'maps', template_name='RomanMaps/maps_list.html')),
    path('2/', views.ListMaps.as_view()),
    path('3/', views.index, name='index'),
]