# Generated by Django 2.2.1 on 2019-10-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorders',
            name='deliver_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userorders',
            name='order_Date',
            field=models.DateTimeField(null=True),
        ),
    ]
