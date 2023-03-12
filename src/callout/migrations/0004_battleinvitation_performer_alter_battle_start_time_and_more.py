# Generated by Django 4.1.6 on 2023-03-04 07:50

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("callout", "0003_remove_battleinvitation_battle_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="battleinvitation",
            name="performer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="battle",
            name="start_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 9, 50, 12, 413143)),
        ),
        migrations.AlterField(
            model_name="battleinvitation",
            name="date_and_time",
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 9, 50, 12, 413143)),
        ),
    ]