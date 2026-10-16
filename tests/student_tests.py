"""Coldline.

===================

File:              tests/student_tests.py
Component:         Student test stage
Purpose:           Run your tests under tests/student; an empty directory is a pass, not an
                    error.
Interacts With:    pyproject.toml (`poe student-tests`, `poe verify`), tests/student/
Sprint/Task:       Sprint 5 — Project 5 / starter (Task 5.1)
Concepts:          pytest exit codes, an empty starter directory
Tools:             Python 3.12, pytest

pytest exits 5 when it collects nothing. The starter's tests/student holds only __init__.py
until you add your first test in Task 1, so that exit means "no tests yet", not a failure.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

STUDENT_TESTS = Path(__file__).resolve().parent / "student"
NO_TESTS_COLLECTED = 5


def run(directory: Path = STUDENT_TESTS) -> int:
    """Run pytest on ``directory`` in its own process; "no tests collected" counts as 0."""
    code = subprocess.run([sys.executable, "-m", "pytest", str(directory)], check=False).returncode
    return 0 if code == NO_TESTS_COLLECTED else code


def main() -> None:
    """Entry point for `poe student-tests`."""
    sys.exit(run())
