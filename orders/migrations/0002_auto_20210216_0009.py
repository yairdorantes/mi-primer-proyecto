# Generated by Django 3.1.6 on 2021-02-16 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orderline',
            table='orderlines',
        ),
    ]
