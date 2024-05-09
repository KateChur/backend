"""
WSGI config for VKR_Churashkina_Events_Platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VKR_Churashkina_Events_Platform.settings')

application = get_wsgi_application()
