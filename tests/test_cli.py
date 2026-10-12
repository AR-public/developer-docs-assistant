"""Tests for the request-validation command-line interface."""

import pytest

from developer_docs_assistant.cli import main


def test_main_reports_success_without_echoing_question(
    capsys: pytest.CaptureFixture[str],
) -> None:
    result = main(["Where is the API guide?"])
    captured = capsys.readouterr()

    assert result == 0
    assert "Request validated." in captured.out
    assert "No model call was made" in captured.out
    assert "Where is the API guide?" not in captured.out
    assert captured.err == ""


def test_main_reports_invalid_question_to_stderr(
    capsys: pytest.CaptureFixture[str],
) -> None:
    result = main(["   "])
    captured = capsys.readouterr()

    assert result == 2
    assert captured.out == ""
    assert "question:" in captured.err
