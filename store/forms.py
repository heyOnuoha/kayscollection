from django.forms import ModelForm
from .models import Product, Categories, SubCategories

class ProductFormUpdateViews(ModelForm):

    class Meta:
        model = Product
        fields = ('views',)

class CategoryFormUpdateHit(ModelForm):

    class Meta:
        model = Categories
        fields = ('hit',)

class SubCategoryFormUpdateHit(ModelForm):

    class Meta:
        model = SubCategories
        fields = ('hit',)