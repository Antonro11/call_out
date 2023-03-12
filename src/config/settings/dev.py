import os

from config.settings.base import *  # NOQA

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # "default": {
    #        "ENGINE": "django.db.backends.postgresql",
    #        "NAME":os.environ.get("POSTGRES_DB"),
    #       "USER":os.environ.get("POSTGRES_USER"),
    #        "PASSWORD":os.environ.get("POSTGRES_PASSWORD"),
    #       "HOST":os.environ.get("POSTGRES_HOST"),
    #       "PORT":os.environ.get("POSTGRES_PORT")
    #   }
}

STATIC_URL = "static/"

STATICFILES_DIRS = (BASE_DIR / "static",)

MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"
