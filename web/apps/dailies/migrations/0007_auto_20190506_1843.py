# Generated by Django 2.1.7 on 2019-05-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailies', '0006_honkaiimpactdaily_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honkaiimpactdaily',
            name='message_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='honkaiimpactdaily',
            name='sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
