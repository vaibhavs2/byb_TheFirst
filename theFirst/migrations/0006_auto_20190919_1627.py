# Generated by Django 2.2.1 on 2019-09-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theFirst', '0005_auto_20190919_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestselling',
            name='semester',
            field=models.CharField(choices=[('semI', 'sem I'), ('semII', 'sem II'), ('semIII', 'sem III'), ('semIV', 'sem IV'), ('semV', 'sem V'), ('semVI', 'sem VI'), ('semVII', 'sem VII'), ('semVIII', 'sem VIII')], default='semI', max_length=11),
        ),
        migrations.AlterField(
            model_name='gooddeals',
            name='semester',
            field=models.CharField(choices=[('semI', 'sem I'), ('semII', 'sem II'), ('semIII', 'sem III'), ('semIV', 'sem IV'), ('semV', 'sem V'), ('semVI', 'sem VI'), ('semVII', 'sem VII'), ('semVIII', 'sem VIII')], default='semI', max_length=11),
        ),
    ]
