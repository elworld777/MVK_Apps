from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<char:pk>', views.exhibitions, name='exhibitions'),
]
