# FILE PURPOSE: Register dashboard models with Django's admin site so beginners can browse data in the browser.
# CAME FROM: beginner_dashboard/urls.py -> path("admin/", admin.site.urls) exposes this admin module.
# CAME FROM: dashboard/models.py -> ExampleRecord defines the schema we expose here.
# NEXT: Open ADMIN_ONBOARDING.md for the exact commands to migrate the database and create a superuser.

# IMPORT: admin is Django's admin interface configuration module.
from django.contrib import admin

# IMPORT: ExampleRecord is our teaching model showcasing ORM structure.
from .models import ExampleRecord


# FUNCTION: admin.site.register wires ExampleRecord into the admin UI with default settings.
# FIRST STEPS: Anytime you add or edit models, run makemigrations + migrate, then createsuperuser for login (see ADMIN_ONBOARDING.md).
# TEACHING TIP: Use @admin.register for custom list displays once you need more control.
admin.site.register(ExampleRecord)
