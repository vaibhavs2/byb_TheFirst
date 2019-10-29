# Generated by Django 2.2.1 on 2019-10-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_bestselling'),
        ('users', '0009_auto_20191024_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorders',
            name='product_id',
        ),
        migrations.AddField(
            model_name='userorders',
            name='product_id',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
    ]
