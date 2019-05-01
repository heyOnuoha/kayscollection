from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Categories, Shop, Product, SubCategories
from .forms import ProductFormUpdateViews, CategoryFormUpdateHit, SubCategoryFormUpdateHit

# Create your views here.
def index(request):

    categories = Categories.objects.all()
    shop_details = Shop.objects.all()[0]
    fproducts = Product.objects.all()

    context = {
        'categories': categories,
        'categories_footer': categories[0:3],
        'shop_details': shop_details,
        'hit_categories': categories.order_by('-hit')[0:3],
        'fproducts': fproducts.order_by('-views')
    }

    return render(request, 'index.html', context)

def categories(request):

    return HttpResponse('categories')

def specific_categories(request, category_name):

    categories = Categories.objects.all()
    shop_details = Shop.objects.all()[0]
    fproducts = Product.objects.all()

    context = {
        'categories': categories,
        'categories_footer': categories[0:3],
        'shop_details': shop_details,
        'hit_categories': categories.order_by('-hit')[0:3],
        'fproducts': fproducts.order_by('-views')
    }

    return render(request, 'categories.html', context)

def subcategories(request, category_name, subcategory_name):

    return HttpResponse('sub category here')

def new_products(request):

    return HttpResponse('new products')

def product(request, category_name, subcategory_name, product_link, product_id):

    try:
        product = Product.objects.get(pk=product_id)
        category = Categories.objects.get(category_link_name=product.category.category_link_name)
        subcategory = SubCategories.objects.get(category_link_name=product.subcategory.category_link_name)
        product_link_v = Product.objects.get(product_link=product_link)

        if category is None or subcategory is None or category.category_link_name != category_name or subcategory.category_link_name != subcategory_name:
            raise Http404("")
    except Product.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    categories = Categories.objects.all()
    shop_details = Shop.objects.all()[0]

    update_data_product = {
        'views': product.views + 1
    }

    update_data_category = {
        'hit': category.hit + 1
    }

    update_data_subcategory = {
        'hit': subcategory.hit + 1
    }


    try:       
        product_form = ProductFormUpdateViews(instance=product, data=update_data_product)
        category_form = CategoryFormUpdateHit(instance=category, data=update_data_category)
        subcategory_form = SubCategoryFormUpdateHit(instance=subcategory, data=update_data_subcategory)


        if product_form.is_valid() and category_form.is_valid() and subcategory_form.is_valid():
            product_form.save()
            category_form.save()
            subcategory_form.save()

    except Exception as e:
        raise Exception(e)

    context = {
        'categories': categories,
        'categories_footer': categories[0:3],
        'shop_details': shop_details,
        'hit_categories': categories.order_by('-hit')[0:3],
        'product': product
    }

    return render(request, 'product.html', context)

