# Generated by Django 2.2.1 on 2019-09-27 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sell.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theFirst', '0008_auto_20190919_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('I', 'sem I'), ('II', 'sem II'), ('III', 'sem III'), ('IV', 'sem IV'), ('V', 'sem V'), ('VI', 'sem VI'), ('VII', 'sem VII'), ('VIII', 'sem VIII')], default='I', max_length=11)),
                ('stock_need', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theFirst.branch')),
            ],
        ),
        migrations.CreateModel(
            name='sell_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('I', 'sem I'), ('II', 'sem II'), ('III', 'sem III'), ('IV', 'sem IV'), ('V', 'sem V'), ('VI', 'sem VI'), ('VII', 'sem VII'), ('VIII', 'sem VIII')], default='I', max_length=11)),
                ('book_name', models.CharField(max_length=300)),
                ('year_of_book', models.SmallIntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=sell.models.current_year)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theFirst.branch')),
                ('sell_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
