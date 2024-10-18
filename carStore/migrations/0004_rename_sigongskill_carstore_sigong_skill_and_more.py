# Generated by Django 5.1.1 on 2024-10-18 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carStore', '0003_alter_carstore_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carstore',
            old_name='sigongSkill',
            new_name='sigong_skill',
        ),
        migrations.RenameField(
            model_name='carstore',
            old_name='storeLocation',
            new_name='store_location',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='storeDetail_address',
            new_name='store_detail_address',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='storeJibun_address',
            new_name='store_jibun_address',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='storePostal_code',
            new_name='store_postal_code',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='storeStreet_address',
            new_name='store_street_address',
        ),
    ]
