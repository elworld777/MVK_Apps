from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ar/', views.ar, name='ar'),
    path('<str:pk>', views.exhibitions, name='exhibitions'),
    path('<str:pk>/<int:id>', views.entry, name='entry'),
]
