# Generated by Django 3.1.3 on 2020-11-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_cost',
            field=models.IntegerField(default=0),
        ),
    ]
