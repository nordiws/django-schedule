# Generated by Django 4.0.3 on 2022-04-08 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='criation_date',
            new_name='creation_date',
        ),
    ]
