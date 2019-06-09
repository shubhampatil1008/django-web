# Generated by Django 2.2.1 on 2019-06-08 13:19

import datetime
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=timezone.now(), verbose_name='date published'),
        ),
    ]
