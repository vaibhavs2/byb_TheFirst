# Generated by Django 2.2.1 on 2019-10-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191027_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorders',
            name='product_id',
        ),
        migrations.AddField(
            model_name='userorders',
            name='product_id',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
