# Generated by Django 5.1.1 on 2024-10-10 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_location_sigongskill_user_isshop_carstore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isShop',
            new_name='isStore',
        ),
        migrations.AddField(
            model_name='user',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.carstore'),
        ),
    ]
