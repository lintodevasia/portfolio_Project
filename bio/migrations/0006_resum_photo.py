# Generated by Django 3.2.7 on 2022-02-24 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0005_resum'),
    ]

    operations = [
        migrations.AddField(
            model_name='resum',
            name='photo',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
