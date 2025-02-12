# Generated by Django 5.0.6 on 2024-08-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusiNess_hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=50)),
                ('day_openging', models.CharField(max_length=10)),
                ('day_ending', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Company_socaial_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=40)),
                ('social_icon', models.CharField(max_length=30)),
                ('social_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FooterImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='footer_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(upload_to='globalLogo/')),
                ('phone_Number', models.CharField(max_length=14)),
                ('adress', models.TextField()),
                ('footertext', models.TextField()),
                ('google_map_url', models.URLField()),
                ('busiNess_hours', models.ManyToManyField(to='globals.business_hours')),
                ('company_socaial_medias', models.ManyToManyField(to='globals.company_socaial_media')),
                ('email', models.ManyToManyField(to='globals.email')),
                ('footerImg', models.ManyToManyField(to='globals.footerimg')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
