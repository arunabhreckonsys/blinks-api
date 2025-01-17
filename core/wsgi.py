"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os
from pathlib import Path
# import newrelic.agent

# cod
# newrelic.agent.initialize('newrelic.ini')
# newrelic.agent.register_application()

from django.core.wsgi import get_wsgi_application

# from core.settings import BASE_DIR

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
