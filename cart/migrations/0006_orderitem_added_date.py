# Generated by Django 2.2.1 on 2019-11-02 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20191101_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='added_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
