<!-- REF-HEADER-START -->
Points To:
- docs/TROUBLESHOOTING.md
Referenced By:
- README.md
- docs\TROUBLESHOOTING.md
<!-- REF-HEADER-END -->












# FILE PURPOSE: Provide a repeatable checklist for running `makemigrations` and `migrate` safely.
# NEXT: Print this list or copy it into your BUILD_LOG.md when you modify `dashboard/models.py`.
# Points To: (auto-managed by script) 
# Referenced By: (auto-managed by script)

## Before You Run `makemigrations`
1. **Confirm the change:** Highlight the exact fields you added/removed in `dashboard/models.py`.
2. **Ensure clean working tree:** `git status` should show only intentional edits.
3. **Revisit data:** Decide whether you need to back up `db.sqlite3` (this repo ignores the file, so copy it first if your local data matters).
   - Why: Backups let you restore data if a migration goes wrong.

## Generate the Migration
4. Run `python manage.py makemigrations dashboard`.
   - Expect Django to create or modify a file in `dashboard/migrations/`. On a fresh clone, seeing `No changes detected` is normal because the initial migration is already committed.
   - If you expected a new file, confirm you saved `dashboard/models.py` and that you targeted the app (`python manage.py makemigrations dashboard`).
   - Why: makemigrations records schema changes so they can be shared and replayed.
5. Open the generated migration and skim the operations (look for `AddField`, `AlterField`, etc.) so you understand what will happen.
   - Why: Reading the migration helps you catch unintended schema changes before applying them.

## Apply the Migration
6. Run `python manage.py migrate`.
7. Watch for success messages (`OK`). If there is an error, read the troubleshooting tips in See ::--:: docs/TROUBLESHOOTING.md
   - Why: migrate applies the recorded changes so your database schema matches your models.

## After the Migration
8. Run the smoke tests: `python manage.py test dashboard`.
9. Start the server (`python manage.py runserver`) and verify the affected pages and `/admin/`.
10. Add notes to `BUILD_LOG.md` (or your team's log) so others know what changed and why.
11. Commit the migration file(s) along with the model changes (and any test updates).
   - Why: Tests and notes catch regressions early; committing migrations keeps teammates in sync.
