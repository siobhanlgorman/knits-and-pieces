# Generated by Django 3.2 on 2021-12-21 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]
