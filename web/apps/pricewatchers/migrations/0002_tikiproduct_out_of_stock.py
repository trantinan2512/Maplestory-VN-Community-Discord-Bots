# Generated by Django 2.1.7 on 2020-02-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricewatchers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tikiproduct',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]
