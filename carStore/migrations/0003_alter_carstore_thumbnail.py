# Generated by Django 5.1.1 on 2024-10-16 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carStore', '0002_carstore_business_hours_carstore_holidays_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carstore',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='car_store_thumbnail'),
        ),
    ]
