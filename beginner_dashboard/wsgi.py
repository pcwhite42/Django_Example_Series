# FILE PURPOSE: Provides the WSGI entry point so traditional web servers (e.g., Gunicorn) can run Django.

# IMPORT: os is needed to point to our Django settings module environment variable.
import os

# IMPORT: get_wsgi_application constructs the WSGI callable Django expects.
from django.core.wsgi import get_wsgi_application

# COMMENT: Ensure the correct settings module is configured before creating the application.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginner_dashboard.settings")

# NEXT: open beginner_dashboard/settings.py to review the config this WSGI app uses.
# COMMENT: WSGI-compatible callable that web servers import.
application = get_wsgi_application()
