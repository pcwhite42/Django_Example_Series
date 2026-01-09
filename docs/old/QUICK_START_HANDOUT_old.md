<!-- REF-HEADER-START -->
Points To:
Referenced By:
<!-- REF-HEADER-END -->



























# Quick Start Handout (Give This to Newcomers)
# FILE PURPOSE: One-page starter that tells beginners exactly which file to open first, what each key file does, and how to get familiar with the database.
# CAME FROM: README.md and docs/ONBOARDING_PORTAL.md -> this handout compresses their "start here" guidance into a single page.

## 1) Open This First
- File to open: `README.md`
- Why: It shows the one-time environment setup and the exact commands to run (`migrate`, `createsuperuser`, `runserver`).
- Next hop: Follow the "Database + admin onboarding" section inside `README.md`, then skim the "Run it checklist".
- Need a cheat sheet of which files you'll touch most? Open `docs/FILE_EDIT_FREQUENCY.md`.
- Unsure about a term? Check `docs/BEGINNER_GLOSSARY.md`.

## 2) Know These Files (Names + What They Do)
- `README.md` — Setup commands, environment variables, and the run checklist.
- `docs/ONBOARDING_PORTAL.md` — Phase-by-phase roadmap linking all tutorials.
- `WALKTHROUGH.txt` — File-by-file map and the URL -> view -> template breadcrumb trail.
- `dashboard/models.py` — Django models (includes the `ExampleRecord` demo table).
- `dashboard/admin.py` — Registers models in the admin; follow its breadcrumbs to `ADMIN_ONBOARDING.md`.
- `dashboard/urls.py` — App URL routes; points to views.
- `dashboard/views.py` — Reads CSVs with pandas and returns responses; see inline breadcrumbs.
- `dashboard/templates/dashboard/index.html` — Main dashboard template showing tables.
- `dashboard/migrations/0001_initial.py` — Shipped initial migration so fresh clones have the `ExampleRecord` table.
- `data/sample.csv` — Demo dataset the dashboard renders.
- `scripts/reset_db.py` — Helper to delete `db.sqlite3` and rerun migrations locally.
- `docs/FILE_EDIT_FREQUENCY.md` — Shows which files you edit often vs. rarely.

## 3) Steps to Get Familiar with the Database (Fast Path)
1) Open a terminal in the project folder (`cd` into the folder that contains `manage.py`). Then set a secret key (run one of these in that terminal **before** other commands) — why: Django refuses to start without a secret key and you should never hardcode it.
   - PowerShell: `$env:DJANGO_SECRET_KEY="replace-with-your-secret"`
   - Windows Command Prompt: `set DJANGO_SECRET_KEY=replace-with-your-secret`
   - macOS/Linux shells: `export DJANGO_SECRET_KEY=replace-with-your-secret`
2) In that same terminal, apply migrations (this creates a fresh `db.sqlite3`): `python manage.py migrate` — why: this syncs the database schema so `/admin/` and models work.
3) Still in the same terminal, create an admin user: `python manage.py createsuperuser` — why: you need credentials to log into `/admin/`.
4) Start the server from the same terminal: `python manage.py runserver` — why: serves the site locally so you can test `/`, `/about/`, and `/admin/`.
5) Visit:
   - `http://127.0.0.1:8000/` — dashboard view backed by `data/sample.csv`.
   - `http://127.0.0.1:8000/admin/` — log in and confirm **Example Records** is listed; open it to view/add rows.
6) Optional reset: delete your local `db.sqlite3` (it’s ignored by git) and rerun `python manage.py migrate`.

## 4) If You Get Stuck
- Re-read the breadcrumbs in `dashboard/views.py` and `dashboard/urls.py` — why: they show the path from URL to view to template when you’re lost.
- Run `python manage.py test dashboard` to ensure key routes still respond — why: quick regression check after edits.
- Check `docs/TROUBLESHOOTING.md` for common fixes — why: it lists the usual setup pitfalls.
- Glance at `docs/FILE_EDIT_FREQUENCY.md` to see which files are safe to edit frequently vs. rarely touched — why: helps avoid breaking rarely-touched plumbing.
- Need structure ideas? Browse `docs/BEGINNER_EXAMPLES.md` (quick wins) and `docs/TUTORIAL_SERIES.md` (longer builds) — why: they mirror classic beginner steps so you learn safely.

## 5) Where to Put Team Assets
- Drop shared CSS/templates/components into `team_base_assets/` for now; we’ll document integration steps after you add them — why: keeps source-controlled, reusable assets in one place.
- To try them immediately, copy CSS into `dashboard/static/dashboard/` and base templates into `dashboard/templates/dashboard/`, then wire them into your templates via `{% extends %}` and `{% static %}` — why: these are Django’s standard hooks for static files and template inheritance.
