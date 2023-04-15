import os

from config.settings.base import *  # NOQA

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = ["localhost"]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = BASE_DIR / "static1/"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

DATABASES = {
    "default_local_postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "callout_db",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 5432,
    },
    "default_sql": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
    "default_mongo": {
        "ENGINE": "djongo",
        "NAME": "djongo_db",
        "HOST": "localhost",
        "PORT": 27017,
        "AUTHENTICATION_SOURCE": "admin",
        "AUTHENTICATION_MECHANISM": "SCRAM-SHA-1",
        "USERNAME": "admin",
        "PASSWORD": "admin",
    },
}

STATIC_URL = "static/"
