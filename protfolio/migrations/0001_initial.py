# Generated by Django 5.0.6 on 2024-07-25 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Protfolio_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Protfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protfolio.protfolio_category')),
            ],
        ),
    ]
