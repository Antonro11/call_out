# Generated by Django 4.0.8 on 2023-03-31 07:04

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("callout", "0019_battle_track_one_battle_track_three_battle_track_two_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="start_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 7, 4, 11, 584723)),
        ),
        migrations.AlterField(
            model_name="battleinvitation",
            name="date_and_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 7, 4, 11, 584027)),
        ),
    ]
