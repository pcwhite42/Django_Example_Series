<!-- REF-HEADER-START -->
Points To:
Referenced By:
<!-- REF-HEADER-END -->













# FILE PURPOSE: Track optional beginner-friendly improvements to tackle iteratively.
# CREATED: Step 21 of BUILD_LOG.md.

## Enhancement Ideas

- [x] Ship a `requirements.txt` (or versions file) capturing the minimal packages and versions tested in this tutorial so learners can install reproducible dependencies with `pip install -r requirements.txt`.
- [x] Add a `docs/command_cheatsheet.md` that groups the most common `manage.py` commands, pandas snippets, and troubleshooting tips on one page for quick reference.
- [x] Provide a short `scripts/` helper (e.g., `scripts/reset_db.py`) that safely deletes the local SQLite database and reruns `migrate`, teaching learners how to automate management tasks with Python.
- [x] Expand README with a "Where to ask for help" section (Stack Overflow tags, Discord communities, Django forums) so learners know support channels.
- [ ] Create step-by-step screenshots or animated GIFs showing `/admin/`, `/`, and the CLI commands to reduce friction for visual learners.
- [x] Add inline code comments demonstrating how to print debug DataFrames safely (`print(data_frame.head())`) and where to remove them afterward.
- [x] Offer a checklist for before/after running `python manage.py makemigrations` so beginners understand what files should change.
- [x] Introduce `docs/GIT_WORKFLOW.md` from README so beginners can find the branching guide quickly.
- [ ] Draft `docs/TEAM_PLAYBOOK.md` with norms for code reviews, pairing sessions, and retrospectives tailored to student teams.
- [x] Add a sample GitHub Issue template (`.github/ISSUE_TEMPLATE/lesson-feedback.md`) to encourage structured bug reports or tutorial feedback.
- [x] Provide a `docs/TROUBLESHOOTING.md` that catalogs common errors (missing SECRET_KEY, migrations not applied, pandas ImportError) with fixes.



