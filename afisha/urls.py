from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>', views.exhibitions, name='exhibitions'),
    path('<str:pk>/<int:id>', views.entry, name='entry'),
    path('ar/', views.ar, name='ar'),
]
