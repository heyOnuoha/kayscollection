from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_location = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'SH_Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.branch_name


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_description = models.TextField(blank=True)
    shop_location = models.CharField(max_length=200, blank=True, null=True)
    shop_logo = models.ImageField(upload_to='photos/logos', blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    currency_iso = models.CharField(max_length=3, blank=True, null=True)
    default_shipping_fee = models.DecimalField(decimal_places=2, max_digits=4, default=15.00)
    contact = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'SH_Shop_Info'
        verbose_name_plural = 'Shop'

    def __str__(self):
        return self.shop_name

    # def save(self, *args, **kwargs):
    #     branch = Branch(branch_name=self.shop_name, branch_location=self.shop_location)
    #     branch.save()
    #     super(Shop, self).save(self, *args, **kwargs)

class Categories(models.Model):

    choices = (
        ('NODE', 'NODE'),
        ('LEAF', 'LEAF')
    )

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=5, choices=choices, default='NODE')
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)
    category_link_name = models.CharField(max_length=50, unique=True)
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'SH_Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name


class SubCategories(models.Model):

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)
    category_link_name = models.CharField(max_length=50, unique=True)
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'SH_SubCategory'
        verbose_name_plural = 'Sub Categories'
    
    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):

        if self.category.category_type == 'LEAF':
            raise ValidationError('Cannot add subcategory to leaf category type')
        else:
            super(SubCategories, self).save(*args, **kwargs)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_link = models.TextField(blank=True, null=True)
    product_image_main = models.ImageField(upload_to="photos/products")
    product_image_one = models.ImageField(upload_to="photos/products", blank=True, null=True)
    product_image_two = models.ImageField(upload_to="photos/products", blank=True, null=True)
    product_image_three = models.ImageField(upload_to="photos/products", blank=True, null=True)
    product_image_four = models.ImageField(upload_to="photos/products", blank=True, null=True)
    product_image_five = models.ImageField(upload_to="photos/products", blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    has_size = models.BooleanField(default=False)
    size_xs = models.BooleanField(default=False)
    size_s = models.BooleanField(default=False)
    size_m = models.BooleanField(default=False)
    size_l = models.BooleanField(default=False)
    size_xl = models.BooleanField(default=False)
    size_xxl = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    free_shipping = models.BooleanField(default=False)
    ratings = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    cost_price = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    selling_price = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategories, blank=True, null=True, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def split_price(self):
        return str(self.selling_price).split('.')


    def save(self, *args, **kwargs):

        if self.subcategory is not None:
            self.category = self.subcategory.category

        self.product_link = "-".join(self.product_name.split(" "))
        self.product_link = self.product_link.lower()

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'SH_Products'
    
