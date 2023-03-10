# Generated by Django 4.1.6 on 2023-03-04 08:00

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("callout", "0006_alter_battle_start_time_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="battleinvitation",
            old_name="user",
            new_name="sender",
        ),
        migrations.AlterField(
            model_name="battle",
            name="start_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 10, 0, 43, 657748)),
        ),
        migrations.AlterField(
            model_name="battleinvitation",
            name="date_and_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 10, 0, 43, 656748)),
        ),
    ]
