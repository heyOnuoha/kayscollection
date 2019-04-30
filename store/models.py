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
    category_link_name = models.CharField(max_length=50)
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
    category_link_name = models.CharField(max_length=50)
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
            super(SubCategories, self).save(self, *args, **kwargs)
