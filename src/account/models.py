import random

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from faker import Faker
from phonenumber_field.modelfields import PhoneNumberField

from account.managers import CustomerManager


class Customer(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    user_type = models.CharField(
        choices=(("spectator", "spectator"), ("performer", "performer")), max_length=35, null=True, blank=True
    )
    nickname = models.CharField(max_length=32, blank=True)
    dance_style = models.CharField(
        choices=(("Popping", "Popping"), ("Hip-hop", "Hip-hop"), ("Experimental", "Experimental")),
        max_length=35,
        blank=True,
    )  # NOQA
    promo_video = models.FileField(upload_to="promo_video", blank=True)
    first_name = models.CharField(_("name"), max_length=150, blank=True)
    last_name = models.CharField(_("surname"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(_("phone number"), null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    photo = models.ImageField(upload_to="user_photo", blank=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=35, blank=True)
    city = models.CharField(max_length=35, blank=True)
    gender = models.CharField(choices=(("M", "Male"), ("F", "Female")), max_length=10, blank=True)
    subscribtions = models.ManyToManyField(to="account.Customer", null=True)
    invitations = models.ManyToManyField(to="callout.BattleInvitation", null=True)
    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_performers(cls, count):
        faker = Faker()

        for i in range(count):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                nickname=faker.first_name()[:2] + faker.last_name()[:2],
                gender=random.choice(["M", "F"]),
                dance_style=random.choice(["Popping", "Hip-hop", "Experimental"]),
                password="example",
                user_type="performer",
            )

    @classmethod
    def generate_spectators(cls, count):
        faker = Faker()

        for i in range(count):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                gender=random.choice(["M", "F"]),
                password="example",
                user_type="spectator",
            )
