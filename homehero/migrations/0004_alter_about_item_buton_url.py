# Generated by Django 5.0.6 on 2024-07-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homehero', '0003_about_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_item',
            name='buton_url',
            field=models.URLField(blank=True),
        ),
    ]
