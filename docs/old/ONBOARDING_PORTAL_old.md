<!-- REF-HEADER-START -->
Points To:
Referenced By:
<!-- REF-HEADER-END -->










# Beginner Dashboard Onboarding Portal
# FILE PURPOSE: Give first-time learners a single entry point that links every guide, example, and workflow in order.
# NEXT STEP: Follow each numbered phase; every action tells you which file to open and what to focus on.

## Phase 0: Get Ready
1. **Install Python** (3.10+ recommended). If you are unsure, run `python --version` in your terminal.
2. **Duplicate `.env.example`** to `.env` and set `DJANGO_SECRET_KEY` when prompted by the setup steps.
3. Skim the three paragraph overview below so you know what is coming next:
   - We will set up a virtual environment.
   - We will run the project and explore the dashboard and admin.
   - We will learn Git basics for collaboration.

## Phase 1: Core Setup (Start Here)
1. Open `README.md`.
   - Read through the "Python & dependencies" section to prepare your virtual environment.
   - Follow the "Database + admin onboarding" commands exactly; expect "No changes detected" when running `makemigrations` on a fresh clone.
   - Run all commands in a terminal pointed at the project folder (where `manage.py` lives) after setting `DJANGO_SECRET_KEY` for your shell (see `.env.example` for PowerShell/Command Prompt/macOS/Linux examples).
2. Still in `README.md`, check the "Run it checklist" and complete each item.
   - Confirm `python manage.py runserver` starts the site.
   - Visit `/`, `/about/`, and `/admin/` to verify the app is running.
3. Optional: Install the pinned versions with `pip install -r requirements.txt` if you want the exact tested environment.
4. Wrap Phase 1 by running `python manage.py test dashboard` so you trust the baseline before editing.
5. Optional: use `python scripts/reset_db.py` anytime you need to rebuild the database from scratch.

## Phase 2: Learn the Code Flow
1. Open `WALKTHROUGH.txt`.
   - Study the **Project Map** to understand each file’s role.
   - Follow the **Follow the Breadcrumbs** section to trace a request from URL to view to template.
2. Open `dashboard/views.py` and read the breadcrumb comments (`# CAME FROM`, `# NEXT`) to see how pandas transforms data.
3. Hop to `dashboard/urls.py` and confirm how URL paths map to view functions.
4. Review `dashboard/templates/dashboard/index.html` to connect context variables to rendered HTML.

## Phase 3: Practice with Guided Examples
1. Open `docs/BEGINNER_EXAMPLES.md` and pick one exercise.
   - Example suggestion: add a GET filter to the dashboard.
   - After finishing an exercise, update the inline breadcrumbs to reflect your changes.
2. Try another example to reinforce pandas manipulations or template updates.
3. Record what you built in your own notes or a personal fork README.

## Phase 4: Level Up with Tutorials
1. Open `docs/TUTORIAL_SERIES.md`.
   - Start with Tutorial 1 if you want to rebuild the entire project from scratch.
   - Tutorial 2 teaches inline charting using pandas only.
   - Tutorial 3 introduces a mini reporting wizard with GET parameters and exports.
2. After each tutorial, run `python manage.py test dashboard` to ensure smoke tests still pass.

## Phase 5: Move Toward Intermediate Skills
1. Open `docs/INTERMEDIATE_GUIDES.md` once you are comfortable with the basics.
   - Choose a guide such as importing CSV data into the ORM or building multi-page reports.
   - Each guide lists stretch goals for deeper exploration.
2. As your features grow, remember to revisit `README.md` to adjust migrations, admin views, or settings appropriately.

## Phase 6: Learn Git & Collaboration
1. Open `docs/GIT_WORKFLOW.md` for a gentle Git primer.
   - Learn what branches are, how to create them, and how to push to GitHub.
   - Practice the step-by-step Pull Request workflow, even if you are collaborating with imaginary teammates.
2. Add items from `ENHANCEMENTS.md` to your personal task list and create branches for each task.
3. When working with others, use GitHub Issues and Pull Requests to coordinate efforts.
4. Read `docs/TEAM_PLAYBOOK.md` together so everyone shares collaboration norms.

## Phase 7: Plan Future Enhancements
1. Review `ENHANCEMENTS.md` to see open ideas (command cheat sheet, team playbook, more automation helpers)..
2. Pick one enhancement and create a new branch following the Git workflow guide.
3. Log your progress in `BUILD_LOG.md` to keep the append-only history intact.

## Quick Reference (One-Line Pointers)
- Setup checklist: `README.md` (Phase 1)
- File-by-file tour: `WALKTHROUGH.txt` (Phase 2)
- Practice drills: `docs/BEGINNER_EXAMPLES.md` (Phase 3)
- Structured tutorials: `docs/TUTORIAL_SERIES.md` (Phase 4)
- Intermediate roadmap: `docs/INTERMEDIATE_GUIDES.md` (Phase 5)
- Command quick reference: `docs/COMMAND_CHEATSHEET.md` (use throughout)
- Git primer: `docs/GIT_WORKFLOW.md` (Phase 6)
- Troubleshooting guide: `docs/TROUBLESHOOTING.md` (Phase 7)
- Enhancement backlog: `ENHANCEMENTS.md` (Phase 7)
- History of changes: `BUILD_LOG.md` (Review anytime)

Follow the phases in order, revisit earlier notes when you feel stuck, and invite peers to go through the same path so everyone shares common vocabulary and expectations.
