#!/usr/bin/env python
# FILE PURPOSE: Provides the command-line entry point so we can run Django helper commands like runserver.

# IMPORT: os lets us talk to the operating system for environment variables and paths.
import os
# IMPORT: sys allows us to read command-line arguments passed into this script.
import sys

# FUNCTION: main() is Django's default helper that dispatches management commands.
# WHY: We keep Django's generated behavior but add comments to explain the flow.
def main():
    """Run administrative tasks."""
    # COMMENT: Django looks for the settings module so commands know project configuration.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginner_dashboard.settings")
    try:
        # IMPORT: execute_from_command_line hands the command to Django's management system.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # COMMENT: Helpful message if Django is missing from the virtual environment.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # NEXT: open beginner_dashboard/settings.py to see how this settings module is configured.
    execute_from_command_line(sys.argv)


# COMMENT: This guard means the script only runs when executed directly, not when imported.
if __name__ == "__main__":
    main()
