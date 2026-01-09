<!-- REF-HEADER-START -->
Points To:
- README.md
- docs/MIGRATIONS_CHECKLIST.md
Referenced By:
- README.md
- docs\BEGINNER_EXAMPLES.md
- docs\MIGRATIONS_CHECKLIST.md
<!-- REF-HEADER-END -->











# FILE PURPOSE: Help beginners diagnose common setup errors without leaving the repo.
# CAME FROM: README.md -> If stuck, check here.
# NEXT: When you fix an issue, add a note to BUILD_LOG.md or your personal journal so you remember what worked. See ::--:: README.md for the main flow.


## Secret Key or Environment Variable Errors
- **Symptom:** `django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.`
- **Fix:**
  1. Copy `.env.example` to `.env` if you have not already.
  2. Set `DJANGO_SECRET_KEY` in your shell (`$env:DJANGO_SECRET_KEY="..."` on PowerShell).
  3. Restart the terminal or re-run the command after exporting the variable.
- **Prevention:** Add the export step to your startup notes; do not commit `.env`.

## No Such Table or Migration Warnings
- **Symptom:** `django.db.utils.OperationalError: no such table: dashboard_examplerecord`.
- **Fix:**
  1. Run `python manage.py migrate` (initial migration is already committed).
  2. If you recently changed models, run `python manage.py makemigrations dashboard` followed by `python manage.py migrate`.
  3. Run `python scripts/reset_db.py` to delete `db.sqlite3` and rerun migrations automatically.
- **Prevention:** Follow the checklist in See ::--:: docs/MIGRATIONS_CHECKLIST.md

## pandas ImportError
- **Symptom:** `ModuleNotFoundError: No module named 'pandas'`.
- **Fix:** Activate your virtual environment and run `pip install -r requirements.txt`.
- **Prevention:** Confirm you are in the correct venv before running Django commands (`which python` or `where python`).

## Server Port Already in Use
- **Symptom:** `Error: That port is already in use.`
- **Fix:**
  1. Stop any running `python manage.py runserver` sessions.
  2. Start the server on a new port: `python manage.py runserver 127.0.0.1:8001`.

## Templates Not Updating
- **Symptom:** You edit a template but the browser shows the old version.
- **Fix:**
  1. Refresh the page with cache bypass (Ctrl+F5 / Cmd+Shift+R).
  2. Ensure you saved the file in your editor.
  3. Check the render function in `dashboard/views.py` to confirm the template path is correct.

## Tests Failing After Edits
- **Symptom:** `AssertionError: 404 != 200` when running `python manage.py test dashboard`.
- **Fix:**
  1. Confirm the route still exists in `dashboard/urls.py`.
  2. Verify you used `reverse("dashboard:home")` instead of hard-coded paths.
  3. Run `python manage.py runserver` and visit the failing URL to inspect the error page.

## Still Stuck?
- Compare your branch against main with `git diff main...HEAD`.
- Search the Django Forum, Stack Overflow (`django` tag), or the Django Discord.
- Ask for help by describing the error, what you tried, and the steps to reproduce it.
