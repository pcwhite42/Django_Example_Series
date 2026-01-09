# FILE PURPOSE: Defines metadata so Django recognizes the dashboard application.

# IMPORT: AppConfig is Django's base class for describing an app to the project.
from django.apps import AppConfig


# CLASS: DashboardConfig declares the app name and readable label seen in admin.
class DashboardConfig(AppConfig):
    # COMMENT: default_auto_field sets the default primary key type for models in this app.
    default_auto_field = "django.db.models.BigAutoField"
    # COMMENT: name is the dotted Python path to the app; Django uses it during setup.
    name = "dashboard"
    # CAME FROM: beginner_dashboard/settings.py -> INSTALLED_APPS registers this config.
