# Generated by Django 4.0.3 on 2022-04-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_kilometer_alter_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='kilometer',
            field=models.CharField(max_length=32),
        ),
    ]
