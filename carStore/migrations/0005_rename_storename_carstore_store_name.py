# Generated by Django 5.1.1 on 2024-10-18 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carStore', '0004_rename_sigongskill_carstore_sigong_skill_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carstore',
            old_name='storeName',
            new_name='store_name',
        ),
    ]
