"""
WSGI config for shinkafa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from core.config import ENV_MODE
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shinkafa.settings")

application = get_wsgi_application()

if ENV_MODE == 'prod' or ENV_MODE is None:
    application = DjangoWhiteNoise(application)
