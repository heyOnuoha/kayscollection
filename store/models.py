from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_description = models.TextField(black=True)
    shop_location = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'SH_Shop_Info'
        verbose_name_plural = 'Shop'

    def __str__(self):
        return self.shop_name

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_location = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'SH_Branch'

    def __str__(self):
        return self.branch_name

class Categories(models.Model):

    choices = (
        ('NODE', 'NODE'),
        ('LEAF', 'LEAF')
    )

    branch = models.ForeignKey(Branch)
    category_type = models.CharField(max_length=5, choices=choices, default='NODE')
    category_parent = models.ForeignKey('self', null=True)
    category_root = models.ForeignKey('self', blank=True, null=True)
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)
    category_link_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'SH_Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):

        if self.category_parent.category_root is None:
            self.category_parent = None
            self.category_root = self
        elif self.category_parent.category_parent is not None:
            self.category_parent  = self.category_parent.category_parent
            self.category_root = self.category_root

        super.save(self, *args, **kwargs)
