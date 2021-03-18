from django.shortcuts import render
from django.views.generic import ListView
from afisha.models import Category
from afisha.models import Setting

# Create your views here.


class ListMaps(ListView):
    model = Category
    # queryset = Maps.objects.all().order_by('id')
    context_object_name = 'category'
    # template_name='RomanMaps/Maps.html'


def index(request):
    category = Category.objects.filter(parent_category=None)
    setting = Setting.objects.all()[0]
    context = {
        'category_list': category,
        'setting': setting
    }
    return render(request, 'category_list.html', context)


def exhibitions(request, pk):
    category = Category.objects.get(url=pk).category_set.all()
    entry = Category.objects.get(url=pk).entry_set.all()
    context = {
        'category_list': category,
        'entry_list': entry,
        'url': pk
    }
    return render(request, 'entry_list.html', context)


def entry(request, pk, id):
    entry = Category.objects.get(url=pk).entry_set.all()
    context = {
        'entry_list': entry,
        'id': id
    }
    return render(request, 'detail.html', context)


def ar(request):
    entry = Category.objects.get(url="ar").entry_set.all()
    context = {
        'entry_list': entry
    }
    return render(request, 'ar_list.html', context)

def info(request):
    return render(request, 'info.html')