# Generated by Django 3.2 on 2021-12-30 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customorder',
            name='size',
        ),
    ]
