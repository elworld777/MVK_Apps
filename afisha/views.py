from django.shortcuts import render
from django.views.generic import ListView
from afisha.models import Category

# Create your views here.


class ListMaps(ListView):
    model = Category
    # queryset = Maps.objects.all().order_by('id')
    context_object_name = 'category'
    # template_name='RomanMaps/Maps.html'


def index(request):
    category = Category.objects.all()
    context = {
        'category_list': category
    }
    return render(request, 'category_list.html', context)


def exhibitions(request, pk):
    category = Category.objects.filter(url=pk)
    subcategory = category.category_set.all()
    context = {
        'category_list': subcategory
    }
    return render(request, 'category_list.html', context)
