# Generated by Django 4.1.6 on 2023-02-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0008_alter_customer_gender_alter_customer_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="photo",
            field=models.ImageField(blank=True, upload_to="user_photo"),
        ),
    ]