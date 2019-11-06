# Generated by Django 2.2.1 on 2019-10-31 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_bestselling'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_auto_20191031_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=20, null=True)),
                ('ordered_date', models.DateTimeField(null=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('shipping_address', models.CharField(max_length=500, null=True)),
                ('total_price', models.PositiveIntegerField(default=0, editable=False)),
                ('payment_received', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='cart.OrderItem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
