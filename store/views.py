from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Categories, Shop, Product, SubCategories

# Create your views here.
def index(request):

    categories = Categories.objects.all()
    shop_details = Shop.objects.all()[0]
    fproducts = Product.objects.all()

    context = {
        'categories': categories,
        'categories_footer': categories[0:3],
        'shop_details': shop_details,
        'hit_categories': categories.order_by('-hit')[0:4],
        'fproducts': fproducts
    }

    return render(request, 'index.html', context)

def categories(request):

    return HttpResponse('categories')

def specific_categories(request, category_name):

    return HttpResponse('specific categories here')

def subcategories(request, category_name, subcategory_name):

    return HttpResponse('sub category here')

def product(request, category_name, subcategory_name, product_link, product_id):

    try:
        category = Categories.objects.get(category_link_name=category_name)
        subcategory = SubCategories.objects.get(category_link_name=subcategory_name)
        product_link_v = Product.objects.get(product_link=product_link)
        product_id = Product.objects.get(pk=product_id)

        if category is None or subcategory is None:
            raise Http404("")
    except Product.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    categories = Categories.objects.all()
    shop_details = Shop.objects.all()[0]
    product = product_id

    context = {
        'categories': categories,
        'categories_footer': categories[0:3],
        'shop_details': shop_details,
        'hit_categories': categories.order_by('-hit')[0:4],
        'product': product
    }

    return render(request, 'product.html', context)

