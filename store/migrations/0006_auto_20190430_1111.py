# Generated by Django 2.2 on 2019-04-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_shop_shop_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_name',
            field=models.CharField(max_length=90),
        ),
    ]
