# Generated by Django 2.2 on 2019-05-01 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20190430_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='hit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
