from django.contrib import admin
from .models import Shop, Branch, Categories, SubCategories, Product

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop_name', 'shop_description')
    list_display_links = ('id', 'shop_name')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch_name', 'branch_location')
    list_display_links = ('id', 'branch_name')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_link_name')
    list_display_links = ('id', 'category_name')

class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_link_name', 'category')
    list_display_links = ('id', 'category_name', 'category')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'has_size', 'quantity', 'selling_price', 'free_shipping', 'ratings')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
admin.site.register(Product, ProductAdmin)