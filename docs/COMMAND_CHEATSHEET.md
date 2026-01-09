<!-- REF-HEADER-START -->
Points To:
- GettingStartedHowTo.md
Referenced By:
- GettingStartedHowTo.md
- README.md
- docs\GIT_WORKFLOW.md
<!-- REF-HEADER-END -->














# Command Cheatsheet
# FILE PURPOSE: Quick reference for the most common commands used throughout the tutorials.
# NEXT: Keep this tab open while working through the phases in GettingStartedHowTo.md See ::--:: GettingStartedHowTo.md
# RUN FROM: A terminal pointed at the project folder (where `manage.py` lives) after activating your virtual environment and setting `DJANGO_SECRET_KEY` for your shell.
# WHY: Virtualenv keeps dependencies isolated; setting the secret key is required before Django will start.
# Points To: (auto-managed by script) 
# Referenced By: (auto-managed by script)

## Virtual Environment & Dependencies
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1      # PowerShell
.venv\Scripts\activate.bat      # Command Prompt
source .venv/bin/activate        # macOS/Linux
pip install -r requirements.txt  # Install exact tested versions
pip install <package>            # Add a new dependency inside your virtualenv
pip freeze > requirements.txt    # Regenerate requirements.txt after adding/removing packages
# WHY: Update requirements.txt so teammates (and future you) can recreate the same environment.
```

## Django Management Commands
```bash
python manage.py runserver              # Start the local development server
python manage.py makemigrations         # Generate migrations after changing models
python manage.py makemigrations dashboard  # Limit migration generation to this app
python manage.py migrate                # Apply migrations to the database
python manage.py createsuperuser        # Create an admin account
python manage.py test dashboard         # Run the smoke tests
# WHY: makemigrations/migrate keep DB schema in sync; createsuperuser lets you into /admin; tests catch regressions early.
```

## Database Maintenance
```bash
python manage.py showmigrations         # Verify which migrations have run
python manage.py sqlmigrate dashboard 0001  # Inspect generated SQL before applying
python manage.py flush                  # Reset the database (drops data, keeps schema)
python scripts/reset_db.py              # Delete db.sqlite3 and rerun migrate
# WHY: These commands help you inspect, reset, or rebuild the DB safely.
```

## Helpful Python Snippets (Run in `python manage.py shell`)
```python
from pathlib import Path
from dashboard.models import ExampleRecord
from django.conf import settings

print(Path(settings.BASE_DIR) / "data" / "sample.csv")
print(ExampleRecord.objects.count())
```

## pandas Debug Helpers (Use sparingly, then remove)
```python
# Inside dashboard/views.py
print(data_frame.head())  # Quick peek at the first five rows
print(summary.round(2))   # Check summary stats without HTML formatting
```

## Git Basics (When Collaborating)
```bash
git status                              # See current changes
git checkout -b feature/my-task         # Create a new branch
git add path/to/file                    # Stage changes
git commit -m "Describe what changed"   # Commit staged changes
git pull --rebase origin main           # Sync with latest main
git push -u origin feature/my-task      # Publish your branch
```

Refer back to `docs/GIT_WORKFLOW.md` for a deeper explanation of branches, forks, and Pull Requests.
