from django.shortcuts import render
from django.views.generic import ListView
from afisha.models import Category
from afisha.models import Dates
from afisha.models import Setting

# Create your views here.

def index(request):
    category = Category.objects.filter(
        parent_category=None).order_by('priority')
    setting = Setting.objects.all().first()
    context = {
        'category_list': category,
        'setting': setting
    }
    return render(request, 'category_list.html', context)


def exhibitions(request, pk):
    try:
        category = Category.objects.filter(
            url=pk).first().category_set.all().order_by('priority')
        entry = Category.objects.filter(url=pk).first().entry_set.all()
    except:
        category = None
        entry = None
    context = {
        'category_list': category,
        'entry_list': entry,
        'url': pk
    }
    return render(request, 'entry_list.html', context)


def entry(request, pk, id):
    try:
        entry = Category.objects.filter(url=pk).first().entry_set.all()
    except:
        entry = None
    context = {
        'entry_list': entry,
        'id': id,
        'url': pk
    }
    return render(request, 'detail.html', context)


def ar(request):
    try:
        entry = Category.objects.filter(url="ar").first().entry_set.all()
    except:
        entry = None
    context = {
        'entry_list': entry
    }
    return render(request, 'ar_list.html', context)


def info(request):
    return render(request, 'info.html')


def muzart(request):
    try:
        category = Category.objects.filter(
            url="muzart").first().category_set.all().order_by('priority')
        entry = Category.objects.filter(url="muzart").first().entry_set.all()
    except:
        category = None
        entry = None
    context = {
        'category_list': category,
        'list': entry,
        'url': "muzart"
    }
    return render(request, 'muzart_category.html', context)


def muzart_list(request, id):
    try:
        category = Category.objects.filter(
            url="muzart").first().category_set.all().order_by('priority')
        entry = Category.objects.filter(url="muzart").first().entry_set.all()
    except:
        category = None
        entry = None
    context = {
        'category_list': category,
        'entry_list': entry,
        'url': "muzart",
        'id': id
    }
    return render(request, 'muzart_list.html', context)


def eco(request):
    try:
        entry = Category.objects.filter(url="eco").first().entry_set.all()
    except:
        entry = None
    context = {
        'entry_list': entry
    }
    return render(request, 'slider.html', context)


def excurs(request):
    try:
        dates = Dates.objects.all().order_by('date_start')
    except:
        dates = None
    context = {
        'dates_list': dates
    }
    return render(request, 'excurs_list.html', context)

def test(request):
    try:
        category = Category.objects.filter(
            url="exhibitions").first().category_set.all().order_by('priority')
        entry = Category.objects.filter(url=pk).first().entry_set(manager='active_objects')
    except:
        category = None
        entry = None
    context = {
        'category_list': category,
        'entry_list': entry,
        'url': "exhibitions"
    }
    return render(request, 'entry_list.html', context)