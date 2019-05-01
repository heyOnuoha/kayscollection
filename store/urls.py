from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('categories/', view=views.categories, name='categories'),
    path('categories/<slug:category_name>/', view=views.specific_categories, name='specific_categories'),
    path('categories/<slug:category_name>/<slug:subcategory_name>/', view=views.subcategories, name='subcategories'),
    #path('categories/new-products/', view=views.new_products, name='new_products'),
    path('categories/<slug:category_name>/<slug:subcategory_name>/<slug:product_link>/<int:product_id>/', view=views.product, name='product')
]