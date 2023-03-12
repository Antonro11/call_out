# Generated by Django 4.1.6 on 2023-03-04 07:14

import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models

import account.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("spectator", "spectator"),
                            ("performer", "performer"),
                        ],
                        max_length=35,
                        null=True,
                    ),
                ),
                ("nickname", models.CharField(blank=True, max_length=32)),
                (
                    "dance_style",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Popping", "Popping"),
                            ("Hip-hop", "Hip-hop"),
                            ("Experimental", "Experimental"),
                        ],
                        max_length=35,
                    ),
                ),
                ("promo_video", models.FileField(blank=True, upload_to="promo_video")),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="name"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, verbose_name="surname"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, unique=True, verbose_name="email address"),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="phone number",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined"),
                ),
                ("photo", models.ImageField(blank=True, upload_to="user_photo")),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("country", models.CharField(blank=True, max_length=35)),
                ("city", models.CharField(blank=True, max_length=35)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=10,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "subscribtions",
                    models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", account.managers.CustomerManager()),
            ],
        ),
    ]
