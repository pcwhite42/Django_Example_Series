# FILE PURPOSE: App-level URL router that connects friendly paths to our dashboard view functions.

# IMPORT: path helps define readable route patterns for this app.
from django.urls import path

# IMPORT: views module holds the functions that respond to requests.
from . import views

# COMMENT: app_name lets Django reverse URLs with the "dashboard:" namespace (useful for links).
app_name = "dashboard"

# COMMENT: urlpatterns maps URL patterns to view callables inside this app.
# CAME FROM: beginner_dashboard/urls.py -> include('dashboard.urls') adds these routes.
urlpatterns = [
    # CAME FROM: dashboard/views.py -> home() via URL route.
    # COMMENT: path("", views.home, name="home") means:
    #   - route "" matches the site root "/"
    #   - view views.home handles the request
    #   - name "home" enables reverse lookups like url 'dashboard:home'
    path("", views.home, name="home"),
    # CAME FROM: dashboard/views.py -> about() explains the teaching flow.
    # COMMENT: path("about/", ...) maps requests for "/about" to the about view.
    # NEXT: open dashboard/templates/dashboard/about.html to see the paired template.
    path("about/", views.about, name="about"),

    # Insert Example 4 work here:
    
]
