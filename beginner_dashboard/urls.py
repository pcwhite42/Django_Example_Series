# FILE PURPOSE: Central routing table that maps URL paths to view functions (including our dashboard app).

# IMPORT: path lets us define human-readable URL patterns; include links to other URL modules.
from django.urls import path, include
# IMPORT: admin site exposes Django's built-in database UI for superusers.
from django.contrib import admin

# NEXT: open dashboard/urls.py to see the app-level routes that join into this list.
# COMMENT: urlpatterns is the list Django uses to match incoming requests to views.
urlpatterns = [
    # COMMENT: When the browser requests "/", include routes from the dashboard app for modular structure.
    path("", include("dashboard.urls")),
    # COMMENT: "/admin/" loads Django's admin site where ExampleRecord becomes editable.
    # NEXT: open dashboard/admin.py to see the registration for ExampleRecord.
    path("admin/", admin.site.urls),
]
