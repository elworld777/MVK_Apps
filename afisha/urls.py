from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ar', views.ar, name='ar'),
    path('info', views.info, name='info'),
    path('muzart', views.muzart, name='muzart'),
    path('excurs', views.excurs, name='excurs'),
    path('eco', views.eco, name='eco'),
    path('test', views.test, name='test'),
    path('muzart/<int:id>', views.muzart_list, name='muzart_list'),
    path('<str:pk>', views.exhibitions, name='exhibitions'),
    path('<str:pk>/<int:id>', views.entry, name='entry'),
]
