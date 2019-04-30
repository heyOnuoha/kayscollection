from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('categories/', view=views.categories, name='categories'),
    path('categories/<slug:category_name>', view=views.categories, name='categories')
]