# Generated by Django 2.2.1 on 2019-10-25 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191023_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='bestSelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
