# Generated by Django 3.0.13 on 2021-08-03 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20210803_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='location_id',
        ),
    ]
