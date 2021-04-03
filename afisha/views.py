from django.shortcuts import render
from django.views.generic import ListView
from afisha.models import Category
from afisha.models import Dates
from afisha.models import Setting
from django.db.models import Q
from django.db.models import Count
from datetime import date

# Create your views here.


def index(request):
    category = Category.active_objects.filter(
        parent_category=None)
    setting = Setting.objects.all().first()
    context = {
        'category_list': category,
        'setting': setting
    }
    return render(request, 'category_list.html', context)


def exhibitions(request, pk):
    try:
        category = Category.objects.filter(
            url=pk).first().category_set(manager='active_objects').all()
        entry = Category.objects.filter(url=pk).first(
        ).entry_set(manager='active_objects').all()
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
        entry = Category.objects.filter(url=pk).first(
        ).entry_set(manager='active_objects').all()
    except:
        entry = None
    context = {
        'entry_list': entry,
        'id': id,
        'url': pk,
        'next': True,
        'count': entry.count()
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
            url="muzart").first().category_set(manager='active_objects').all()
        entry = Category.objects.filter(url="muzart").first(
        ).entry_set(manager='active_objects').all()
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
            url="muzart").first().category_set(manager='active_objects').all()
        entry = Category.objects.filter(url="muzart").first(
        ).entry_set(manager='active_objects').all()
    except:
        category = None
        entry = None
    context = {
        'category_list': category,
        'entry_list': entry,
        'url': "muzart",
        'id': id,
        'next': True,
        'count': entry.count()
    }
    return render(request, 'muzart_list.html', context)


def eco(request):
    try:
        entry = Category.objects.filter(url="eco").first(
        ).entry_set(manager='active_objects').all()
    except:
        entry = None
    context = {
        'entry_list': entry,
        'next': True,
        'count': entry.count()
    }
    return render(request, 'slider.html', context)


def excurs(request):
    try:
        dates = Dates.active_objects.all().order_by('date_start')
    except:
        dates = None
    context = {
        'dates_list': dates,
        'next': True,
        'count': dates.count()
    }
    return render(request, 'excurs_list.html', context)


def test(request):
    try:
        # category = Category.objects.filter(
        #     url="prog").first().category_set.all().annotate(entry_active=Count('entry', distinct=True, filter=Q(active=True)), entry_date=Count('entry', distinct=True, filter=Q(date_end__gte=date.today())), entry_none=Count('entry', distinct=True, filter=Q(date_end=None)), cat_count=Count('category', distinct=True, filter=Q(active=True))).filter(Q(active=True), (Q(entry_active__gt=0) & (Q(entry_date__gt=0) | Q(entry_none__gt=0))) | Q(cat_count__gt=0)).order_by('priority')
        category = Category.objects.filter(url="prog").first().category_set.all().annotate(entry_active=Count('entry', distinct=True, filter=Q(active=True)), entry_date=Count('entry', distinct=True, filter=Q(date_end__gte=date.today())), cat_count=Count('category', distinct=True, filter=Q(active=True))).filter(Q(active=True), (Q(entry_active__gt=0) & Q(entry_date__gt=0)) | Q(cat_count__gt=0)).order_by('priority')

        entry = Category.objects.filter(url="prog").first(
        ).entry_set(manager='active_objects').all()
    except:
        category = None
        entry = None
    context = {
        'category_list': category,
        'entry_list': entry,
        'url': "prog"
    }
    return render(request, 'entry_list.html', context)
