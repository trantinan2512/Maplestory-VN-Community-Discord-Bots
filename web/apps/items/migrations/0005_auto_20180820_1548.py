# Generated by Django 2.1 on 2018-08-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20180820_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemstatrange',
            name='max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemstatrange',
            name='min',
            field=models.IntegerField(default=0),
        ),
    ]
