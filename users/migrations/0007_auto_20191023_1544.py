# Generated by Django 2.2.1 on 2019-10-23 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190928_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^([\\s\\d]+)$', 'Only numbers are allowed.')]),
        ),
    ]