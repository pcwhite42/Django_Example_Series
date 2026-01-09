<!-- REF-HEADER-START -->
Points To:
Referenced By:
- docs\TUTORIAL_SERIES.md
<!-- REF-HEADER-END -->








# Tutorial 1: Build a CSV Insights Dashboard
# FILE PURPOSE: Teach you—step by step—how to show your own CSV on `/`, verify `/about/`, and use `/admin/`.
# GOAL (DONE WHEN): Your custom CSV renders on `/`, `/about/` loads, and `/admin/` works with a superuser you created. You can describe how URL -> view -> template works using your own code.
# PREREQS: Follow README Sections 0–2 (virtualenv, secret key, install deps, migrate, superuser).

## Step-by-Step
1) Get a CSV ready
   - What: Copy `data/sample.csv` to a new file (e.g., `data/my_data.csv`) or create your own CSV with headers.
   - How: Save the file under `data/` with the `my_data.csv` name so the existing path pattern works.

2) Confirm URLs route to views
   - What: In `beginner_dashboard/urls.py`, ensure it includes `dashboard/urls.py`. In `dashboard/urls.py`, map `""` (home) to `views.home` and `about/` to `views.about`.
   - How: Check for `path("", views.home, name="home")` and `path("about/", views.about, name="about")`.

3) Point the home view to your CSV
   - What: In `dashboard/views.py`, set `csv_path = Path(settings.BASE_DIR) / "data" / "my_data.csv"` (replace `my_data.csv` with your filename if different).
   - How: Edit the `csv_path` assignment near the top of `home()`; keep the rest of the pandas logic unchanged so tables render.

4) Apply migrations and prep admin
   - What: Run `python manage.py migrate` and `python manage.py createsuperuser`.
   - Why: `migrate` creates/updates the database schema (so `/admin/` works); `createsuperuser` lets you log into `/admin/`.
   - How: In your activated virtualenv and same terminal, run the commands listed above. Choose username/password when prompted.

5) Run the server and verify pages
   - What: `python manage.py runserver`, then visit:
     - `/` to see your CSV table/summary
     - `/about/` to confirm the static page
     - `/admin/` to log in; confirm **Example Records** shows up
   - Why: Confirms URL -> view -> template is wired correctly and your data is loading.
   - How: Use the browser URLs above; if errors appear, check the traceback and file paths.

6) EXTRA: Add breadcrumbs where you touched code
   - What: Add/update `# CAME FROM` and `# NEXT` near the lines you edited (URLs, views, templates).
   - Why: Breadcrumbs help you (and teammates) trace the flow quickly later.
   - How: Follow the existing comment style already in the codebase.

7) Capture what you learned
   - What: Note the CSV name/path you used and the commands you ran in BUILD_LOG.md or personal notes.
   - Why: Tracking your steps helps you repeat success and debug faster next time.
   - How: Append a short note with the date and outcome.

## Why This Tutorial Matters
- Shows the complete URL -> view -> template flow with your own data.
- Reinforces migrations/admin with a tangible outcome (your CSV live on `/`).
- Builds habits: breadcrumbs, verification in the browser, and keeping a log of what changed.
