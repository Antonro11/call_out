# Generated by Django 4.1.6 on 2023-03-09 17:59

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "callout",
            "0013_rename_accepted_battleinvitation_accepted_performer_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="start_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 19, 59, 20, 625582)),
        ),
        migrations.AlterField(
            model_name="battleinvitation",
            name="date_and_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 19, 59, 20, 624588)),
        ),
    ]
