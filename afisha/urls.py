from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ar', views.ar, name='ar'),
    path('info', views.info, name='info'),
    path('muzart', views.muzart, name='muzart'),
    path('excurs', views.excurs, name='excurs'),
    path('slider', views.slider, name='slider'),
    path('slider1', views.slider1, name='slider1'),
    path('slider2', views.slider2, name='slider2'),
    path('exhibit', views.exhibit, name='exhibit'),
    path('test', views.test, name='test'),
    path('muzart/<int:id>', views.muzart_list, name='muzart_list'),
    path('<str:pk>', views.exhibitions, name='exhibitions'),
    path('<str:pk>/<int:id>', views.entry, name='entry'),
]
