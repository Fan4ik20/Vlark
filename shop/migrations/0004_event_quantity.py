# Generated by Django 3.1.3 on 2020-11-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201117_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='quantity',
            field=models.IntegerField(default=100),
        ),
    ]
