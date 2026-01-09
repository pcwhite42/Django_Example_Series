<!-- REF-HEADER-START -->
Points To:
Referenced By:
- GettingStartedHowTo.md
- docs\TUTORIAL_SERIES.md
<!-- REF-HEADER-END -->




# FILE PURPOSE: Sketch intermediate-level paths for learners who finished the beginner dashboard and want the next challenge.
# CAME FROM: docs/TUTORIAL_SERIES.md -> after finishing the examples, come here to expand your skills.
# NEXT: Pick one guide, create a new Git branch, and document your progress so you can teach others later.

## Guide 1: Persist CSV Data into the ORM
- Summary: Import `data/sample.csv` into the `ExampleRecord` model so the dashboard reads from the database instead of disk.
- Key Concepts:
  - Django management commands (`python manage.py shell` or custom commands).
  - Bulk creating model instances from pandas DataFrames.
  - Updating the view to query `ExampleRecord.objects.all()` and convert it back into a DataFrame.
- Stretch Goal: Add an admin action that re-imports the CSV on demand.

## Guide 2: Build a Multi-Page Report
- Summary: Split analytics across multiple views (`/overview/`, `/trends/`, `/export/`) while sharing helper functions.
- Key Concepts:
  - Using `dashboard/utils.py` to extract shared pandas transformations.
  - Leveraging Django URL namespaces and template inheritance to avoid duplication.
  - Documenting navigation breadcrumbs so new pages remain easy to follow.
- Stretch Goal: Add smoke tests for each new route using the existing pattern in `dashboard/tests.py`.

## Guide 3: Add User Input Safely
- Summary: Let authenticated users upload a CSV, validate it, and display a preview.
- Key Concepts:
  - Django forms and file uploads (still storing files locally for simplicity).
  - Validating CSV headers/types before handing them to pandas.
  - Explaining security considerations (e.g., cleaning HTML from user data).
- Stretch Goal: Store uploads in a temporary folder and add a cleanup command.

## Guide 4: Schedule a Daily Summary Email (Conceptual)
- Summary: Generate a daily report using pandas and send it via email.
- Key Concepts:
  - Using Django's email utilities with the console backend for local testing.
  - Writing a `management/commands/send_daily_summary.py` script.
  - Logging results so learners can debug background tasks.
- Stretch Goal: Replace the console backend with a real SMTP service once ready for production.

## Guide 5: Deploy to a Free Platform
- Summary: Package the project for deployment on a beginner-friendly host (e.g., PythonAnywhere or Render) without adding new dependencies.
- Key Concepts:
  - Configuring environment variables for production.
  - Collecting static files with `python manage.py collectstatic`.
  - Migrating the SQLite database or switching to the host's managed database service.
- Stretch Goal: Automate deployment with a simple shell script learners can customize.
