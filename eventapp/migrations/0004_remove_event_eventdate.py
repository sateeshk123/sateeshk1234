# Generated by Django 4.0.4 on 2022-04-23 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_remove_event_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventdate',
        ),
    ]
