# FILE PURPOSE: Exposes an ASGI-compatible application so modern servers can talk to Django asynchronously.

# IMPORT: os lets us point to the Django settings module environment variable.
import os

# IMPORT: get_asgi_application creates the ASGI app object Django servers will use.
from django.core.asgi import get_asgi_application

# COMMENT: Configure the default settings module before creating the ASGI application instance.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginner_dashboard.settings")

# NEXT: open beginner_dashboard/settings.py to see the configuration this application relies on.
# COMMENT: Instantiate the ASGI application; used by servers like Daphne or Uvicorn.
application = get_asgi_application()
