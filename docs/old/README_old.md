<!-- REF-HEADER-START -->
Points To:
Referenced By:
<!-- REF-HEADER-END -->



























# FILE PURPOSE: Quick-start guide for the beginner Django + pandas tutorial project.
# CAME FROM: ADMIN_ONBOARDING.md -> after preparing the admin site, come here for the full environment checklist.
# NEXT: Open WALKTHROUGH.txt for a file-by-file tour and the "add a new page" recipe.

## Welcome

This repository teaches you how to combine **Django 5+** with **pandas** to render CSV data, wire up the admin site, and add new pages safely. Every file includes breadcrumbs so you always know where to head next.

**First stop for newcomers:** open [docs/ONBOARDING_PORTAL.md](docs/ONBOARDING_PORTAL.md) for a phase-by-phase roadmap that links every tutorial, example, and workflow.

## Python & dependencies

- Python 3.12+ recommended (3.10+ works if Django 5 is available on your platform).
- Install packages inside a virtual environment to keep your tooling isolated.

### Create & activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

```cmd
.venv\Scripts\activate.bat  # Windows Command Prompt
```

```bash
source .venv/bin/activate   # macOS/Linux shells
```

### Install Django + pandas

```bash
pip install "django>=5.0" pandas
```

Prefer a ready-to-go setup? Install the exact versions we used:

```bash
pip install -r requirements.txt
```

Adding a new library later? Install it in your virtualenv (e.g., `pip install requests`) and then update `requirements.txt` so teammates can recreate your environment (`pip freeze > requirements.txt`).

## Environment variables

1. Copy `.env.example` to `.env` (optional) or export the values directly.
2. Set `DJANGO_SECRET_KEY` before you run management commands.

```cmd
set DJANGO_SECRET_KEY=replace-with-your-secret  # Windows Command Prompt
```

```powershell
$env:DJANGO_SECRET_KEY="replace-with-your-secret"  # PowerShell
```

```bash
export DJANGO_SECRET_KEY=replace-with-your-secret  # macOS/Linux
```

Generate a secret key one time with:

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

## Django project scaffolding (already done here)

The repository already contains the results of these commands. Run them yourself if you want to rebuild from scratch:

```bash
django-admin startproject beginner_dashboard .
python manage.py startapp dashboard
```

## Database + admin onboarding

Open a terminal in the project folder (the one containing `manage.py`). The initial migration for `dashboard.ExampleRecord` ships with this repo, so on a fresh clone you can jump straight to applying migrations (this will create your local `db.sqlite3`, which the repo ignores):

```bash
python manage.py migrate
```

If you run `python manage.py makemigrations` right away, Django will print `No changes detected.` - that is normal until you edit `dashboard/models.py`. After you make model changes (or intentionally want to regenerate the initial migration), run:

```bash
python manage.py makemigrations dashboard
python manage.py migrate
```

Need a clean slate? Delete your local `db.sqlite3` file (the repo does not track it) and rerun `python manage.py migrate` to regenerate it.

Finish by creating a superuser and logging in:

```bash
python manage.py createsuperuser
```

Visit `http://127.0.0.1:8000/admin/`, log in with the superuser you created, and look for **Example Records** in the sidebar.

## Run it checklist

- [ ] Activate your virtual environment.
- [ ] Set `DJANGO_SECRET_KEY` (see `.env.example` for platform-specific notes).
- [ ] Install dependencies with `pip install "django>=5.0" pandas`.
- [ ] Apply migrations: `python manage.py migrate` (run `python manage.py makemigrations dashboard` first only after you edit `dashboard/models.py`; otherwise expect `No changes detected`).
- [ ] Optional: load demo data or tweak `data/sample.csv`.
- [ ] Optional: run smoke tests with `python manage.py test dashboard`.
- [ ] Start the server: `python manage.py runserver`.
- [ ] Visit `http://127.0.0.1:8000/` and confirm the CSV table and summary render.
- [ ] Visit `http://127.0.0.1:8000/about/` to confirm the new teaching page.
- [ ] Log into `http://127.0.0.1:8000/admin/` and explore **Example Records**.

## Learn more

- Step-by-step walkthrough: [WALKTHROUGH.txt](WALKTHROUGH.txt)
- Admin deep dive: [ADMIN_ONBOARDING.md](ADMIN_ONBOARDING.md)
- Settings tour: [beginner_dashboard/settings.py](beginner_dashboard/settings.py)
- Beginner practice menu: [docs/BEGINNER_EXAMPLES.md](docs/BEGINNER_EXAMPLES.md)
- Next-step roadmap: [docs/INTERMEDIATE_GUIDES.md](docs/INTERMEDIATE_GUIDES.md)
- Structured tutorials: [docs/TUTORIAL_SERIES.md](docs/TUTORIAL_SERIES.md)
- Command quick reference: [docs/COMMAND_CHEATSHEET.md](docs/COMMAND_CHEATSHEET.md)
- Git & collaboration primer: [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md)
- Team norms playbook: [docs/TEAM_PLAYBOOK.md](docs/TEAM_PLAYBOOK.md)
- Unified onboarding portal: [docs/ONBOARDING_PORTAL.md](docs/ONBOARDING_PORTAL.md)
- Troubleshooting guide: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- Migration checklist: [docs/MIGRATIONS_CHECKLIST.md](docs/MIGRATIONS_CHECKLIST.md)
- Quick reset helper: `python scripts/reset_db.py`
- Visual capture guide: [docs/VISUAL_CAPTURE_GUIDE.md](docs/VISUAL_CAPTURE_GUIDE.md)
- Enhancement roadmap: [docs/ENHANCEMENT_ROADMAP.md](docs/ENHANCEMENT_ROADMAP.md)

## Where to ask for help

- [Django Forum](https://forum.djangoproject.com/) - official community Q&A and discussions.
- Stack Overflow - use the `django` and `pandas` tags; share tracebacks and the steps you followed.
- [Django Discord](https://discord.gg/djangodevelopers) - real-time chat with learners and maintainers.
- Local notes - keep a personal log of commands you run and outcomes so you can debug faster and help teammates.
- GitHub Issues - use the Lesson Feedback template (`.github/ISSUE_TEMPLATE/lesson-feedback.md`) to report bugs or documentation gaps.

Remember: for production deployments, disable `DEBUG`, set `ALLOWED_HOSTS` to your real domain, add `CSRF_TRUSTED_ORIGINS`, and store secrets in the environment.
