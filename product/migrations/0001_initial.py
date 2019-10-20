# Generated by Django 2.2.1 on 2019-10-16 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theFirst', '0008_auto_20190919_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('book_name', models.CharField(max_length=255)),
                ('status_new', models.BooleanField(default=True)),
                ('semester', models.CharField(choices=[('I', 'sem I'), ('II', 'sem II'), ('III', 'sem III'), ('IV', 'sem IV'), ('V', 'sem V'), ('VI', 'sem VI'), ('VII', 'sem VII'), ('VIII', 'sem VIII')], default='I', max_length=11)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theFirst.branch')),
            ],
        ),
    ]