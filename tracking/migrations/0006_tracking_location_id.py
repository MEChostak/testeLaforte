# Generated by Django 3.0.13 on 2021-08-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_remove_tracking_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracking',
            name='location_id',
            field=models.IntegerField(default=123456789),
        ),
    ]
