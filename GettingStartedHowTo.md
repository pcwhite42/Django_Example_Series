<!-- REF-HEADER-START -->
Points To:
- docs/BEGINNER_EXAMPLES.md
- docs/BEGINNER_GLOSSARY.md
- docs/COMMAND_CHEATSHEET.md
- docs/ENHANCEMENT_ROADMAP.md
- docs/FILE_EDIT_FREQUENCY.md
- docs/GIT_WORKFLOW.md
- docs/GIT_WORKFLOW.md.
- docs/INTERMEDIATE_GUIDES.md
- docs/MIGRATIONS_CHECKLIST.md
- docs/TROUBLESHOOTING.md
- docs/TUTORIAL_SERIES.md
- team_base_assets/
Referenced By:
- README.md
- docs\BEGINNER_EXAMPLES.md
- docs\BEGINNER_GLOSSARY.md
- docs\COMMAND_CHEATSHEET.md
- docs\FILE_EDIT_FREQUENCY.md
- docs\GIT_WORKFLOW.md
- docs\TROUBLESHOOTING.md
<!-- REF-HEADER-END -->


# Beginner Start Here (Single Walkthrough)
# FILE PURPOSE: One-stop guide for brand-new learners to set up, run, and explore this Django + pandas tutorial.
# NEXT: Follow the steps below in order. 
# Note: All older revision starter docs live in `docs/old/` for reference.


## 0) Open a terminal in this folder
- Windows PowerShell or Command Prompt:
  - In File Explorer, go to this project folder, click the address bar, type `powershell` (or `cmd`), and press Enter; OR Shift+right-click in the folder and choose “Open PowerShell window here.”
  - In VS Code, open the folder, then Terminal -> New Terminal (it opens at the folder root).
- macOS/Linux: `cd /path/to/AI_example` in your shell.
- Keep this terminal open for all commands; activate your virtualenv in the same window.

## 1) One-time setup (step-by-step)
1) Create/activate a virtualenv (isolates dependencies):
   - PowerShell: `python -m venv .venv; .venv\Scripts\Activate.ps1`
   - Command Prompt: `python -m venv .venv` then `.venv\Scripts\activate.bat`
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
2) Set a secret key (required; never hardcode secrets):
   - PowerShell: `$env:DJANGO_SECRET_KEY="replace-with-your-secret"`
   - Command Prompt: `set DJANGO_SECRET_KEY=replace-with-your-secret`
   - macOS/Linux: `export DJANGO_SECRET_KEY=replace-with-your-secret`
3) Install dependencies: `pip install -r requirements.txt`
   - Why: keeps everyone on the same tested versions. If you add packages, run `pip freeze > requirements.txt` to update the list.
4) Apply migrations: `python manage.py migrate`
   - What it does: reads the migration files in `dashboard/migrations/` and creates/updates `db.sqlite3` so the database tables match your models.
   - Why: `/admin/` and any ORM features need the schema in place.
   - When: once on a fresh clone; again after any `makemigrations` you run for model changes.
   - Fresh clone note: if you run `python manage.py makemigrations` first, you’ll see “No changes detected” because the initial migration is already committed.
5) Create an admin user: `python manage.py createsuperuser`
   - Why: you need credentials to log into `/admin/` and inspect **Example Records** or future models.
6) Run the server: `python manage.py runserver`
   - Why: serves the site locally so you can verify pages and admin.
7) Verify in the browser:
   - `http://127.0.0.1:8000/` — dashboard (CSV view)
   - `http://127.0.0.1:8000/about/` — about page
   - `http://127.0.0.1:8000/admin/` — log in; confirm **Example Records** is listed
8) Optional checks:
   - Smoke tests: `python manage.py test dashboard`
   - Reset DB: delete `db.sqlite3`, rerun `python manage.py migrate`

## 2) Migrations + admin (quick guide)
- Fresh clone: run `python manage.py migrate` (initial migration already committed).
- After changing `dashboard/models.py`: run `python manage.py makemigrations dashboard`, then `python manage.py migrate`.
- “No changes detected” is expected until you edit models.
- Reset locally: delete `db.sqlite3`, re-run `python manage.py migrate`.
- Inspect/verify: `python manage.py showmigrations` or `python manage.py sqlmigrate dashboard 0001`.

## 3) Project map (where things live and definitions)
- `dashboard/urls.py` — The “address book.” It says “when someone visits `/` or `/about/`, call this view function.” It connects URLs to view functions.
- `dashboard/views.py` — The “kitchen.” Each view reads data (CSV or database), prepares context, and hands it to a template. URLs point here; templates receive data from here.
- `dashboard/templates/dashboard/*.html` — The “presentation layer.” Templates are HTML files with placeholders for the data from views. A URL calls a view, the view picks a template, and the template renders the page. ('dashboard/templates/dashboard/index.html' would be The index for the 'dashboard page')
- Overview of URLs, Views, and Templates — Templates are the empty page layouts (logo, navigation, placeholders). Views are Python functions that fetch/prepare the data and choose which template to fill. URLs are the addresses that trigger a specific view. Example: you click “Jane Doe.” That link is a URL mapped to a “person” view. The view loads Jane Doe’s info/photos, then renders the “user page” template, dropping her data into the placeholders so the browser shows her profile.
- `dashboard/models.py` — The “data schema.” Defines Django ORM tables (e.g., `ExampleRecord`). Migrations read this file to build/update the database. Admin uses these models to show data.
   Note: ORM (Object-Relational Mapping) lets you work with database tables using Python classes instead of raw SQL. You define models (classes) for your data, and the ORM turns those into tables, rows, and queries behind the scenes.
