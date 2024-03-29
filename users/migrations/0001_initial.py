# Generated by Django 2.2.1 on 2019-09-19 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=400, null=True)),
                ('landmark', models.CharField(max_length=400, null=True)),
                ('city', models.CharField(choices=[('Bhilai', 'Bhilai'), ('Durg', 'Durg')], max_length=50, null=True)),
                ('pinCode', models.SmallIntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
