# FILE PURPOSE: Delete the local SQLite database and rerun migrations in one command.
# NEXT: Run `python scripts/reset_db.py` from the project root whenever you want a clean slate.

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    db_path = repo_root / "db.sqlite3"

    if db_path.exists():
        db_path.unlink()
        print(f"[reset_db] Deleted {db_path.name}")
    else:
        print("[reset_db] No db.sqlite3 found; continuing with migrate")

    try:
        subprocess.run(
            [sys.executable, "manage.py", "migrate"],
            cwd=repo_root,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        print("[reset_db] Migrate failed. See error above and rerun manually.")
        raise SystemExit(exc.returncode) from exc

    print("[reset_db] Database recreated via `python manage.py migrate`")


if __name__ == "__main__":
    main()
