# Generated by Django 4.1.6 on 2023-03-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_customer_changed_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="changed_time",
            field=models.BooleanField(default=True),
        ),
    ]
