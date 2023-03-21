# Generated by Django 4.1.6 on 2023-03-18 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("callout", "0015_alter_battle_start_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 18, 19, 26, 24, 2008)
            ),
        ),
        migrations.AlterField(
            model_name="battleinvitation",
            name="date_and_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 18, 19, 26, 24, 1454)
            ),
        ),
    ]