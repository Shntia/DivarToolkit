# Generated by Django 4.0.3 on 2022-04-12 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_dailyprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyprice',
            name='date',
            field=models.CharField(default=datetime.datetime(2022, 4, 12, 19, 21, 11, 242920), max_length=32),
        ),
    ]
