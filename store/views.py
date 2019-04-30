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
        'categories_footer': categories[0:3],
        'shop_details': shop_details
    }

    print(shop_details)

    return render(request, 'index.html', context)

def categories(request):

    return HttpResponse('categories')

def specific_categories(request, category_name):

    return HttpResponse('specific categories here')

def subcategories(reques, category_name, subcategory_name):

    return HttpResponse('sub category here')

