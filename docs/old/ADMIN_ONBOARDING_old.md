<!-- REF-HEADER-START -->
Points To:
Referenced By:
<!-- REF-HEADER-END -->



























# FILE PURPOSE: Admin onboarding checklist so beginners can get into /admin quickly.
# CAME FROM: dashboard/admin.py -> registering ExampleRecord points here for the setup commands.
# NEXT: After finishing these basics, open WALKTHROUGH.txt for the full project tour (created later in this tutorial).

## Create the database tables

1. From a terminal in the project folder (where `manage.py` lives), run `python manage.py migrate`
   - The initial migration for `dashboard.ExampleRecord` is already committed here, so running `python manage.py makemigrations` immediately after cloning will print `No changes detected.` That message is expected until you edit `dashboard/models.py`.
   - Use `python manage.py makemigrations dashboard` only after you change the models (or if you intentionally want to regenerate the initial migration) before re-running `python manage.py migrate`.
2. After you change the models, generate a new migration with `python manage.py makemigrations dashboard`, then apply it with `python manage.py migrate`.

### Reset the local database (optional)

- Delete the local `db.sqlite3` file (the repo ignores it) and rerun `python manage.py migrate` to recreate the schema from scratch.

## Create a superuser account

- `python manage.py createsuperuser`
- Follow the prompts to set a username, email (optional), and password.

## Verify in the browser

1. Start the server with `python manage.py runserver`.
2. Visit `http://127.0.0.1:8000/admin/`.
3. Log in with the superuser credentials you just created and confirm **Example Records** appears in the sidebar.