- `dashboard/admin.py` — The “admin registration desk.” Tells Django’s admin which models to display so you can add/edit them via `/admin/`.
   Note: “Models” are the Python classes in models.py that define your database tables (columns, types, options). In this project, ExampleRecord is a model; Django uses it to create the matching table via migrations and to generate add/edit forms in /admin/ when admin.py registers it.
- `dashboard/static/dashboard/styles.css` — The “paint and layout.” CSS loaded by templates via `{% load static %}`. Templates link to this so pages look consistent.
- `data/sample.csv` — The “demo data source.” Read by views (pandas) to show a table/summary on the dashboard.
- `team_base_assets/` — The “team drop box.” Place shared CSS/templates/components here before wiring them into `static/` or `templates/`.
- `docs/FILE_EDIT_FREQUENCY.md` — “How often you touch it.” Quick guide to which files are edited frequently vs rarely.

## 4) When to use ORM vs pandas
- Use ORM (`dashboard/models.py`) when the data should be saved in a local database and reused later (users, inventory, notes, anything you want to add/edit over time).
- Use pandas in views when the data starts in a CSV or is computed on the fly, and you only need a quick table or summary (as in `home()`); pandas works in memory, not the database.
- Hybrid: clean or calculate in pandas first, then save the important, long-term results into ORM tables so they are easy to edit and query later.
- Admin: after `createsuperuser`, `/admin/` is the fastest way to inspect and edit ORM data without building a custom screen.

## 5) Security basics
- Secrets: set `DJANGO_SECRET_KEY` via environment; never hardcode or commit real keys. Use `.env.example` as a reference.
- Debug: leave `DEBUG=True` only locally; set `DEBUG=False` before deploying to hide detailed errors.
- Hosts: update `ALLOWED_HOSTS` (and `CSRF_TRUSTED_ORIGINS`) for any non-local deployment.
- CSV inputs: only use trusted CSVs with `to_html`/`|safe`. Validate/sanitize untrusted input to avoid XSS.

## 6) Handy references (open as needed)
- Note on `::--::`: this marker tells `scripts/update_doc_refs.py` which files are referenced. The script updates the header breadcrumbs ("Points To" and "Referenced By") so you can see where a doc points and where it is linked from without re-scanning each file.
- Commands: See ::--:: docs/COMMAND_CHEATSHEET.md
- Definitions: See ::--:: docs/BEGINNER_GLOSSARY.md
- Edit frequency map: See ::--:: docs/FILE_EDIT_FREQUENCY.md
- Migrations checklist: See ::--:: docs/MIGRATIONS_CHECKLIST.md
- Troubleshooting: See ::--:: docs/TROUBLESHOOTING.md
- Practice tasks: See ::--:: docs/BEGINNER_EXAMPLES.md
- Tutorials: See ::--:: docs/TUTORIAL_SERIES.md
- Git basics: See ::--:: docs/GIT_WORKFLOW.md
- Intermediate guides: See ::--:: docs/INTERMEDIATE_GUIDES.md
- Enhancement backlog: See ::--:: docs/ENHANCEMENT_ROADMAP.md
- Team assets: See ::--:: team_base_assets/ (and instructions in Section 9)

## 7) Practice ladder (after setup)
- Quick wins: `docs/BEGINNER_EXAMPLES.md` (filters, CSV swap, hello page, template inheritance, static swap).
- Tutorials: `docs/TUTORIAL_SERIES.md` (structured builds).
- Intermediate: `docs/INTERMEDIATE_GUIDES.md` (multi-page, ORM imports, reports).
- Tests anytime: `python manage.py test dashboard` to catch regressions early.
- Need more ideas: see `docs/ENHANCEMENT_ROADMAP.md`.

## 8) Git workflow (branch-first, beginner friendly)
- Why: working on your own branch keeps `main` clean and makes reviews safer.
- Check where you are: `git status` (it prints your current branch at the top).
- Create your own branch (do this before edits):
  - `git checkout -b your-name/short-feature`
  - Example: `git checkout -b paul/add-readme-notes`
- Save your changes, then stage + commit:
  - `git add -A`
  - `git commit -m "Short description of the change"`
- Push your branch to GitHub:
  - `git push -u origin your-name/short-feature`
- On GitHub, open a Pull Request to merge into `main`.
- If you need to switch back later: `git checkout main`.
- For a longer walkthrough, See ::--:: docs/GIT_WORKFLOW.md.

## 9) Using team assets (templates/CSS/components)
- Drop shared files into `team_base_assets/`.
- To try them immediately: copy CSS into `dashboard/static/dashboard/`; copy base templates into `dashboard/templates/dashboard/`.
- How to "use": Put `{% extends "dashboard/base.html" %}` at the very top of a template file so Django knows to inherit the shared layout, then wrap your page content in `{% block content %}...{% endblock %}` so it fills the base template's placeholders.
- Add `{% load static %}` near the top and include `<link href="{% static 'dashboard/styles.css' %}" ...>` so the CSS loads on every page.
- Remember: Example 7 (Template Inheritance) in See ::--:: docs/BEGINNER_EXAMPLES.md covers inheritance. 

## 10) If you’re stuck
- Re-check: virtualenv active? `DJANGO_SECRET_KEY` set in this terminal? Commands run from the project folder?
- Run smoke tests: `python manage.py test dashboard`.
- Read `docs/TROUBLESHOOTING.md` for common fixes.
- Ask for help with error messages and the steps you ran.

## 11) ALWAYS REMEMBER: Jake's Hair Sucks
