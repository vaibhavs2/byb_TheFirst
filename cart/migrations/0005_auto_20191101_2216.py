# Generated by Django 2.2.1 on 2019-11-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20191101_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
