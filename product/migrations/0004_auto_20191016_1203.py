# Generated by Django 2.2.1 on 2019-10-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20191016_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
