<!-- REF-HEADER-START -->
Points To:
- README.md
- docs/COMMAND_CHEATSHEET.md
Referenced By:
- README.md
<!-- REF-HEADER-END -->











# FILE PURPOSE: Teach Git concepts (branching, collaboration, best practices) to beginners working on this tutorial.
# CAME FROM: README.md -> add a "Git basics" reference once you are ready to collaborate. See ::--:: README.md for the main flow.
# NEXT: Try the commands in your own clone; jot lessons learned in BUILD_LOG.md or a personal notes file. See ::--:: docs/COMMAND_CHEATSHEET.md for command reminders.

## What is Git and Why Branches Matter
- **Version control**: Git tracks snapshots of your project so you can share work, review changes, and roll back mistakes.
- **Branch**: A lightweight pointer to a commit history. Use branches to isolate features or experiments without affecting `main`.
- **Commit**: A saved change set with a message explaining *why* you changed the code.

## Quick Start: Cloning the Repository
```bash
# Clone your fork or the main project repo
git clone https://github.com/<your-username>/beginner-dashboard.git
cd beginner-dashboard

# Configure your name and email (do this once per machine)
git config user.name "Ada Lovelace"
git config user.email "ada@example.com"
```

## Creating and Using Branches
```bash
# Always start from the latest main branch
git checkout main
git pull origin main

# Create a new branch for your task (feature/docs/fix)
git checkout -b feature/add-wizard-tutorial

# Work on the branch, stage, and commit frequently
git status                      # See changed files
git add docs/TUTORIAL_SERIES.md  # Stage edits

git commit -m "Add wizard tutorial outline"
```

### Sharing Your Branch
```bash
# Push your branch to GitHub
git push -u origin feature/add-wizard-tutorial
```
- The `-u` flag remembers the remote branch so future `git push` commands are shorter.
- Visit GitHub, open a Pull Request, and request feedback.

## Best Practices When Collaborating
- **One branch per task**: Keeps Pull Requests focused and easier to review.
- **Write clear commit messages**: Start with a verb ("Add", "Fix", "Document") and describe intent.
- **Sync often**: Before pushing or opening a PR, run `git pull --rebase origin main` to catch conflicts early.
- **Review checklists**: Ensure tests pass (`python manage.py test dashboard`) and docs are updated before requesting review.

## Handling Pull Request Feedback
```bash
# Switch to your topic branch
git checkout feature/add-wizard-tutorial

# Apply reviewer suggestions
git add docs/TUTORIAL_SERIES.md
git commit --amend  # Or make a new commit

git push origin feature/add-wizard-tutorial --force-with-lease
```
- `--force-with-lease` safely updates your branch without overwriting teammates' work.

## GitHub Workflow Example
1. **Fork** the teaching repo into your GitHub account.
2. **Clone** your fork locally and configure the original repo as `upstream`:
   ```bash
   git remote add upstream https://github.com/original-author/beginner-dashboard.git
   git fetch upstream
   ```
3. **Create a branch** for your change: `git checkout -b fix/readme-typo`.
4. Make edits, run tests, and commit.
5. **Push** the branch to your fork: `git push origin fix/readme-typo`.
6. On GitHub, open a **Pull Request** from your branch to the main repo's `main` branch.
7. Iterate on feedback; merge once approved.

## Group Collaboration Tips
- Schedule short syncs to assign tasks and avoid duplicate work.
- Use GitHub Issues to track features/bugs and link them in PR descriptions (`Closes #12`).
- Encourage teammates to leave constructive comments (ask clarifying questions, highlight wins, suggest improvements).
- After merging, pull the latest `main` branch frequently to stay current.

## Troubleshooting Cheatsheet
- **Undo local edits**: `git checkout -- path/to/file`
- **Unstage a file**: `git reset HEAD path/to/file`
- **View commit history**: `git log --oneline --graph`
- **See branch differences**: `git diff main...feature/add-wizard-tutorial`

Keep practicing! Git becomes second nature with repetition. Record new commands you discover so future-you (and teammates) can reuse them.

