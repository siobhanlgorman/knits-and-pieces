# Generated by Django 3.2 on 2021-12-30 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0004_auto_20211230_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customorder',
            old_name='pattern_name',
            new_name='design',
        ),
    ]
