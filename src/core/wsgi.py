
import os
import sys

from django.core.wsgi import get_wsgi_application

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
