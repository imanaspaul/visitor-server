# Generated by Django 3.1.1 on 2020-09-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrylog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrylog',
            name='checkout_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Vistor checkout date and time'),
        ),
    ]
