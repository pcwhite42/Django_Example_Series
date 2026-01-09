<!-- REF-HEADER-START -->
Points To:
- README.md
Referenced By:
- README.md
<!-- REF-HEADER-END -->











# FILE PURPOSE: Quick edit frequency map so beginners know which files they will touch often vs. rarely.
# CAME FROM: README.md -> Quick index points here for edit-frequency context.
# NEXT: Keep it nearby while coding; update if your team’s habits change. See ::--:: README.md for the entry point.
# Points To: (auto-managed by script) 
# Referenced By: (auto-managed by script)

## Edit Frequency Map (from most frequent to rare)
- **dashboard/views.py** — Frequent. Core logic for loading CSVs and building context.
- **dashboard/templates/dashboard/index.html / about.html / hello.html** — Frequent. Layout/content tweaks.
- **dashboard/urls.py** — Frequent when adding routes.
- **dashboard/static/dashboard/styles.css** — Occasional for styling changes.
- **docs/BEGINNER_EXAMPLES.md** — Occasional when adding practice tasks.
- **README.md** — Occasional when setup steps change.
- **docs/COMMAND_CHEATSHEET.md** — Occasional to add/remove commands.
- **docs/MIGRATIONS_CHECKLIST.md** — Occasional when migration steps change.
- **docs/TUTORIAL_SERIES.md / docs/INTERMEDIATE_GUIDES.md** — Occasional as you add lessons.
- **beginner_dashboard/settings.py** — Rare; adjust only for new apps or security settings.
- **dashboard/models.py** — Occasional when schema changes; run `makemigrations` + `migrate`.
- **dashboard/admin.py** — Occasional when registering new models or admin tweaks.
- **manage.py / beginner_dashboard/asgi.py / wsgi.py** — Rare; leave as-is unless you know why you’re editing them.
