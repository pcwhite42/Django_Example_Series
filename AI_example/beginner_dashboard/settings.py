# FILE PURPOSE: Central configuration for the Django project (apps, middleware, templates, static files, etc.).
# CAME FROM: manage.py/asgi.py/wsgi.py -> os.environ.setdefault("DJANGO_SETTINGS_MODULE", ...) loads this settings module.

# IMPORT: Path builds filesystem paths; os lets us read environment variables for secrets.
from pathlib import Path
import os

# COMMENT: BASE_DIR is the root of our project used to build paths (templates, static files, data).
BASE_DIR = Path(__file__).resolve().parent.parent

# COMMENT: SECRET_KEY is used for cryptographic signing; Django generates one per project.
# TEACHING NOTE: Read DJANGO_SECRET_KEY from the environment so secrets stay out of source control.
# TEACHING FALLBACK: The default below is safe for local learning only. Generate a real key with:
#   python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-teaching-key-change-me"
)

# COMMENT: DEBUG=True is great for learning because Django shows detailed error pages.
# DEPLOYMENT REMINDER: Set DEBUG=False in production so stack traces and settings stay private.
DEBUG = True

# COMMENT: ALLOWED_HOSTS lists trusted hostnames; lock it down even in tutorials to promote good habits.
# TEACHING DEFAULT: Local requests only. Add real domain names (and optional ports) before deploying.
ALLOWED_HOSTS: list[str] = ["127.0.0.1", "localhost"]
# DEPLOYMENT NOTE: Pair ALLOWED_HOSTS updates with CSRF_TRUSTED_ORIGINS (e.g., ["https://example.com"]) once you host it.

# COMMENT: INSTALLED_APPS lists Django and custom apps the project uses.
#          We include Django defaults plus our new "dashboard" app so Django can find its models and templates.
INSTALLED_APPS = [
    "django.contrib.admin",  # Admin site for managing data
    "django.contrib.auth",  # Authentication framework
    "django.contrib.contenttypes",  # Content type system
    "django.contrib.sessions",  # Server-side sessions
    "django.contrib.messages",  # Messaging framework (flash messages)
    "django.contrib.staticfiles",  # Static file handling (CSS, images)
    "dashboard",  # Our teaching app that renders the CSV dashboard
]

# COMMENT: MIDDLEWARE are hooks that wrap every request (security, sessions, etc.).
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# COMMENT: ROOT_URLCONF points Django to the module containing the project's URL patterns.
ROOT_URLCONF = "beginner_dashboard.urls"

# COMMENT: TEMPLATES tells Django where to find HTML files and how to render them.
#          The DIRS setting adds BASE_DIR / "dashboard" / "templates" so we can keep templates beside the app.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "dashboard" / "templates"],  # Teach: custom templates location
        "APP_DIRS": True,  # Let Django find templates inside app folders automatically
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# COMMENT: WSGI_APPLICATION points to the callable defined in beginner_dashboard/wsgi.py for deployment.
WSGI_APPLICATION = "beginner_dashboard.wsgi.application"

# COMMENT: Using SQLite keeps this tutorial simple; database file lives inside the project directory.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# COMMENT: Password validation settings help enforce strong password rules (good practice, even in tutorials).
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# COMMENT: Language and timezone defaults.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# COMMENT: STATIC_URL defines the URL prefix for static assets.
# COMMENT: STATICFILES_DIRS tells Django where to look for custom static files (like our CSS).
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "dashboard" / "static"]

# COMMENT: Default primary key type for new models.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# NEXT: open dashboard/apps.py to see how this app describes itself to Django.
