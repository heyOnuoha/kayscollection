# Generated by Django 2.2 on 2019-05-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_link_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='category_link_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
