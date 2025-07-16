"""
WSGI config for Network_Management_System project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Network_Management_System.settings')

application = get_wsgi_application()

# Optional: Explicitly set the staticfiles directory
BASE_DIR = Path(__file__).resolve().parent.parent
application = WhiteNoise(application, root=BASE_DIR / 'staticfiles')
