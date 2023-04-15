import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

from callout import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = get_asgi_application()
