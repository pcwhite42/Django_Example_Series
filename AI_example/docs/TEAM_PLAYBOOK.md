<!-- REF-HEADER-START -->
Points To:
Referenced By:
<!-- REF-HEADER-END -->











# FILE PURPOSE: Establish collaboration habits for student teams working through this tutorial.
# CAME FROM: ENHANCEMENTS.md -> provides norms once learners start pairing or opening PRs.
# NEXT: Review this document during your first team sync and adapt it to your workflow.

## Roles and Responsibilities
- **Driver:** Actively edits code, narrates changes, and references breadcrumbs (e.g., “CAME FROM dashboard/views.py”).
- **Navigator:** Follows along, checks docs (README, WALKTHROUGH, CHECKLISTS), and spots bugs or missing steps.
- **Reviewer:** Reads Pull Requests, runs tests, and ensures instructions remain beginner-friendly.
Rotate roles frequently so everyone practices each skill.

## Daily Habits
1. **Sync on priorities:** Start standups by glancing at `ENHANCEMENTS.md` and open issues.
2. **Update BUILD_LOG.md:** Log each collaborative task (append-only) with timestamps.
3. **Test before sharing:** Run `python manage.py test dashboard` (or `python scripts/reset_db.py` + migrate) before pushing.
4. **Celebrate learning:** Use a shared document to track lessons learned, tricky errors, or shortcuts discovered.

## Branch & Pull Request Workflow
1. Branch from `main`: `git checkout -b feature/<short-description>`.
2. Keep commits focused; reference the tutorial phase or doc you touched in the commit message.
3. Open Pull Requests early (`Draft` state) to ask for feedback. Include:
   - What changed (files + docs).
   - Screenshots or command outputs if relevant.
   - Checklist: tests, migrations, docs updates.
4. Reviewers comment inline, request changes, or approve once satisfied.
5. Merge via GitHub once approvals/tests pass; delete merged branches to keep the tree clean.

## Issue Management
- Use GitHub Issues labels like `docs`, `beginner-task`, `bug`, `enhancement`.
- Link issues in Pull Requests (`Fixes #12`) and close them only after the tutorial/docs are updated.
- Create fatigue-free issues: include reproduction steps, expected vs. actual behavior, and suggested next experiments.

## Pair Programming Tips
- Share your screen and keep `docs/ONBOARDING_PORTAL.md` open as a map.
- Narrate your thought process; when stuck, consult `docs/TROUBLESHOOTING.md`.
- Pause every 20–30 minutes to summarize progress and verify tests still pass.

## Retrospectives
- Weekly or milestone-based, answer:
  - What helped a beginner succeed this week?
  - Which parts of the docs need clarifying?
  - Which command or script saved time (add to cheat sheet if missing)?
- Translate action items into new tasks in `ENHANCEMENTS.md` or GitHub Issues.

## Conflict Resolution
- Default to the teaching style in existing files (breadcrumbs, plain language).
- If disagreement arises, prototype the options on separate branches, test both, and compare.
- Escalate decisions by documenting pros/cons in the Pull Request description and tagging the maintainer.

## Staying Beginner-Friendly
- Whenever you add a feature or automation, update:
  - `README.md` -> “Learn more” section.
  - `docs/ONBOARDING_PORTAL.md` -> appropriate phase.
  - `docs/TROUBLESHOOTING.md` -> new failure modes and fixes.
- Keep code comments clear, avoid jargon, and link to docs when referencing advanced concepts.
