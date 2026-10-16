"""Coldline.

===================

File:              tests/unit/test_student_tests_runner.py
Component:         Unit tests — Student test stage
Purpose:           Prove the student-test stage passes on an empty tests/student and fails
                    on a failing test.
Interacts With:    tests/student_tests.py, pyproject.toml (`poe student-tests`)
Sprint/Task:       Sprint 5 — Project 5 / starter (Task 5.1)
Concepts:          pytest exit codes, an empty starter directory
Tools:             Python 3.12, pytest
"""

from __future__ import annotations

from pathlib import Path

from tests import student_tests


def test_an_empty_directory_passes(tmp_path: Path) -> None:
    """The starter has no student tests yet; that is a pass."""
    (tmp_path / "__init__.py").write_text("", encoding="utf-8")
    assert student_tests.run(tmp_path) == 0


def test_a_failing_test_fails(tmp_path: Path) -> None:
    """A failing student test fails the stage."""
    (tmp_path / "test_x.py").write_text("def test_x():\n    assert False\n", encoding="utf-8")
    assert student_tests.run(tmp_path) == 1


def test_a_passing_test_passes(tmp_path: Path) -> None:
    """A passing student test passes the stage."""
    (tmp_path / "test_x.py").write_text("def test_x():\n    assert True\n", encoding="utf-8")
    assert student_tests.run(tmp_path) == 0
