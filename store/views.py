from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories
from .models import Shop

# Create your views here.
def index(request):

    categories = Categories.objects.all()
    shop_details = Shop.objects.all()[0]

    context = {
        'categories': categories,
        'shop_details': shop_details
    }

    print(shop_details)

    return render(request, 'index.html', context)

def categories(request, category_name):

    return HttpResponse('hello')

