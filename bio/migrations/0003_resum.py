# Generated by Django 3.2.7 on 2022-02-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='resum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='files')),
            ],
        ),
    ]
