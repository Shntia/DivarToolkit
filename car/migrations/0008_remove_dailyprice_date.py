# Generated by Django 4.0.3 on 2022-04-12 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_dailyprice_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyprice',
            name='date',
        ),
    ]
