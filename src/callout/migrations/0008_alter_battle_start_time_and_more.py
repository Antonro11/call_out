# Generated by Django 4.1.6 on 2023-02-21 07:57

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("callout", "0007_alter_battle_start_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="start_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 9, 57, 48, 485742)),
        ),
        migrations.AlterField(
            model_name="battleinvitation",
            name="date_and_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 9, 57, 48, 485742)),
        ),
    ]