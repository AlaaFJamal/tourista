# Generated by Django 2.0.7 on 2019-07-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_auto_20190725_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='created_time',
            field=models.DateTimeField(),
        ),
    ]
