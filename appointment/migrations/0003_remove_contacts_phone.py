# Generated by Django 5.0.6 on 2024-07-25 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='phone',
        ),
    ]
