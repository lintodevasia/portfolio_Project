# Generated by Django 3.2.7 on 2022-02-24 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0009_auto_20220224_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='resume',
        ),
    ]
